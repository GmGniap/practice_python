# 2022 Code 

### Mini_Project - Scraping Tableau Featured Developer page 
- Main idea is to make monthly scraper to collect Tableau Dev data and make an analysis/viz.
- Buit with -> `Selenium` , `BeautifulSoup` , `Datasette` , `Python`
----------

## Big_Project - Burma Price Monitor

- Built with -> `requests-html` , `pandas` , `datasette` , `github-action`, `cloud-run`

#### About

The base idea of this project is to record the daily struggles of Burma People to be remembered in the furture and the significant point to monitor is **price** of commodity or groceries.

Current tracking prices - Rice , Common groceries , Petrol

#### Data Sources

1. Petrol price from Myanmar Petroleum Trade Association (short : MPTA)
2. Common gorceries price from Wisarra
3. Rice data from Myanmar Rice Association Facebook Page.

#### Workflow

1. Daily collect/scrape data from websites.
2. Automate with Github Action.
3. Deploy with `Datasette` to Google `Cloud run` service.

#### Remaining to do :pencil:

- Data Viz
    - [ ] Create Tableau Dashboard
    - [ ] Embed dashboard into webpage

- Datasette
    - [ ] Update metadata.yml
    - [ ] Add custom template for UI

- Myanmar Rice
    - [ ] Collect data from Gsheet
    - [ ] Insert into price.db

- MPTA : 
    - [x] Update to Datasette
    - [x] Automate with Github Action

- Wisarra 
    - [x] Update to Datasette