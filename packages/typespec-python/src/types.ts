import { Type } from "@typespec/compiler";
import { HttpAuth, Visibility } from "@typespec/http";
import {
    SdkContext,
    SdkEnumValueType,
    SdkType,
    SdkModelType,
    SdkBodyModelPropertyType,
    SdkUnionType,
    SdkEnumType,
    SdkBuiltInType,
    SdkArrayType,
    SdkDictionaryType,
    SdkConstantType,
    SdkDatetimeType,
    SdkDurationType,
    getClientType,
    shouldFlattenProperty,
} from "@azure-tools/typespec-client-generator-core";
import { dump } from "js-yaml";
import { camelToSnakeCase } from "./utils.js";
import { getModelsMode } from "./emitter.js";

export const typesMap = new Map<SdkType, Record<string, any>>();
export const simpleTypesMap = new Map<string | null, Record<string, any>>();

export interface CredentialType {
    kind: "Credential";
    scheme: HttpAuth;
}

export interface CredentialTypeUnion {
    kind: "CredentialTypeUnion";
    types: CredentialType[];
}

function isEmptyModel(type: SdkType): boolean {
    // object, {} will be treated as empty model, user defined empty model will not
    return (
        type.kind === "model" &&
        type.properties.length === 0 &&
        !type.baseModel &&
        !type.discriminatedSubtypes &&
        !type.discriminatorValue &&
        (type.name === "" || type.name === "object")
    );
}

function getSimpleTypeResult(result: Record<string, any>): Record<string, any> {
    const key = dump(result, { sortKeys: true });
    const value = simpleTypesMap.get(key);
    if (value) {
        result = value;
    } else {
        simpleTypesMap.set(key, result);
    }
    return result;
}

export function getType(
    context: SdkContext,
    type: CredentialType | CredentialTypeUnion | Type | SdkType,
    fromBody = false,
): Record<string, any> {
    if (type.kind === "Credential") {
        return emitCredential(type.scheme);
    }
    if (type.kind === "CredentialTypeUnion") {
        return emitCredentialUnion(type);
    }

    switch (type.kind) {
        case "model":
            return emitModel(context, type, fromBody);
        case "union":
            return emitUnion(context, type);
        case "enum":
            return emitEnum(type);
        case "constant":
            return emitConstant(type)!;
        case "array":
        case "dict":
            return emitArrayOrDict(context, type)!;
        case "utcDateTime":
        case "offsetDateTime":
        case "duration":
            return emitDurationOrDateType(type);
        case "enumvalue":
            return emitEnumMember(type, emitEnum(type.enumType));
        case "bytes":
        case "boolean":
        case "plainDate":
        case "plainTime":
        case "numeric":
        case "integer":
        case "safeint":
        case "int8":
        case "uint8":
        case "int16":
        case "uint16":
        case "int32":
        case "uint32":
        case "int64":
        case "uint64":
        case "float":
        case "float32":
        case "float64":
        case "decimal":
        case "decimal128":
        case "string":
        case "password":
        case "guid":
        case "url":
        case "uuid":
        case "eTag":
        case "armId":
        case "ipAddress":
        case "azureLocation":
            return emitBuiltInType(type);
        case "any":
            return KnownTypes.any;
        case "String":
        case "Number":
        case "Boolean":
        case "Intrinsic":
        case "Scalar":
        case "Enum":
        case "Union":
        case "ModelProperty":
        case "UnionVariant":
            return getType(context, getClientType(context, type));
        case "Model":
            return getType(context, getClientType(context, type), fromBody);
        default:
            throw Error(`Not supported ${type.kind}`);
    }
}

