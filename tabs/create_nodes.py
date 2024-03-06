import streamlit as st
import uuid

def create_nodes():
    name_node = st.text_input("Type in the name of the node")
    type_node = st.selectbox("Specify the type of the node", ["Node", "Person"])
    age_node = int(st.number_input("Input the age of the node", value=0))
    save_node_button = st.button("Store Node", use_container_width=True, type="primary")
    if save_node_button:
        save_node(name_node, age_node, type_node)
    st.write(st.session_state["node_list"])


def save_node(name, age, type_n):
    node_dict = {
        "name": name,
        "age": age,
        "id": str(uuid.uuid4()),
        "type": type_n
    }
    st.session_state["node_list"].append(node_dict)
    st.session_state["graph_dict"]["nodes"] = st.session_state["node_list"]