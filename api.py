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
    def get(self):
        """GET request for sales data"""

        # reqparse object is deprecated, use Schema from Marshmallow instead...
        parser = reqparse.RequestParser()
        parser.add_argument("hierarchy_id")
        parser.add_argument("city_id")
        parser.add_argument("start_date")
        parser.add_argument("end_date")
        parser.add_argument("volume")
        args = parser.parse_args()

        # return "..."
        return f"city_id is {args['city_id']}"


# api.com/SalesData
api.add_resource(SalesData, "/salesdata")

if __name__ == "__main__":
    app.run(debug=True)
