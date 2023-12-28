import streamlit as st

new_register, reference = st.columns(spec=2, gap="large")

with new_register:
    with st.container(border=True):
        model_name = st.text_input(
            label="Model Name",
            placeholder="airoboros-l2-13b-3.1.1",
            )
        
        repo_id = st.text_input(
            label="Repository ID",
            placeholder="TheBloke/Airoboros-L2-13B-3.1.1-GGUF",
            )
        
        original_repo_id = st.text_input(
            label="Original Repository ID",
            placeholder="jondurbin/airoboros-l2-13b-3.1.1",
            )
        
        quantize = st.multiselect(
            'Select downloaded quantize',
            ['Green', 'Yellow', 'Red', 'Blue']
            )



with reference:
    with st.container(border=True):
        st.text_input(
            label="Model Name"
            )
