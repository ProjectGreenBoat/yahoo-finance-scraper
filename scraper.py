from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tqdm import tqdm, trange

import sys
import csv

# if there are no CLI parameters
# if len(sys.argv) <= 1:
#     print('Ticker symbol CLI argument missing!')
#     sys.exit(2)

# read the ticker from the CLI argument
# ticker_symbol = sys.argv[1]
           
# Scrape the stock page for data
def scrape_stock(driver, ticker_symbol):
    print(f"Started Scraping: {ticker_symbol}")
    stock = {}
    if (ticker_symbol.isalpha()):
        url = f'https://finance.yahoo.com/quote/{ticker_symbol}'
        driver.get(url)
        stock['ticker'] = ticker_symbol

        # scraping logic...
        try:
            stock['regular_market_price'] = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="regularMarketPrice"]').text
            stock['regular_market_change'] = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="regularMarketChange"]').text
            stock['regular_market_change_percent'] = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="regularMarketChangePercent"]').text.replace('(', '').replace(')', '')
        except:
            print(f"Warning: Couldn't find regular market data for {ticker_symbol}")

        try:
            stock['post_market_price'] = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="postMarketPrice"]').text
            stock['post_market_change'] = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="postMarketChange"]').text
            stock['post_market_change_percent'] = driver.find_element(By.CSS_SELECTOR, f'[data-symbol="{ticker_symbol}"][data-field="postMarketChangePercent"]').text.replace('(', '').replace(')', '')
        except:
            print(f"Warning: Couldn't find post market data for {ticker_symbol}")

        try:
            stock['previous_close'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="PREV_CLOSE-value"]').text
        except:
            print(f'\tCouldn\'t find previous close for {ticker_symbol}')

        try:
            stock['open_value'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="OPEN-value"]').text
        except:
            print(f'\tCouldn\'t find open valuefor {ticker_symbol}')

        try:
            stock['bid'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="BID-value"]').text
        except:
            print(f'\tCouldn\'t find bid for {ticker_symbol}')
        
        try:
            stock['ask'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="ASK-value"]').text
        except:
            print(f'\tCouldn\'t find ask for {ticker_symbol}')
        
        try:
            stock['days_range'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="DAYS_RANGE-value"]').text
        except:
            print(f'\tCouldn\'t find days range for {ticker_symbol}')
        
        try:
            stock['week_range'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="FIFTY_TWO_WK_RANGE-value"]').text
        except:
            print(f'\tCouldn\'t find week range for {ticker_symbol}')

        try:
            stock['volume'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="TD_VOLUME-value"]').text
        except:
            print(f'\tCouldn\'t find volume for {ticker_symbol}')
        
        try:
            stock['avg_volume'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="AVERAGE_VOLUME_3MONTH-value"]').text
        except:
            print(f'\tCouldn\'t find AVG volume for {ticker_symbol}')

        try:
            stock['market_cap'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="MARKET_CAP-value"]').text
        except:
            print(f'\tCouldn\'t find market cap for {ticker_symbol}')

        try:
            stock['beta'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="BETA_5Y-value"]').text
        except:
            print(f'\tCouldn\'t find beta for {ticker_symbol}')
        
        try:
            stock['pe_ratio'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="PE_RATIO-value"]').text
        except:
            print(f'\tCouldn\'t find pe ratio for {ticker_symbol}')
        
        try:
            stock['eps'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EPS_RATIO-value"]').text
        except:
            print(f'\tCouldn\'t find eps for {ticker_symbol}')

        try:
            stock['earnings_date'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EARNINGS_DATE-value"]').text
        except:
            print(f'\tCouldn\'t find earnings date for {ticker_symbol}')

        try:
            stock['dividend_yield'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="DIVIDEND_AND_YIELD-value"]').text
        except:
            print(f'\tCouldn\'t find dividend yield for {ticker_symbol}')
        
        try:
            stock['ex_dividend_date'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EX_DIVIDEND_DATE-value"]').text
        except:
            print(f'\tCouldn\'t find ex dividend date for {ticker_symbol}')

        try:
            stock['year_target_est'] = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="ONE_YEAR_TARGET_PRICE-value"]').text
        except:
            print(f'\tCouldn\'t find year target est. about {ticker_symbol}')

    print(f"Finished Scraping: {ticker_symbol}")
    return stock

# initialize a Chrome instance with the right configuration
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)
driver.set_window_size(1150, 1000)

# the array containing all scraped data
stocks = []

# Scrape the current top 30 trending stocks 
driver.get("https://finance.yahoo.com/trending-tickers/")
tickers = []
print("Finding Top Daily Stocks...")
with tqdm(total=30) as pbar:
    for i in range(1,31):
        tickers.append(driver.find_element(By.CSS_SELECTOR, f'tr.simpTblRow:nth-child({i}) > td:nth-child(1)').text)
        pbar.update(1);

# scraping all market securities
# for ticker_symbol in sys.argv[1:]:
#     stocks.append(scrape_stock(driver, ticker_symbol))
print("Scraping stocks...")
with tqdm(total=30) as pbar:
    for ticker in tickers:
        stocks.append(scrape_stock(driver, ticker))
        pbar.update(1)

# close the browser and free up the resources
driver.quit()

# extract the name of the dictionary fields
# to use it as the header of the output CSV file
max_len = -1
for stock in stocks: 
    if(len(stock) > max_len): 
        max_len = len(stock) 
        csv_header = stock # Pick stock with most data so the csv file has all the possible values

# export the scraped data to CSV
with open('stocks.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, csv_header)
    dict_writer.writeheader()
    dict_writer.writerows(stocks)

print("DONE! Output stock information to stocks.csv")