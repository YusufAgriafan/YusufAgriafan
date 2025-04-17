import streamlit as st

st.set_page_config(page_title="My Portfolio | Yusuf Agung Rizky Afandi", page_icon="💻", layout="wide")

st.set_home_page = st.Page(
    page = "views/home.py",
    title="Home",
    icon="👤",
    default=True,
)

st.set_me_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="🐐",
)

st.set_projects_page = st.Page(
    page="views/projects.py",
    title="My Projects",
    icon="📽️",
)

st.set_contact_page = st.Page(
    page = "views/contact.py",
    title="Contact",
    icon="📞",
)

pg = st.navigation(
    pages=[
        st.set_home_page,
        st.set_me_page,
        st.set_projects_page,
        st.set_contact_page,
    ],
)

with st.sidebar:
    st.title("My Portfolio")
    st.markdown("👋 Welcome to my portfolio! Explore my projects, learn about me, and feel free to get in touch.")
    st.markdown("---")

pg.run()