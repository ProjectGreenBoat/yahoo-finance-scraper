<h1 align="center">
  <strong>
      Yahoo Finance Stock Scraper
  </strong>
</h1>

<p align="center">
    <img align="center" src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white"/>
    <img align="center" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
</p>

Selenium driven web-scraping tool that scrapes the top 30 trending tickers from yahoo finance and generates a csv file containing various detailed statistics of each stock.

## Usage
First run...
```bash
pip install -r requirements.txt
```

Then you can run the following command, which should generate a .csv file containing information about the stocks.
```
python scraper.py
```

## Parsing
How to parse the .csv file into a map
```python
def parse_csv(filename):
    data = {}
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ticker']:
                data[row['ticker']] = {k: v for k, v in row.items() if k != 'ticker'}
    return data

data_map = parse_csv('stocks.csv')

# Output
#{
#  "TSLA": {
#    "regular_market_price": "262.90",
#    "regular_market_change": "-28.36",
#    "regular_market_change_percent": "-9.74%",
#    "post_market_price": "262.65",
#    "post_market_change": "-0.25",
#    "post_market_change_percent": "-0.10%",
#    "previous_close": "291.26",
#    "open_value": "279.56",
#    "bid": "263.05 x 900",
#    "ask": "262.91 x 1800",
#    "days_range": "261.20 - 280.93",
#    "week_range": "101.81 - 314.67",
#    "volume": "173,200,396",
#    "avg_volume": "136,351,475",
#    "market_cap": "833.262B",
#    "beta": "N/A",
#    "pe_ratio": "77.78",
#    "eps": "3.38",
#    "earnings_date": "Oct 17, 2023 - Oct 23, 2023",
#    "dividend_yield": "N/A (N/A)",
#    "ex_dividend_date": "N/A",
#    "year_target_est": "216.94"
#  }, ...
#}
```
