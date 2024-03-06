import streamlit as st
import networkx as nx

def check_path(graph:nx.Graph):
    node1_col, node2_col = st.columns(2)
    with node1_col:
        node1_select = st.selectbox("Select first node", options=graph.nodes, key="node1_select")
    with node2_col:
        node2_select = st.selectbox("Select second node", options=graph.nodes, key="node2_select")
    if node1_select and node2_select:
        if nx.has_path(graph, node1_select, node2_select):
            st.success(f"There is a path between node {node1_select} and node {node2_select}.")
        else:
            st.error(f"There is no path between node {node1_select} and node {node2_select}.")


def shortest_path(graph: nx.Graph):
    import graphviz
    node1_col, node2_col = st.columns(2)
    with node1_col:
        node1_select = st.selectbox("Select first node",
        options=graph.nodes,
        key="node1_select")
    with node2_col:
        node2_select = st.selectbox("Select second node",
                                    options=graph.nodes,
                                    key="node2_select")
    try:
        shortest_path_for_graph = nx.shortest_path(graph,node1_select, node2_select)
        st.success(f"The shortest path between {node1_select} "
                   f"and {node2_select} is {shortest_path_for_graph}")
        st.write(shortest_path_for_graph)
        subgraph=graph.subgraph(shortest_path_for_graph)
        graphviz_graph=graphviz.Digraph()
        st.write(subgraph.edges)
        for node in subgraph.nodes:
            graphviz_graph.node(str(node))
            # Add edges to the Graphviz object

        for edge in subgraph.edges:
            graphviz_graph.edge(str(edge[0]), str(edge[1]))
        st.graphviz_chart(graphviz_graph)
    except nx.NetworkXNoPath:
        st.error(f"There is no path between {node1_select} and {node2_select}")

