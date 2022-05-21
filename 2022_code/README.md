# 2022 Code 

## Burma Price Monitor

- Built with -> `requests-html` , `pandas` , `datasette` , `github-action`, `cloud-run`, `bigquery`, `sqlite`

#### **About**

The base idea of this project is to record the daily struggles of Burma People to be remembered in the furture and the significant point to monitor is **price** of commodity or groceries.

Current tracking prices - Rice , Common groceries , Petrol

#### **Data Sources**

1. Petrol price from Myanmar Petroleum Trade Association (short : MPTA)
2. Common gorceries price from Wisarra
3. Rice data from Myanmar Rice Association Facebook Page.
4. Daily price rates from Denko company website. (starting from 2022 May 19)
5. Startfish Petroleum port price. (starting from 2019 Dec 29 to current day)

#### **Installation**
- Install required libraries :
```
pip install -r requirements.txt
```
- Run scraping task - [code](./scrape_marketprice.py)
```
python3 scrape_marketprice.py
```
- Deploy to datasette & cloud run
```
./deploy.sh
```

#### **Workflow**

1. Daily collect/scrape data from websites.
2. Automate with Github Action.
3. Deploy with `Datasette` to Google `Cloud run` service.

#### Remaining to do :pencil:

- Data Viz
    - [ ] Create Tableau Dashboard
    - [ ] Embed dashboard into webpage

- Datasette
    - [ ] Manual in Burmese
    - [ ] Add custom template for UI
    - [x] Update metadata.yml

- Myanmar Rice
    - [x] Collect data from Gsheet into BigQuery
    - [ ] BigQuery into SQlite db with python
    - [ ] Insert into price.db

- MPTA : 
    - [x] Update to Datasette
    - [x] Automate with Github Action

- Wisarra 
    - [x] Update to Datasette

- Added resources
    - [x] Denko - May 19
    - [x] Starfish Petrol - May 21

---------
### Mini_Project
- Scraping Tableau Featured Developer page
    - [Code](./scrape_tableau_dev.ipynb)
    - Main idea is to make monthly scraper to collect Tableau Dev data and make an analysis/viz.
    - Buit with -> `Selenium` , `BeautifulSoup` , `Datasette` , `Python`
----------