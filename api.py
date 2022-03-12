#! venv\Scripts\python.exe

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
from pathlib import Path

app = Flask(__name__)
api = Api(app)

# Data locations
# /data/product_hierarchy.csv
product_path = Path("data\\product_hierarchy.csv")

# /data/store_cities.csv
cities_path = Path("data\\store_cities.csv")

# /data/sales.csv/sales.csv
sales_path = Path("data\\sales.csv\\sales.csv")


class SalesData(Resource):
    def post(self):
        parser = reqparse.RequestParser()


if __name__ == "__main__":
    app.run(debug=True)
