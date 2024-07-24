import streamlit as st

st.set_page_config(
    page_title="My Custom Streamlit App",
    page_icon="🎈",
    layout="centered",
)

if 'num_list' not in st.session_state:
    st.session_state.num_list = []

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")

with col2:
    input1 = st.text_input('your graph name')
    n = st.number_input('your graph', step=0.1)
    btn = st.button('add')

    if btn:
        st.session_state.num_list.append(n)

    st.write(f'Your list: {len(st.session_state.num_list)}')

    for number in st.session_state.num_list:
        st.write(number)

    btn1 = st.button('make')
    if btn1:
        st.write('##', input1)
        st.line_chart(st.session_state.num_list)

with col3:
    st.write("")
