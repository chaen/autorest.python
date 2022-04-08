# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TYPE_CHECKING
from .base_schema import BaseSchema
from .imports import FileImport, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


class DictionarySchema(BaseSchema):
    """Schema for dictionaries that will be serialized.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    :param element_type: The type of the value for the dictionary
    :type element_type: ~autorest.models.BaseSchema
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        element_type: "BaseSchema",
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.element_type = element_type

    @property
    def serialization_type(self) -> str:
        """Returns the serialization value for msrest.

        :return: The serialization value for msrest
        :rtype: str
        """
        return f"{{{self.element_type.serialization_type}}}"

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        """The python type used for type annotation

        :return: The type annotation for this schema
        :rtype: str
        """
        return f"Dict[str, {self.element_type.type_annotation(is_operation_file=is_operation_file)}]"

    @property
    def docstring_text(self) -> str:
        return f"dict mapping str to {self.element_type.docstring_text}"

    @property
    def docstring_type(self) -> str:
        """The python type used for RST syntax input and type annotation.

        :param str namespace: Optional. The namespace for the models.
        """
        return f"dict[str, {self.element_type.docstring_type}]"

    def xml_serialization_ctxt(self) -> Optional[str]:
        raise NotImplementedError(
            "Dictionary schema does not support XML serialization."
        )

    def get_json_template_representation(self, **kwargs: Any) -> Any:
        return {
            f'"{"str"}"': self.element_type.get_json_template_representation(**kwargs)
        }

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "DictionarySchema":
        """Constructs a DictionarySchema from yaml data.

        :param yaml_data: the yaml data from which we will construct this schema
        :type yaml_data: dict[str, Any]

        :return: A created DictionarySchema
        :rtype: ~autorest.models.DictionarySchema
        """
        element_schema = yaml_data["elementType"]

        from . import build_schema  # pylint: disable=import-outside-toplevel

        element_type = build_schema(yaml_data=element_schema, code_model=code_model)

        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            element_type=element_type,
        )

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "typing", "Dict", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.merge(self.element_type.imports())
        return file_import

    def model_file_imports(self) -> FileImport:
        file_import = self.imports()
        file_import.merge(self.element_type.model_file_imports())
        return file_import
