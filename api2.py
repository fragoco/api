#! venv\Scripts\python.exe

from flask import Flask
from flask_restful import Resource, Api, reqparse
from pathlib import Path
import pandas as pd

app = Flask(__name__)
api = Api(app)

# Create paths to data locations
# /data/product_hierarchy.csv
product_path = Path("data\\product_hierarchy.csv")
# /data/store_cities.csv
cities_path = Path("data\\store_cities.csv")
# /data/sales/sales.csv (Subfolder changed to "sales" from "sales.csv")
sales_path = Path("data\\sales\\sales.csv")

# Read data sets
sales_df = pd.read_csv(sales_path)
prod_df = pd.read_csv(product_path)
cities_df = pd.read_csv(cities_path)

# Pepare sales_df "date"-column data
sales_df["date"] = pd.to_datetime(sales_df["date"], format="%Y-%m-%d")


class ProdSales(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("hierarchy1_id", type=str, required=True)
        parser.add_argument("startdate", type=str, required=True)
        parser.add_argument("enddate", type=str, required=True)
        args = parser.parse_args()

        # Creating date range
        date_range = pd.date_range(
            start=pd.to_datetime(args["startdate"]), end=pd.to_datetime(args["enddate"])
        )

        # pepare filters
        # filter by user provided dates
        date_range_filt = sales_df["sales"].isin(date_range)
        # "hierarchy_id" filter applied to "product_id" in prod_df
        hierarchy_filt = prod_df["hierarchy1_id"] == args["hierarchy1_id"]
        prod_filt = prod_df.loc[hierarchy_filt]["product_id"]

        # prodsales_filt = date_range_filt & prod_filt

        # return filtered data
        return sales_df.loc[date_range_filt & prod_filt].agg(
            {"sales": "sum", "revenue": "sum"}
        )

        # return {
        #     "hierarchy1_id": args["hierarchy1_id"],
        #     "startdate": args["startdate"],
        #     "enddate": args["enddate"],
        # }


class CitySales(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("cityid", type=str, required=True)
        parser.add_argument("startdate", type=str, required=True)
        parser.add_argument("enddate", type=str, required=True)
        args = parser.parse_args()

        return {
            "cityid": args["cityid"],
            "startdate": args["startdate"],
            "enddate": args["enddate"],
        }


class Volume(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("product_id", type=str, required=True)
        parser.add_argument("startdate", type=str, required=True)
        parser.add_argument("enddate", type=str, required=True)
        args = parser.parse_args()

        return {
            "product_id": args["product_id"],
            "startdate": args["startdate"],
            "enddate": args["enddate"],
        }


# Resource Product Sales Data (ProdSales) has multiple URLs
api.add_resource(ProdSales, "/", "/prodsales")
api.add_resource(CitySales, "/citysales")
api.add_resource(Volume, "/volume")

if __name__ == "__main__":
    app.run(debug=True)
