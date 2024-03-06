
import streamlit as st
import json
from tabs.tab_utils import graph_dict_to_ppr_dict

def export_graph():
    graph_string = json.dumps(st.session_state["graph_dict"])
    ppr_dict = graph_dict_to_ppr_dict(st.session_state["graph_dict"])
    ppr_json = json.dumps(ppr_dict)

    st.download_button(
        "Export Graph to JSON",
        file_name="graph.json",
        mime="application/json",
        data=graph_string,
        use_container_width=True,
        type="primary"
    )

    st.download_button(
        "Export Graph to JSON",
        file_name="graph.json",
        mime="application/json",
        data=ppr_json,
        use_container_width=True,
        type="secondary"
    )