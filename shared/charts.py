# Reusable chart functions
# ====================
# utils/charts.py - Reusable Chart Components
# ====================
"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ✅ PERFORMANCE TIP #17: Create chart templates to avoid repetition
CHART_TEMPLATE = {
    'layout': {
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'font': {'size': 12},
        'margin': {'l': 40, 'r': 40, 't': 40, 'b': 40}
    }
}

def create_bar_chart(df: pd.DataFrame, x: str, y: str, 
                     title: str = None) -> go.Figure:
    '''Create optimized bar chart'''
    
    # ✅ PERFORMANCE TIP #18: Aggregate before plotting
    if len(df) > 1000:
        plot_df = df.groupby(x)[y].mean().reset_index()
    else:
        plot_df = df
    
    fig = px.bar(plot_df, x=x, y=y, title=title)
    fig.update_layout(**CHART_TEMPLATE['layout'])
    
    return fig

def create_line_chart(df: pd.DataFrame, x: str, y: str,
                     color: str = None) -> go.Figure:
    '''Create optimized line chart'''
    
    # ✅ PERFORMANCE TIP #19: Sample large datasets
    if len(df) > 5000:
        plot_df = df.sample(n=5000, random_state=42)
    else:
        plot_df = df
    
    fig = px.line(plot_df, x=x, y=y, color=color)
    fig.update_layout(**CHART_TEMPLATE['layout'])
    
    return fig
"""
