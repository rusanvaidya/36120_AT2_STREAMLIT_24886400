import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import plotly.express as px
import json

# Base URL of the FastAPI backend
BASE_URL = "https://three6120-at2-fastapi-24886400-1.onrender.com/"

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Function to change the page
def change_page(page_name):
    st.session_state.page = page_name

# Function to plot forecast data
def plot_forecast(forecast_data):
    df = pd.DataFrame(forecast_data)
    fig = px.line(df, x='Date', y='Forecasted Sales Volume', title="7-Day Sales Forecast")
    return fig

# Home Page definition
def home_page():
    st.title("📊 Welcome to the Sales Prediction App")
    
    response = requests.get(f"{BASE_URL}")
    if response.status_code == 200:
        content = response.json()
        description = content.get('Description', "Description not available")
        githubLink = content.get('github_repo_link', "#")
        st.markdown(f"""{description}""")
        st.write(f"Github Link: {githubLink}")
    
    st.markdown("""
        This interactive app allows you to:
        - **Predict sales** for specific stores and items.
        - **Forecast national sales** for the upcoming week.
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔮 Predict Sales"):
            change_page('predict_sales')
    with col2:
        if st.button("📈 Forecast National Sales"):
            change_page('forecast_sales')

# Predict Sales Page definition
def predict_sales_page():
    st.title("🔮 Predict Sales for Store and Item")
    
    # Input form for sales prediction
    with st.form("predict_sales_form"):
        item_id = st.text_input("Item ID", "HOBBIES_1_001")
        store_id = st.text_input("Store ID", "WI_1")
        date = st.date_input("Date", datetime.today())
        submit_button = st.form_submit_button(label="Predict")

    # Make prediction if form is submitted
    if submit_button:
        date_str = date.strftime('%Y-%m-%d')
        response = requests.get(f"{BASE_URL}/sales/stores/items/", params={"item_id": item_id, "store_id": store_id, "date": date_str})
        
        if response.status_code == 200:
            predicted_sales = response.json()
            st.success(f"Predicted Sales Volume: {predicted_sales.get('prediction', 'N/A')}")
        else:
            st.error("Error fetching prediction")

    st.button("🏠 Back to Home", on_click=change_page, args=("home",))

# Forecast National Sales Page definition
def forecast_sales_page():
    st.title("📈 Forecast National Sales for the Next 7 Days")

    # Input form for forecast
    with st.form("forecast_sales_form"):
        forecast_date = st.date_input("Forecast Start Date", datetime.today())
        submit_forecast = st.form_submit_button(label="Forecast")

    # Display forecast data
    if submit_forecast:
        forecast_date_str = forecast_date.strftime('%Y-%m-%d')
        forecast_response = requests.get(f"{BASE_URL}/sales/national/", params={"date": forecast_date_str})
        
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            st.write("Forecasted Sales for the Next 7 Days:")
            
            # Convert data to DataFrame
            forecast_df = pd.DataFrame(list(forecast_data.items()), columns=['Date', 'Forecasted Sales Volume'])
            st.dataframe(forecast_df)
            
            # Plot forecast data
            fig = plot_forecast(forecast_df)
            st.plotly_chart(fig)
        else:
            st.error("Error fetching forecast")

    st.button("🏠 Back to Home", on_click=change_page, args=("home",))

# Sidebar for navigation
if st.session_state.page != 'home':
    with st.sidebar:
        st.title("Navigation")
        st.button("🏠 Home", on_click=change_page, args=("home",))
        st.button("🔮 Predict Sales", on_click=change_page, args=("predict_sales",))
        st.button("📈 Forecast National Sales", on_click=change_page, args=("forecast_sales",))

# Display the page based on the session state
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'predict_sales':
    predict_sales_page()
elif st.session_state.page == 'forecast_sales':
    forecast_sales_page()
