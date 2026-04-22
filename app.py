from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


# Implement homepage route that returns a welcome message
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Products API"})


# GET /products route that returns all products or filters by category
@app.route("/products")
def get_products():
    category = request.args.get("category")

    if category:
        filtered_products = [
            product for product in products
            if product["category"].lower() == category.lower()
        ]
        return jsonify(filtered_products)

    return jsonify(products)


# GET /products/<id> route that returns a specific product by ID or 404
@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((product for product in products if product["id"] == id), None)

    if product:
        return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)