import streamlit as st
st.write("helllloooo")
n=st.text_input("whats your name")
st.divider()
st.title(n)

if 'counter' not in st.session_state:
    st.session_state.counter=0

if st.button("increment by 1"):
    st.session_state.counter+=1
if st.button("reset"):
    st.session_state.counter=0
st.write(st.session_state.counter)

