import streamlit as st

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.login import login_page

def main():
    st.set_page_config(page_title="Dressing AI", page_icon="👚", layout="centered")
    
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        login_page()
    else:
        st.title("👕 Bienvenue dans ta garde-robe IA")
        with st.sidebar:
            if st.button("Ajouter une image"):
                "bien joué"

if __name__ == "__main__":
    main()