function emitCredential(auth: HttpAuth): Record<string, any> {
    let credential_type: Record<string, any> = {};
    if (auth.type === "oauth2") {
        credential_type = {
            type: "OAuth2",
            policy: {
                type: "BearerTokenCredentialPolicy",
                credentialScopes: [],
            },
        };
        for (const flow of auth.flows) {
            for (const scope of flow.scopes) {
                credential_type.policy.credentialScopes.push(scope.value);
            }
            credential_type.policy.credentialScopes.push();
        }
    } else if (auth.type === "apiKey") {
        credential_type = {
            type: "Key",
            policy: {
                type: "KeyCredentialPolicy",
                key: auth.name,
            },
        };
    } else if (auth.type === "http") {
        credential_type = {
            type: "Key",
            policy: {
                type: "KeyCredentialPolicy",
                key: "Authorization",
                scheme: auth.scheme[0].toUpperCase() + auth.scheme.slice(1),
            },
        };
    }
    return getSimpleTypeResult(credential_type);
}

function emitCredentialUnion(cred_types: CredentialTypeUnion): Record<string, any> {
    const result: Record<string, any> = {};
    // Export as CombinedType, which is already a Union Type in autorest codegen
    result.type = "combined";
    result.types = [];
    for (const cred_type of cred_types.types) {
        result.types.push(emitCredential(cred_type.scheme));
    }

    return getSimpleTypeResult(result);
}

function visibilityMapping(visibility?: Visibility[]): string[] | undefined {
    if (visibility === undefined) {
        return undefined;
    }
    const result = [];
    for (const v of visibility) {
        if (v === Visibility.Read) {
            result.push("read");
        } else if (v === Visibility.Create) {
            result.push("create");
        } else if (v === Visibility.Update) {
            result.push("update");
        } else if (v === Visibility.Delete) {
            result.push("delete");
        } else if (v === Visibility.Query) {
            result.push("query");
        }
    }
    return result;
}

function emitProperty(context: SdkContext, type: SdkBodyModelPropertyType): Record<string, any> {
    return {
        clientName: camelToSnakeCase(type.nameInClient),
        wireName: type.serializedName,
        type: getType(context, type.type),
        optional: type.optional,
        description: type.description,
        addedOn: type.apiVersions[0],
        visibility: visibilityMapping(type.visibility),
        isDiscriminator: type.discriminator,
        flatten: shouldFlattenProperty(context, type.__raw!),
        isMultipartFileInput: type.isMultipartFileInput,
    };
}

function emitModel(context: SdkContext, type: SdkModelType, fromBody: boolean): Record<string, any> {
    if (isEmptyModel(type)) {
        return KnownTypes.any;
    }
    if (typesMap.has(type)) {
        return typesMap.get(type)!;
    }
    const parents: Record<string, any>[] = [];
    const newValue = {
        type: type.kind,
        name: type.generatedName ?? type.name,
        description: type.description,
        parents: parents,
        discriminatorValue: type.discriminatorValue,
        discriminatedSubtypes: {} as Record<string, Record<string, any>>,
        properties: new Array<Record<string, any>>(),
        snakeCaseName: type.name ? camelToSnakeCase(type.name) : type.name,
        base: type.name === "" && fromBody ? "json" : getModelsMode(context) === "msrest" ? "msrest" : "dpg",
        internal: type.access === "internal",
    };

    typesMap.set(type, newValue);
    newValue.parents = type.baseModel ? [getType(context, type.baseModel)] : newValue.parents;
    for (const property of type.properties.values()) {
        if (property.kind === "property") {
            newValue.properties.push(emitProperty(context, property));
            // type for base discriminator returned by TCGC changes from constant to string while
            // autorest treat all discriminator as constant type, so we need to change to constant type here
            if (type.discriminatedSubtypes && property.discriminator) {
                newValue.properties[newValue.properties.length - 1].isPolymorphic = true;
                if (property.type.kind === "string") {
                    newValue.properties[newValue.properties.length - 1].type = getConstantType(null);
                }
            }
        }
    }
    if (type.discriminatedSubtypes) {
        for (const key in type.discriminatedSubtypes) {
            newValue.discriminatedSubtypes[key] = getType(context, type.discriminatedSubtypes[key]);
        }
    }
    return newValue;
}

