import streamlit as st

if not st.user.is_logged_in:
    if st.button('Log in with Microsoft'):
        st.login('microsoft')
    st.stop()

st.write(f"Hello, {st.user.name}!")