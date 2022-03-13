# Sales & Product data API

## Setup

The datasets have been downloaded and placed in the `\data` folder:  
`\data\product_hierarchy.csv`  
`\data\store_cities.csv`  
`\data\sales\sales.csv`

Install the necessary libraries using pip  
`pip install -r requirements.txt`

run the application  
`python api.py`

## API usage

Endpoint|GET request format|Example|Returns
-|-|-|-
/prodsales|/prodsales[hierarchyid][startdate YYYY-MM-DD][enddate YYYY-MM-DD]|/prodsales?hierarchyid=H01&startdate=2017-01-02&enddate=2017-02-28|Total sales quantity, Total revenue
/citysales|/citysales[cityid][startdate YYYY-MM-DD][enddate YYYY-MM-DD]|/citysales?cityid=C005&startdate=2017-02-02&enddate=2017-05-02|Total sales quantity, Total revenue
/volume|/volume[productid][startdate YYYY-MM-DD][enddate YYYY-MM-DD]|/volume?productid=P0001&startdate=2017-01-02&enddate=2017-05-28|Total sales physical volume, Total stock physical volume

### Short personal message

Hi everyone,
thank you for a fun and interesting challenge, it has kept me occupied and entertained over the weekend.
