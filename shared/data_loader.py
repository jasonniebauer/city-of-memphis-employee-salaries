# ====================
# Efficient Data Loading with Caching
# ====================
import streamlit as st
import pandas as pd


def get_city_division_category(row):
    division = row['Division Name']
    public_safety = ['Police Services', 'Fire Services']
    public_works = ['Public Works', 'Solid Waste', 'City Engineering', 'General Services']
    stronger_neighborhoods = ['Memphis Parks', 'Library Services', 'Housing and Community Development']
    good_government = ['Executive', 'Finance and Administration', 'Human Resources', 'Information Technology', 'City Attorney', 'City Court Clerk', 'Judicial', 'Legislative']

    if division in public_safety:
        return 'Public Safety'
    elif division in public_works:
        return 'Public Works'
    elif division in stronger_neighborhoods:
        return 'Stronger Neighborhoods'
    elif division in good_government:
        return 'Good Government'
    else:
        return

@st.cache_data(ttl=3600, show_spinner="Loading salary data...")
def load_salary_data() -> pd.DataFrame:
    """Load salary data - cached globally"""
    df = pd.read_csv('data/City of Memphis Employee Salaries 2025.csv')
    
    # # Optimize data types for performance
    # df['department'] = df['department'].astype('category')
    # df['title'] = df['title'].astype('category')
    
    # Categorize city divisions/departments
    df['Division Category'] = df.apply(get_city_division_category, axis=1)

    # Rename Category column to Employment Type
    df = df.rename(columns={'Category': 'Employment Type'})
    # Replace 'Regular' with 'Full-time' in the Employment Type column
    df['Employment Type'] = df['Employment Type'].replace('Regular', 'Full-time')
    # Replace 'Part-Time' with 'Part-time' in the Employment Type column
    df['Employment Type'] = df['Employment Type'].replace('Part-Time', 'Part-time')
    
    return df

@st.cache_data(ttl=3600)
def get_department_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Compute department statistics - cached"""
    return df.groupby('department').agg({
        'salary': ['count', 'mean', 'median', 'min', 'max']
    }).round(0)

def initialize_data():
    """Initialize data in session state"""
    if 'salary_data' not in st.session_state:
        st.session_state.salary_data = load_salary_data()
    return st.session_state.salary_data

"""
import streamlit as st
import pandas as pd
from typing import Optional

# ✅ PERFORMANCE TIP #5: Use @st.cache_data for data loading
# - Use ttl for data that changes periodically
# - Use show_spinner for better UX
# - Use max_entries to limit cache size
@st.cache_data(ttl=3600, show_spinner="Loading data...")
def load_salary_data(filepath: str) -> pd.DataFrame:
    '''Load salary data with caching'''
    # For large files, consider using parquet instead of CSV
    if filepath.endswith('.parquet'):
        return pd.read_parquet(filepath)
    elif filepath.endswith('.csv'):
        # ✅ PERFORMANCE TIP #6: Use dtypes and usecols to reduce memory
        dtypes = {
            'employee_id': 'int32',
            'department': 'category',
            'salary': 'float32'
        }
        return pd.read_csv(filepath, dtype=dtypes)
    else:
        raise ValueError(f"Unsupported format: {filepath}")

# ✅ PERFORMANCE TIP #7: Cache expensive computations separately
@st.cache_data(ttl=3600)
def compute_department_stats(df: pd.DataFrame) -> pd.DataFrame:
    '''Compute aggregated statistics'''
    return df.groupby('department').agg({
        'salary': ['mean', 'median', 'count'],
        'employee_id': 'count'
    }).reset_index()

# ✅ PERFORMANCE TIP #8: Use @st.cache_resource for connections/models
@st.cache_resource
def get_database_connection():
    '''Maintain single DB connection across reruns'''
    import sqlalchemy
    return sqlalchemy.create_engine("postgresql://...")

# ✅ PERFORMANCE TIP #9: Lazy load heavy dependencies
def load_ml_model():
    '''Only import when needed'''
    if 'model' not in st.session_state:
        import joblib
        st.session_state.model = joblib.load('model.pkl')
    return st.session_state.model
"""