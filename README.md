<h1 align="center">
  <strong>
      Yahoo Finance Stock Scraper
  </strong>
</h1>

<p align="center">
    <img align="center" src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white"/>
    <img align="center" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
</p>

Selenium driven web-scraping tool capable of scraping multiple Yahoo Finance stock pages and generating a csv file containing various detailed statistics of each stock.

## Usage
First run...
```bash
pip install selenium webdriver-manager
```

Then you can run the following command, which should generate a .csv file containing information about the stocks you provide as command line arguments.
```
python scraper.py TSLA AMZN GOOG
```
(_The script may take a while to finish working depending on the number stocks you want to scrape_)</br></br>

