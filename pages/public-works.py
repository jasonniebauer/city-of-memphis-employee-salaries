import streamlit as st
import pandas as pd
from shared.navigation import render_navigation
from shared.data_loader import initialize_data
from config import PAGE_CONFIG


# Render navigation
render_navigation()

# Get data from session state
df = initialize_data()

# Page-specific active CSS (only runs here, so only highlights Public Works when on page)
# st.markdown("""
# <style>
#     /* Set background color for active page link */
#     [data-testid="stPageLink-NavLink"][href="public-works"] {
#         background-color: #4285F4 !important;
#     }
            
#     /* Set page link icon and text color */
#     [data-testid="stPageLink-NavLink"][href="public-works"] span {
#         color: white !important;
#     }
# </style>
# """, unsafe_allow_html=True)
st.markdown("""
<style>
    /* Set background color for active page link */
    [data-testid="stPageLink-NavLink"][href="public-works"] {
        background: #D2E3FC;
        border-left: 5px solid #4285F4;
        padding-left: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)


# Main content
st.title("Public Works")
st.markdown("### Public Works, Solid Waste Management, City Engineering, and General Services")