
import streamlit as st
import networkx as nx

def specific_node(graph:nx.Graph):
    node_select = st.selectbox("Select node", options=graph.nodes, key="node_select")
    node=graph.nodes[node_select]
    st.info(node)
