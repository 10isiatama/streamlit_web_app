import streamlit as st

code = """
print("Yes" if ok else "No")
"""

st.code(code, language="python") 