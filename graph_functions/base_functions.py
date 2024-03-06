import networkx as nx
import streamlit as st


def output_nodes_and_edges(graph:nx.Graph):
    st.write(graph.nodes)
    st.write(graph.edges)


def count_nodes(graph:nx.Graph):
    num_nodes = len(graph.nodes)
    num_nodes = graph.number_of_nodes()
    st.info(f"The graph has {num_nodes} nodes")


def find_density(graph:nx.Graph):
    density=nx.density(graph)
    st.info(f"The density of graph is {density}")



def is_empty(graph:nx.Graph):
    is_empty=nx.is_empty(graph)
    if is_empty:
        st.info("The graph is empty.")
    else:
        st.info("The graph is not empty.")


def is_directed(graph:nx.Graph):
    is_directed=nx.is_directed(graph)
    if is_directed:
        st.info("The graph is directed.")
    else:
        st.info("The graph is not directed")
        