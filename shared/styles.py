import streamlit as st


def render_reusable_styles():
    """Render reusable styles across all pages"""
    st.markdown(
        """
        <style>
        /* Hide GitHub buttons on public site */
        [data-testid="stToolbarActionButton"] {
            display: none !important;
        }

        /* Remove padding from top of page */
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}

        /* Remove white background from header section */
        header { background: transparent !important; }

        .xl-metric {
            font-weight: 600;
            line-height: 1.0;
            font-size: 2.75rem !important;
            margin-bottom: 0;
            text-align: center; 
        }

        [data-testid="stCaptionContainer"] .small-label {
            font-size: smaller !important;
            margin-top: 0;
            line-height: 1.0;
        }

        .center {
            text-align: center;        
        }
        .left {
            text-align: left;        
        }
                
        .bold {
            font-weight: 600;        
        }

        .mb-0 {
            margin-bottom: 0 !important;        
        }
        .pt-0 {
            padding-top: 0 !important;        
        }
                
        .red {
            color: #EA4335;        
        }
        .blue {
            color: #4285F4;        
        }
        .green {
            color: #34A853;        
        }
        .yellow {
            color: #FBBC04;        
        }
        .grey {
            color: #9AA0A6;
        }

        .table-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            border-bottom: 1px solid #F1F3F4;
            padding: 0.2rem 0;
        }
        .table-row:last-of-type {
            border-bottom: none;
        }
        </style>
        """, unsafe_allow_html=True)