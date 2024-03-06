import streamlit as st
import uuid
from model import metamodel_dict

def create_edges():
    # Model logic
    node_list = st.session_state["node_list"]
    node_name_list = []
    for node in node_list:
        node_name_list.append(node["name"])
    # UI Rendering
    node1_col, relation_col, node2_col = st.columns(3)
    with node1_col:
        node1_select = st.selectbox(
            "Select the first node",
            options=node_name_list,
            key="node1_select"
        )
    with relation_col:
        # Logic
        relation_list = metamodel_dict["edges"]
        # UI Rendering
        relation_name = st.selectbox(
            "Specify the relation",
            options=relation_list)
    with node2_col:
        node2_select = st.selectbox(
            "Select the second node",
            options=node_name_list,
            key="node2_select"
        )
    store_edge_button = st.button("Store Relation",
                                  use_container_width=True,
                                  type="primary")

    if store_edge_button:
        save_edge(node1_select, relation_name, node2_select)

    st.write(f"{node1_select} is {relation_name} {node2_select}")  # Most pythonic version
    st.write(st.session_state["edge_list"])


def save_edge(node1, relation, node2):
    edge_dict = {
        "source": node1,
        "target": node2,
        "type": relation,
        "id": str(uuid.uuid4()),
    }
    st.session_state["edge_list"].append(edge_dict)
    st.session_state["graph_dict"]["edges"]=st.session_state["edge_list"]
