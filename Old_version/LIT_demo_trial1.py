import streamlit as st
import numpy as np

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))
    
uploaded_file = st.file_uploader("Choose a file")    
    
