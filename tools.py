# 

import os
from dotenv import load_dotenv
from datetime import datetime
import sqlite3
from typing import Optional, Union, List, Dict, Tuple
import json

def search_products(
    description: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
    price: Optional[float] = None,
    quantity: Optional[int] = None,
) -> List[Dict]:
    """
    Search for products based on description, quantity, price range, and rating range.

    Args:
        description: (Optional[str]) The name of the product. Defaults to None.
        category: (Optional[str]) The category of the product. Defaults to None.
        min_price: (Optional[float]) The minimum price. Defaults to None.
        max_price: (Optional[float]) The maximum price. Defaults to None.
        min_rating: (Optional[float]) The minimum rating. Defaults to None.
        max_rating: (Optional[float]) The maximum rating. Defaults to None.
        price: Optional[float] The price of the product. Defaults to None.
        quantity: Optional[int] The quantity of the product. Defaults to None.

    Returns:
        List[Dict]: A list of product dictionaries matching the search criteria.
    """

    query = "SELECT description, price, quantity FROM products WHERE 1=1"
    params: Tuple = ()

    if description:
        query += " AND LOWER(description) LIKE LOWER(?)"
        params += (f"%{description}%",)
    if category:
        query += " AND LOWER(category) LIKE LOWER(?)"
        params += (f"%{category}%",)
    if price is not None:
        query += " AND price >= ?"
        params += (price,)
    if max_price is not None:
        query += " AND price <= ?"
        params += (max_price,)
    if min_rating is not None:
        query += " AND rating >= ?"
        params += (min_rating,)
    if max_rating is not None:
        query += " AND rating <= ?"
        params += (max_rating,)
    query += " LIMIT 2"

    return execute_query(query, params)

def execute_query(query: str, params: Tuple = ()) -> List[Dict]:
    try:
        with sqlite3.connect('FullStackSQL.db') as conn:
            conn.row_factory = sqlite3.Row  # This allows accessing columns by name
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            # Convert rows to a list of dictionaries
            return [dict(row) for row in results]
    except sqlite3.Error as e:
        # Handle database errors
        print(f"Database error: {e}")
        return []
    except Exception as e:
        # Handle other potential errors
        print(f"An error occurred: {e}")
        return []