function emitEnum(type: SdkEnumType): Record<string, any> {
    if (typesMap.has(type)) {
        return typesMap.get(type)!;
    }
    const values: Record<string, any>[] = [];
    const name = type.generatedName ?? type.name;
    const newValue = {
        name: name,
        snakeCaseName: camelToSnakeCase(name),
        description: type.description || `Type of ${name}`,
        internal: type.access === "internal",
        type: type.kind,
        valueType: emitBuiltInType(type.valueType),
        values,
        xmlMetadata: {},
    };
    for (const value of type.values) {
        newValue.values.push(emitEnumMember(value, newValue));
    }
    typesMap.set(type, newValue);
    return newValue;
}

function enumName(name: string): string {
    if (name.toUpperCase() === name) {
        return name;
    }
    return camelToSnakeCase(name).toUpperCase();
}

function emitEnumMember(type: SdkEnumValueType, enumType: Record<string, any>): Record<string, any> {
    return {
        name: enumName(type.name),
        value: type.value,
        description: type.description,
        enumType,
        type: type.kind,
        valueType: enumType["valueType"],
    };
}

function emitDurationOrDateType(type: SdkDurationType | SdkDatetimeType): Record<string, any> {
    return getSimpleTypeResult({
        ...emitBuiltInType(type),
        wireType: emitBuiltInType(type.wireType),
    });
}

function emitArrayOrDict(context: SdkContext, type: SdkArrayType | SdkDictionaryType): Record<string, any> {
    const kind = type.kind === "array" ? "list" : type.kind;
    return getSimpleTypeResult({
        type: kind,
        elementType: getType(context, type.valueType),
    });
}

function emitConstant(type: SdkConstantType) {
    return getSimpleTypeResult({
        type: type.kind,
        value: type.value,
        valueType: emitBuiltInType(type.valueType),
    });
}

const sdkScalarKindToPythonKind: Record<string, string> = {
    numeric: "integer",
    integer: "integer",
    safeint: "integer",
    int8: "integer",
    uint8: "integer",
    int16: "integer",
    uint16: "integer",
    int32: "integer",
    uint32: "integer",
    int64: "integer",
    uint64: "integer",
    float: "float",
    float32: "float",
    float64: "float",
    decimal: "decimal",
    decimal128: "decimal",
    string: "string",
    password: "string",
    guid: "string",
    url: "string",
    uuid: "string",
    etag: "string",
    armId: "string",
    ipAddress: "string",
    azureLocation: "string",
};

function emitBuiltInType(type: SdkBuiltInType | SdkDurationType | SdkDatetimeType): Record<string, any> {
    if (type.kind === "duration" && type.encode === "seconds") {
        return getSimpleTypeResult({
            type: sdkScalarKindToPythonKind[type.wireType.kind],
            encode: type.encode,
        });
    }
    if (type.encode === "unixTimestamp") {
        return getSimpleTypeResult({
            type: "unixtime",
            encode: type.encode,
        });
    }
    return getSimpleTypeResult({
        type: sdkScalarKindToPythonKind[type.kind] || type.kind, // TODO: switch to kind
        encode: type.encode,
    });
}

function emitUnion(context: SdkContext, type: SdkUnionType): Record<string, any> {
    return getSimpleTypeResult({
        name: type.name,
        snakeCaseName: camelToSnakeCase(type.name || ""),
        description: `Type of ${type.name}`,
        internal: true,
        type: "combined",
        types: type.values.map((x) => getType(context, x)),
        xmlMetadata: {},
    });
}

export function getConstantType(key: string | null): Record<string, any> {
    const cache = simpleTypesMap.get(key);
    if (cache) {
        return cache;
    }
    const type = {
        apiVersions: [],
        type: "constant",
        value: key,
        valueType: KnownTypes.string,
        xmlMetadata: {},
    };
    simpleTypesMap.set(key, type);
    return type;
}

export const KnownTypes = {
    string: { type: "string" },
    anyObject: { type: "any-object" },
    any: { type: "any" },
};
