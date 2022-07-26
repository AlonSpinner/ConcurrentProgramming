from workers.WikiWorker import WikiWorker

wikiWorker = WikiWorker()
symbol_list = []
for symbol in wikiWorker.get_sp_500_companies():
    symbol_list.append(symbol)

print(len(symbol_list))