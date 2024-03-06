
import graphviz
import streamlit as st

def visualize_graph():
    def set_color(node_type):
        color = "Grey"
        #Refactor the code to use a dictionary
        color_dict = {
            "Person": "Blue",
            "Node": "Green",
            "Resource": "Violet",
            "Sensor": "Red"
        }
        if node_type in color_dict:
            color = color_dict[node_type]
        return color

    # Create a graphlib graph object
    with st.expander("Graphviz Visualisation"):
        graph = graphviz.Digraph()
        graph_dict = st.session_state["graph_dict"]
        node_list = graph_dict["nodes"]
        edge_list = graph_dict["edges"]
        for node in node_list:
            node_name = node["name"]
            graph.node(node_name, color=set_color(node["type"]))
        for edge in edge_list:
            source = edge["source"]
            target = edge["target"]
            label = edge["type"]
            graph.edge(source, target, label)
        st.graphviz_chart(graph)