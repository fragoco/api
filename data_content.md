# Data Content

This data is collected from a Turkish retail company. Time period is beginning from 2017 to the end of 2019.

## File descriptions

- sales.csv - Train data. Daily sales data covering 2017-2019.
- product_hierarchy.csv - Data containing the hierarchy and sizes of the products.
- store_cities.csv - Data containing the city, type and size information of the stores.

## Column descriptions

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
