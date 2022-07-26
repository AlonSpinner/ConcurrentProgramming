import threading
import requests
from lxml import html
import time
import random
from multiprocessing import Queue

class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue : Queue,  **kwargs):
        super(YahooFinancePriceScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()

    def run(self):
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break
            
            yahooFinancePriceWorker = YahooFinancePriceWorker(symbol = val)
            price = yahooFinancePriceWorker.get_price()
            print(price)
            time.sleep(random.random())


class YahooFinancePriceWorker():
    def __init__(self, symbol, **kwargs):
        self._symbol = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f"{base_url}{self._symbol}"

    def get_price(self):
        time.sleep(20 * random.random())
        r = requests.get(self._url)
        if r.status_code != 200:
            return
        page_contents = html.fromstring(r.text)
        raw_price = page_contents.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')[0].text
        price = float(raw_price.replace(',', ''))
        return price
