import networkx as nx
from graph_functions import output_nodes_and_edges, count_nodes, find_density, check_path, is_empty, is_directed, specific_node, shortest_path
import streamlit as st

def analyze_graph():
    G = nx.DiGraph()
    graph_dict = st.session_state["graph_dict"]
    node_list = graph_dict["nodes"]
    edge_list = graph_dict["edges"]
    node_tuple_list = []
    edge_tuple_list = []

    for node in node_list:
        node_tuple = (node["name"], node)
        node_tuple_list.append(node_tuple)

    for edge in edge_list:
        edge_tuple = (edge["source"], edge["target"], edge)
        edge_tuple_list.append(edge_tuple)

    G.add_nodes_from(node_tuple_list)
    G.add_edges_from(edge_tuple_list)

    functions = {
        "Output nodes and edges": output_nodes_and_edges,
        "Count Nodes": count_nodes,
        "Density of Graph": find_density,
        "Check Path": check_path,
        "Check if Graph is Empty": is_empty,
        "Is Graph Directed": is_directed,
        "Specific Node": specific_node,
        "Shortest Path": shortest_path
    }
    select_function = st.selectbox(label="Select function",
                                   options=list(functions.keys()))
    if select_function in functions:
        functions[select_function](graph=G)
    else:   
        st.write("Function not found")