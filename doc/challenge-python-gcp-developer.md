# Challenge

## Tips

- Make sure to read the feature description fully
- Make sure to understand each acceptance criteria
- Make sure to explore the datasets and their columns
- Assume any missing data/information, if necessary
- Try to make it as production ready as you have time for
- You are free to take shortcuts, but be prepared to discuss them and how to improve them
- If you can't achieve every acceptance criteria, then that is fine. Let us talk about it in our technical discussion
- Above all, have fun

## Feature

As a Data Analyst, I want to be able to search and view relevant sales data, so that I can make better business decisions.

### Acceptance Criteria

- Given a Data Analyst, when wanting to view sales that are aggregated by specific
city_id/specific hierarchy_id and date range, then there is an API that provides this capability.
- Given a Data Analyst, when wanting to view aggregated volume data for specific product and date range, then there is an API that provides this capability.
- Given a Data Analyst, when wanting to view Total Revenue on Public holidays, then there is an API that provides this capability (Optional).

### Technical Requirements & Questions

- Dataset - [https://www.kaggle.com/berkayalan/retail-sales-data](https://www.kaggle.com/berkayalan/retail-sales-data)
- Backend API - Build a python application which can read from provided datasets and based on the user’s input, aggregate the data accordingly and return the value back to the user. It would be good if you can create a REST API interface for your python application. API.

- Queries -
  - Total Sales quantity and revenue for Specific product **hierarchy1_id** and specified **date** range. Returns a single row.
  - Total Sales quantity and revenue for Specific **city_id** and specified **date** range. Returns a single row.
  - Total **volume** (using provided **product dimensions** multiplied by **quantity**) of a specific **product** for specified **date** range. Returns a single row.
- Bonus steps (optional)
  - Containerize your application
  - Assuming the Region to be Sweden, calculate **Total revenue** on **2018 Public holiday** dates. You can choose to either web scrape or download public holidays for 2018.
- Questions
  - How will you test this application?
  - If there is a requirement to deploy the above application on Cloud (Preferably Google Cloud), which services will you prefer to use and why?

## Notes

Understanding the data

### Data Content

This data is collected from a Turkish retail company. Time period is beginning from 2017 to the end of 2019.

### File descriptions

- sales.csv - Train data. Daily sales data covering 2017-2019.
- product_hierarchy.csv - Data containing the hierarchy and sizes of the products.
- store_cities.csv - Data containing the city, type and size information of the stores.

### Column descriptions

- store_id - The unique identifier of a store.
- product_id - The unique identifier of a product.
- date - Sales date (YYYY-MM-DD)
- sales - Sales quantity
- revenue - Daily total sales revenue
- stock - End of day stock quantity
- price - Product sales price
- promotype1 - Type of promotion applied on channel 1
- promobin1 - Binned promotion rate for applied promotype1
- promotype2 - Type of promotion applied on channel 2
- promobin2 - Binned promotion rate for applied promotype2
- promodiscount2 - Discount rate for applied promo type 2
- promodiscounttype_2 - Type of discount applied
- product_length - Length of product
- product_depth - Depth of product
- product_width - Width of product
- hierarchy1_id
- hierarchy2_id
- hierarchy3_id
- hierarchy4_id
- hierarchy5_id
- storetype_id
- store_size
- city_id
- trainortest - rows with train tag will be used to train KNNRegressor and rows with test tag will be used for accuracy calculation

### Queries

- View Product sales
  - input
    - hierarchy1_id
    - date
  - output
    - sales
    - revenue
- View City sales
  - input
    - city_id
    - date
  - output
    - sales
    - revenue
- Volume data
  - input
    - product_id
    - product_length
    - product_depth
    - product_width
    - sales (quantity?)
    - date
  - output
    - volume
- Public Holiday Sales
  - input
    - 2018 Public holidays
  - output
    - revenue (holidays)

#### Locations
