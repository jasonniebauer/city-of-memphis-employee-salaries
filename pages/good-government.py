import streamlit as st
import pandas as pd
from shared.navigation import render_navigation
from shared.data_loader import initialize_data
from config import PAGE_CONFIG


# Render navigation
render_navigation()

# Get data from session state
df = initialize_data()

# Page-specific active CSS (only runs here, so only highlights Good Government when on page)
# st.markdown("""
# <style>
#     /* Set background color for active page link */
#     [data-testid="stPageLink-NavLink"][href="good-government"] {
#         background-color: #FBBC04 !important;
#     }
# </style>
# """, unsafe_allow_html=True)

st.markdown("""
<style>
    /* Set background color for active page link */
    [data-testid="stPageLink-NavLink"][href="good-government"] {
        background: #FEEFC3;
        border-left: 5px solid #FBBC04;
        padding-left: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)


# Main content
st.title("Good Government")
st.markdown("### Administration, Finance, HR, IT, Legal, and Governance")