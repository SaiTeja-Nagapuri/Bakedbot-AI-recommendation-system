from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import json
import asyncio

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Product dataset
products = [
    {
        "id": 1,
        "name": "Relaxation Tea",
        "type": "beverage",
        "description": "A soothing herbal tea blend designed for relaxation and stress relief.",
        "effects": ["relaxation", "stress relief"],
        "ingredients": ["Chamomile", "Lavender"],
        "price": 12.99,
        "sales_data": {
            "units_sold": 120,
            "last_month_revenue": 1558.8
        }
    }
]

# Ingredient information
ingredients = [
    {
        "name": "Chamomile",
        "properties": "Mild, floral aroma; known for calming effects",
        "common_effects": ["relaxation", "improved sleep"]
    },
    {
        "name": "Lavender",
        "properties": "Sweet, floral scent; often used for calming and stress relief",
        "common_effects": ["relaxation", "stress relief"]
    }
]

# Sales data
sales_data = [
    {
        "product_id": 1,
        "daily_sales": [
            {
                "date": "2025-01-01",
                "units_sold": 5
            },
            {
                "date": "2025-01-02",
                "units_sold": 7
            }
        ]
    }
]

# Example helper functions to retrieve product, ingredient, and sales data
def get_product_info(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return product

def get_ingredient_info(ingredient_name):
    ingredient = next((i for i in ingredients if i["name"] == ingredient_name), None)
    return ingredient

def get_sales_data(product_id):
    sales = next((s for s in sales_data if s["product_id"] == product_id), None)
    return sales

@app.get("/recommend")
def recommend():
    if not products:
        raise HTTPException(status_code=404, detail="No products available")
    
    # Get the first product for demonstration (you can customize the recommendation logic here)
    recommended_product = products[0]

    # Add ingredient details to the recommended product
    ingredients_info = []
    for ingredient in recommended_product["ingredients"]:
        ingredient_info = get_ingredient_info(ingredient)
        if ingredient_info:
            ingredients_info.append({
                "name": ingredient_info["name"],
                "properties": ingredient_info["properties"],
                "common_effects": ingredient_info["common_effects"]
            })
    
    # Add sales data to the recommended product
    sales_info = get_sales_data(recommended_product["id"])
    sales_details = {
        "units_sold": sales_info["daily_sales"][0]["units_sold"] if sales_info else 0,
        "last_month_revenue": recommended_product["sales_data"]["last_month_revenue"]
    } if sales_info else {}

    # Combine all information for the response
    return {
        "recommended_product": {
            "name": recommended_product["name"],
            "type": recommended_product["type"],
            "effects": recommended_product["effects"],
            "ingredients": ingredients_info,
            "sales": sales_details
        }
    }

@app.get("/products")
def get_products():
    return {"products": products}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Received: {data}")
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        # Close the websocket properly after the connection ends
        await websocket.close()

# Graceful shutdown handling
@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down... Cleaning up resources.")
    await asyncio.sleep(1)  # Simulate cleanup time if needed

# Example usage inside the app
@app.get("/product/{product_id}")
def get_product_details(product_id: int):
    product_info = get_product_info(product_id)
    if not product_info:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product_info}

@app.get("/ingredient/{ingredient_name}")
def get_ingredient_details(ingredient_name: str):
    ingredient_info = get_ingredient_info(ingredient_name)
    if not ingredient_info:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return {"ingredient": ingredient_info}

@app.get("/sales/{product_id}")
def get_sales_details(product_id: int):
    sales_info = get_sales_data(product_id)
    if not sales_info:
        raise HTTPException(status_code=404, detail="Sales data not found")
    return {"sales": sales_info}
