import React, { useEffect, useState } from 'react';

const RecommendComponent = () => {
    const [recommendedProduct, setRecommendedProduct] = useState(null);

    useEffect(() => {
        fetch('http://localhost:8000/recommend') // Assuming FastAPI is running on port 8000
            .then((response) => response.json())
            .then((data) => {
                setRecommendedProduct(data.recommended_product);
            })
            .catch((error) => console.error('Error fetching data:', error));
    }, []);

    if (!recommendedProduct) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Recommended Product: {recommendedProduct.name}</h1>
            <p>Type: {recommendedProduct.type}</p>
            <p>Effects: {recommendedProduct.effects.join(', ')}</p>
            <h3>Ingredients:</h3>
            <ul>
                {recommendedProduct.ingredients.map((ingredient, index) => (
                    <li key={index}>
                        <strong>{ingredient.name}</strong>
                        <p>Properties: {ingredient.properties}</p>
                        <p>Common Effects: {ingredient.common_effects.join(', ')}</p>
                    </li>
                ))}
            </ul>
            <h3>Sales:</h3>
            <p>Units Sold (Last Month): {recommendedProduct.sales.units_sold}</p>
            <p>Revenue: ${recommendedProduct.sales.last_month_revenue.toFixed(2)}</p>
        </div>
    );
};

export default RecommendComponent;
