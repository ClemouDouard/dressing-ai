import streamlit as st
import bcrypt

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db import add_user, get_user

def login_page():
    st.title("Dressing AI : Connexion")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_id = None
    
    menu = st.radio("Choisir une action", ["Se connecter", "S'inscrire"])

    if menu=="Se connecter":
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        if st.button("Se connecter"):
            user = get_user(username)
            if user and bcrypt.checkpw(password.encore(), user[2].encode()):
                st.success("Connexion réussie")
                st.session_state.logged_in = True
                st.session_state.user_id = user[0]
                st.rerun()
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect")
    
    elif menu=="S'inscrire":
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        if st.button("S'inscrire"):
            if get_user(username):
                st.warning("Ce nom d'utilisateur est déjà pris")
            else:
                password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                add_user(username, password_hash)
                st.success("Inscription réussie")

    if st.session_state.logged_in:
        st.info(f"Connecté en tant que {username}")
        if st.button("Se déconnecter"):
            st.session_state.logged_in = False
            st.session_state.user_id = None
            st.rerun()