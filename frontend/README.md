# BakedBot AI Product Recommendation System

This project implements an AI-powered product recommendation system using FastAPI for the backend and React for the frontend. The system provides product recommendations, along with detailed information about products, their ingredients, and sales data.

## Features

- **Product Recommendations**: The system returns top product recommendations based on the available data.
- **Product Details**: Includes product name, type, effects, ingredients, and sales data (units sold, revenue).
- **WebSocket Support**: Real-time updates and communication between frontend and backend using WebSockets.

## Tech Stack

- **Backend**:
  - FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
  - WebSockets: Real-time communication between the client and the server.
  - Uvicorn: ASGI server for running FastAPI.

- **Frontend**:
  - React: A JavaScript library for building user interfaces.
  - Axios: Promise-based HTTP client for making API requests.

- **Data**:
  - JSON: For storing product, ingredient, and sales data.

## Installation

### Backend (FastAPI)

1. Clone the repository:

    ```bash
    git clone https://github.com/Saitejanagapuri55/bakebot-ai-recommendation-system.git
    cd bakebot-ai-recommendation-system
    ```

2. Set up a Python virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI backend:

    ```bash
    uvicorn main:app --reload
    ```

   The backend will be running on `http://localhost:8000`.

### Frontend (React)

1. Navigate to the frontend directory:

    ```bash
    cd frontend
    ```

2. Install the required dependencies:

    ```bash
    npm install
    ```

3. Start the React development server:

    ```bash
    npm start
    ```

   The frontend will be running on `http://localhost:3000`.

## Endpoints

### GET `/recommend`

- Fetches product recommendations with detailed information including:
  - Product name, type, effects
  - Ingredient details (name, properties, common effects)
  - Sales data (units sold, revenue)

Example response:
```json
{
  "recommended_product": {
    "name": "Relaxation Tea",
    "type": "beverage",
    "effects": ["relaxation", "stress relief"],
    "ingredients": [
      {
        "name": "Chamomile",
        "properties": "Mild, floral aroma; known for calming effects",
        "common_effects": ["relaxation", "improved sleep"]
      },
      {
        "name": "Lavender",
        "properties": "Aromatic herb known for relaxation properties",
        "common_effects": ["stress relief", "calming"]
      }
    ],
    "sales": {
      "units_sold": 120,
      "last_month_revenue": 1558.8
    }
  }
}

## Running the Application

## Start the FastAPI backend as described above.
## Start the React frontend as described above.
### Open your browser and navigate to http://localhost:3000 to interact with the application.