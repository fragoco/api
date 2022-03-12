# Challenge

## Tips

- Make sure to read the feature description fully
- Make sure to understand each acceptance criteria
- Make sure to explore the datasets and their columns
- Assume any missing data/information, if necessary
- Try to make it as production ready as you have time for
- You are free to take shortcuts, but be prepared to duscuss them and how to improve them
- If you can't achieve every acceptance criteria, then that is fine. Let us talk about it in our techincal discussion
- Above all, have fun

## Feature

As a Data Analys, I want to be able to search and view relevant sales data, so that I can make better business decisions.

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
  - Total Sales quantity and revenue for Specific **city id** and specified **date** range. Returns a single row.
  - Total **volume** (using provided **product dimensions** multiplied by **quantity**) of a specific **product** for specified **date** range. Returns a single row.
- Bonus steps (optional)
  - Containerize your application
  - Assuming the Region to be Sweden, calculate **Total revenue** on **2018 Public holiday** dates. You can choose to either web scrape or download public holidays for 2018.
- Questions
  - How will you test this application?
  - If there is a requirement to deploy the above application on Cloud (Preferably Google Cloud), which services will you prefer to use and why?

## Notes

### Queries

- Product sales
  - input
    - hierarchy1_id
    - date
  - output
    - sales
    - revenue
- City sales
  - input
    - city id
    - date
  - output
  