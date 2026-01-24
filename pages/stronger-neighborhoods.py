import streamlit as st
import pandas as pd
from shared.navigation import render_navigation
from shared.data_loader import initialize_data
from config import PAGE_CONFIG


# Render navigation
render_navigation()

# Get data from session state
df = initialize_data()

# Page-specific active CSS (only runs here, so only highlights Stronger Neighborhoods when on page)
# st.markdown("""
# <style>
#     /* Set background color for active page link */
#     [data-testid="stPageLink-NavLink"][href="stronger-neighborhoods"] {
#         background-color: #34A853 !important;
#     }
            
#     /* Set page link icon and text color */
#     [data-testid="stPageLink-NavLink"][href="stronger-neighborhoods"] span {
#         color: white !important;
#     }
# </style>
# """, unsafe_allow_html=True)
st.markdown("""
<style>
    /* Set background color for active page link */
    [data-testid="stPageLink-NavLink"][href="stronger-neighborhoods"] {
        background: #CEEAD6;
        border-left: 5px solid #34A853;
        padding-left: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)


# Main content
st.title("Stronger Neighborhoods")
st.markdown("### Parks, Libraries, and Housing & Community Development")