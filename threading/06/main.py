from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorker import YahooFinancePriceWorker
import time 

def main():

    scarpper_start_time = time.time()
    wikiWorker = WikiWorker()
    
    current_workers = []
    for symbol in wikiWorker.get_sp_500_companies():
        yahooFinancePriceWorker = YahooFinancePriceWorker(symbol = symbol)
        current_workers.append(yahooFinancePriceWorker)

    for w in current_workers:
        w.join()

    print("extracting time took", round(time.time() - scarpper_start_time, 1))


if __name__ == "__main__":
    main()
