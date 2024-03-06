from model import Generated, AssetAdministrationShells, Submodels, Keys, SemanticId, SubmodelElements
import json
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer, JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


def create_semantic_id(semantic_id_str):
    # This function will parse the string and create a SemanticId instance
    keys = [Keys(type_value="IRDI", value=semantic_id_str)]  # Simplified example
    return SemanticId(keys=keys)


def add_properties_to_submodels(submodels, properties):
    for prop in properties:
        element = SubmodelElements(
            id_short=prop["name"],
            value=[prop["value"]],
            value_type=prop["datatype"],
            semantic_id=create_semantic_id(prop["semanticId"]) if prop.get("semanticId") else None,
            # Add other necessary attributes here
        )
        submodels.submodel_elements.append(element)


def convert_to_aas(aas_payload):
    # Create outer AAS shell object (Generated)
    aas_container = Generated()
    # Reference on the inside AAS
    aas_list = aas_container.asset_administration_shells
    # Create submodel object for the submodel container
    aas_submodels = aas_container.submodels

    # Create AAS objects from payload
    for asset in aas_payload:  # Accesses the dict objects of the list
        aas = AssetAdministrationShells()
        aas.id_short = asset["name"]
        aas.id = asset["id"]
        # TODO aas.asset_information -> THink what we want to display here
        aas_list.append(aas)
        # Create submodel reference to the asset internal submodel list
        submodel_list = aas.submodels

        # Create Submodels for each AAS
        for submodel in asset["submodels"]:
            container_sm = Submodels()
            container_sm.id_short = submodel["name"]
            container_sm.id = submodel["id"]

            # Populate submodel elements with properties
            add_properties_to_submodels(container_sm, submodel["properties"])

            # Register submodels
            aas_submodels.append(container_sm)

            asset_sm = Submodels()
            asset_sm.type_value = "ModelReference"
            # Create the key element and append
            key = Keys()
            key.type_value = "Submodel"
            key.value = submodel["id"]
            asset_sm.keys.append(key)

            submodel_list.append(asset_sm)

    aas_json = serialize_aas(aas_container)
    cleaned_aas_json = clean_dict(aas_json)
    return aas_json


def serialize_aas(aas_container):
    config = SerializerConfig(pretty_print=False, ignore_default_attributes=True)
    json_serializer = JsonSerializer(context=XmlContext(), config=config)
    aas_json_string = json_serializer.render(aas_container)
    aas_dict = json.loads(aas_json_string)
    return aas_dict


# Utility function to optimize JSON dictionary
def clean_dict(aas_dict: dict):
    for key, value in aas_dict.copy().items():
        if value is None or value == "" or value == "Null" or value == "None":
            del aas_dict[key]
        elif isinstance(value, list):
            if value:
                new_value_list = []
                for entry in value:
                    if isinstance(entry, str):
                        pass
                    elif isinstance(entry, dict):
                        new_value_list.append(clean_dict(entry))
            else:
                del aas_dict[key]
        elif isinstance(value, dict):
            value = clean_dict(value)
    return aas_dict
