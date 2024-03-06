from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union


@dataclass
class ExternalSubjectId:
    class Meta:
        name = "externalSubjectId"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    keys: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Keys:
    class Meta:
        name = "keys"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PreferredName:
    class Meta:
        name = "preferredName"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    text: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ReferredSemanticId:
    class Meta:
        name = "referredSemanticId"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    keys: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class SemanticIdListElement:
    class Meta:
        name = "semanticIdListElement"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    keys: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class DataSpecification:
    class Meta:
        name = "dataSpecification"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    keys: List[Keys] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class DataSpecificationContent:
    class Meta:
        name = "dataSpecificationContent"

    preferred_name: List[PreferredName] = field(
        default_factory=list,
        metadata={
            "name": "preferredName",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    model_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class First:
    class Meta:
        name = "first"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    referred_semantic_id: Optional[ReferredSemanticId] = field(
        default=None,
        metadata={
            "name": "referredSemanticId",
            "type": "Element",
        },
    )
    keys: List[Keys] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Second:
    class Meta:
        name = "second"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    keys: List[Keys] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class SemanticId:
    class Meta:
        name = "semanticId"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    keys: List[Keys] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class EmbeddedDataSpecifications:
    class Meta:
        name = "embeddedDataSpecifications"

    data_specification: Optional[DataSpecification] = field(
        default=None,
        metadata={
            "name": "dataSpecification",
            "type": "Element",
            "required": True,
        },
    )
    data_specification_content: Optional[DataSpecificationContent] = field(
        default=None,
        metadata={
            "name": "dataSpecificationContent",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SpecificAssetIds:
    class Meta:
        name = "specificAssetIds"

    semantic_id: Optional[SemanticId] = field(
        default=None,
        metadata={
            "name": "semanticId",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    external_subject_id: Optional[ExternalSubjectId] = field(
        default=None,
        metadata={
            "name": "externalSubjectId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"

    id_short: Optional[str] = field(
        default=None,
        metadata={
            "name": "idShort",
            "type": "Element",
        },
    )
    first: Optional[First] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    second: Optional[Second] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: List["Value"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    value_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueType",
            "type": "Element",
        },
    )
    model_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelType",
            "type": "Element",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    keys: List[Keys] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class AssetInformation:
    class Meta:
        name = "assetInformation"

    asset_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "assetKind",
            "type": "Element",
            "required": True,
        },
    )
    global_asset_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "globalAssetId",
            "type": "Element",
            "required": True,
        },
    )
    specific_asset_ids: List[SpecificAssetIds] = field(
        default_factory=list,
        metadata={
            "name": "specificAssetIds",
            "type": "Element",
        },
    )


@dataclass
class ConceptDescriptions:
    class Meta:
        name = "conceptDescriptions"

    id_short: Optional[str] = field(
        default=None,
        metadata={
            "name": "idShort",
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    embedded_data_specifications: List[EmbeddedDataSpecifications] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    model_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SubmodelElements:
    class Meta:
        name = "submodelElements"

    id_short: Optional[str] = field(
        default=None,
        metadata={
            "name": "idShort",
            "type": "Element",
            "required": True,
        },
    )
    semantic_id: Optional[SemanticId] = field(
        default=None,
        metadata={
            "name": "semanticId",
            "type": "Element",
        },
    )
    embedded_data_specifications: List[object] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
        },
    )
    value_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueType",
            "type": "Element",
        },
    )
    semantic_id_list_element: Optional[SemanticIdListElement] = field(
        default=None,
        metadata={
            "name": "semanticIdListElement",
            "type": "Element",
        },
    )
    type_value_list_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeValueListElement",
            "type": "Element",
        },
    )
    value: List[Union[int, Value, float, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Element",
        },
    )
    model_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Submodels:
    class Meta:
        name = "submodels"

    id_short: Optional[str] = field(
        default=None,
        metadata={
            "name": "idShort",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    submodel_elements: List[SubmodelElements] = field(
        default_factory=list,
        metadata={
            "name": "submodelElements",
            "type": "Element",
        },
    )
    model_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelType",
            "type": "Element",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    keys: List[Keys] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class AssetAdministrationShells:
    class Meta:
        name = "assetAdministrationShells"

    id_short: Optional[str] = field(
        default=None,
        metadata={
            "name": "idShort",
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    asset_information: Optional[AssetInformation] = field(
        default=None,
        metadata={
            "name": "assetInformation",
            "type": "Element",
            "required": True,
        },
    )
    submodels: List[Submodels] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    model_type: Optional[str] = field(
        default="AssetAdministrationShell",
        metadata={
            "name": "modelType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Generated:
    class Meta:
        name = "generated"

    asset_administration_shells: List[AssetAdministrationShells] = field(
        default_factory=list,
        metadata={
            "name": "assetAdministrationShells",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    submodels: List[Submodels] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    concept_descriptions: List[ConceptDescriptions] = field(
        default_factory=list,
        metadata={
            "name": "conceptDescriptions",
            "type": "Element",
            "min_occurs": 1,
        },
    )
