from typing import List
import json
import streamlit as st 
from streamlit_option_menu import option_menu
from tabs.tab_utils import update_session_state, ppr_dict_to_graph_dict


def upload_graph():
    uploaded_graph = st.file_uploader("Upload an existing graph", type="json")
    if uploaded_graph is not None:
        uploaded_graph_dict = json.load(uploaded_graph)
        uploaded_nodes = uploaded_graph_dict["nodes"]
        uploaded_edges = uploaded_graph_dict["edges"]
        if "sourceHandle" in uploaded_graph_dict["edges"][0]:
            uploaded_graph_dict = ppr_dict_to_graph_dict(uploaded_graph_dict)
            uploaded_nodes = uploaded_graph_dict["nodes"]
            uploaded_edges = uploaded_graph_dict["edges"]
        st.json(uploaded_graph_dict, expanded=False)
    else:
        st.info("Please upload a graph if available")
        uploaded_nodes = []
        uploaded_edges = []

    update_graph_button = st.button(
        "Update Graph via the Upload",
        use_container_width=True,
        type="primary"
    )
    if update_graph_button and uploaded_graph is not None:
        update_session_state(uploaded_nodes, uploaded_edges)
