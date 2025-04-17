import streamlit as st

st.title("My Projects")

import streamlit as st

# Define navigation options
navigation = ["Home", "About", "Portfolio", "Contact"]

# Create a navigation menu
choice = st.sidebar.radio("Navigation Menu", navigation)

# Display content based on the selected menu
if choice == "Home":
    st.title("Welcome to the Home Page")
elif choice == "About":
    st.title("About Us")
    st.write("This is the About page.")
elif choice == "Portfolio":
    st.title("Our Portfolio")
    st.write("Here is our portfolio.")
elif choice == "Contact":
    st.title("Contact Us")
    st.write("Get in touch with us.")



# Embed HTML code
html_code = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">

<div class="container text-center mt-5">
    <div class="row g-4">
        <div class="col-md-4">
            <div class="card shadow-sm">
                <div class="card-body">
                    <a href="contact">link</a>
                    <h5 class="card-title">Project 1</h5>
                    <p class="card-text">Description of Project 1</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">Project 2</h5>
                    <p class="card-text">Description of Project 2</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">Project 3</h5>
                    <p class="card-text">Description of Project 3</p>
                </div>
            </div>
        </div>
    </div>
</div>
"""
st.markdown(html_code, unsafe_allow_html=True)
