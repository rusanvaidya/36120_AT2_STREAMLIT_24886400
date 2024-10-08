# Streamlit Sales Forecasting App

This project is a **Streamlit-based sales forecasting app** with a backend powered by machine learning models. The app allows users to interact with the model and get sales forecasts for different dates and stores.

This application allows users to forecast sales for different stores and items, based on historical sales data. Users can interact with the frontend via a **Streamlit app**, which communicates with a backend to fetch forecast results.

The backend is built with **FastAPI** and uses a machine learning model trained with historical data. The frontend is built using **Streamlit** to provide a user-friendly interface.

<a href="https://three6120-at2-streamlit-24886400.onrender.com/">Go to web application</a>

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: FastAPI (Python-based API)
- **Package Management**: Poetry
- **Containerization**: Docker
- **Predictive Model**: SGD
- **Forecasting Model**: SARIMAX

---

1. **Go to the backend directory and run before running following steps**

2. **Poetry Installation**
   ```bash
   poetry install

3. **Ensure Docker is installed** 
on your machine. If not, follow [Docker installation instructions](https://docs.docker.com/get-docker/).

4. **Build the Docker image for the backend**:
   ```bash
   docker build -t sales-frontend .

5. **Run Docker Containers**
    ```bash
    docker run -d -p 8501:8501 sales-frontend



