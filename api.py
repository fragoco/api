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
        """GET request data for product sales quantity and revenue"""

        parser = reqparse.RequestParser()
        parser.add_argument("hierarchyid", type=str, required=True)
        parser.add_argument("startdate", type=str, required=True)
        parser.add_argument("enddate", type=str, required=True)
        args = parser.parse_args()

        # Creating date range
        date_range = pd.date_range(
            start=pd.to_datetime(args["startdate"]), end=pd.to_datetime(args["enddate"])
        )

        # Prepare filters
        # Filter by user provided dates
        date_range_filt = sales_df["date"].isin(date_range)
        # "hierarchy_id" filter applied to "product_id" in prod_df
        hierarchy_filt = prod_df["hierarchy1_id"] == args["hierarchyid"]
        # Series created with the matching result of the prod_df "product_id" column filtered by "hierarchy1_id"
        prod_hierarchy_filt = prod_df.loc[hierarchy_filt]["product_id"]
        # Filter applied to sales_df "product_id" column
        prod_filt = sales_df["product_id"].isin(prod_hierarchy_filt)

        # Return filtered, aggregated data
        return (
            sales_df.loc[(date_range_filt & prod_filt)]
            .agg({"sales": "sum", "revenue": "sum"})
            .to_dict()
        )


class CitySales(Resource):
    def get(self):
        """GET request data for city specific sales quantity and revenue"""

        parser = reqparse.RequestParser()
        parser.add_argument("cityid", type=str, required=True)
        parser.add_argument("startdate", type=str, required=True)
        parser.add_argument("enddate", type=str, required=True)
        args = parser.parse_args()

        # Creating date range
        date_range = pd.date_range(
            start=pd.to_datetime(args["startdate"]), end=pd.to_datetime(args["enddate"])
        )

        # Prepare filters
        # Filter by user provided dates
        date_range_filt = sales_df["date"].isin(date_range)
        # city_id filter applied to store_id
        city_filt = cities_df["city_id"] == args["cityid"]
        #
        store_filt = cities_df.loc[city_filt]["store_id"]
        #
        store_sales_filt = sales_df["store_id"].isin(store_filt)

        return (
            sales_df.loc[(date_range_filt & store_sales_filt)]
            .agg({"sales": "sum", "revenue": "sum"})
            .to_dict()
        )


class Volume(Resource):
    def get(self):
        """GET request data for volume sales quantity and stock"""

        parser = reqparse.RequestParser()
        parser.add_argument("productid", type=str, required=True)
        parser.add_argument("startdate", type=str, required=True)
        parser.add_argument("enddate", type=str, required=True)
        args = parser.parse_args()

        # Creating date range
        date_range = pd.date_range(
            start=pd.to_datetime(args["startdate"]), end=pd.to_datetime(args["enddate"])
        )

        # Prepare filters
        # Filter by user provided dates
        date_range_filt = sales_df["date"].isin(date_range)
        #
        sales_prodid = sales_df["product_id"] == args["productid"]
        #
        prod_prodid = prod_df["product_id"] == args["productid"]

        # Calculations
        # Single product volume size
        prod_vol = (
            prod_df.loc[prod_prodid]["product_length"]
            * prod_df.loc[prod_prodid]["product_depth"]
            * prod_df.loc[prod_prodid]["product_width"]
        )
        # Sum of sales quantity and stock quantity during user defined period
        sales_stock = sales_df.loc[(date_range_filt & sales_prodid)].agg(
            {"sales": "sum", "stock": "sum"}
        )

        # Return multiplied results
        return {
            "Total sales volume": prod_vol[1] * sales_stock[0],
            "Total stock volume": prod_vol[1] * sales_stock[1:2][0],
        }


# Resource Product Sales Data (ProdSales) has multiple URLs
api.add_resource(ProdSales, "/", "/prodsales")
api.add_resource(CitySales, "/citysales")
api.add_resource(Volume, "/volume")

if __name__ == "__main__":
    app.run(debug=False)
