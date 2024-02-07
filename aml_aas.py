import streamlit as st
import json
from aas_utils import convert_to_aas

if "aas_payload" not in st.session_state:
    st.session_state["aas_payload"]  = None

st.header("AAS Generator")
raw_data = st.file_uploader("Upload AML file", type=["json"])

if raw_data is not None:
    aas_payload = json.load(raw_data)
    st.session_state["aas_payload"] = aas_payload

    convert_to_aas_btn = st.button("Convert to AAS", type="primary", use_container_width=True)

    if convert_to_aas_btn:
        aas_json = convert_to_aas(st.session_state["aas_payload"])
        st.write(aas_json)