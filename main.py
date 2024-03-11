import streamlit as st
import json
from streamlit_option_menu import option_menu
from tabs import (upload_graph,
                  create_nodes,
                  create_edges,
                  visualize_graph,
                  analyze_graph, 
                  export_graph)

def open_tab(tab_name):
    if selected_tab in tab_dict:
        return tab_dict[tab_name]()
    else:
        st.error("The selected tab is not available")

if __name__ == '__main__':

    if "node_list" not in st.session_state:
        st.session_state["node_list"] = []
    if "edge_list" not in st.session_state:
        st.session_state["edge_list"] = []
    if "graph_dict" not in st.session_state:
        st.session_state["graph_dict"] = {}

    st.set_page_config(layout="wide", initial_sidebar_state="expanded")
    st.title("PPR-AAS Graph Analyzer")

    tab_dict = {
        "Import Graph": upload_graph,
        "Create Nodes": create_nodes,
        "Create Relations": create_edges,
        "Visualize the Graph": visualize_graph,
        "Analyze the Graph": analyze_graph,
        "Export the Graph": export_graph
    }


    with st.sidebar:
        selected_tab = option_menu("Main Menu",
                                   list(tab_dict.keys()),
                                   icons=['house', 'gear', "arrow-clockwise"],
                                   menu_icon="cast",
                                   default_index=0,
                                   orientation="vertical"
                                   )

    open_tab(selected_tab)





