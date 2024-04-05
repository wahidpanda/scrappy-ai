

from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/s?k=iphone"

wanted_list=["₹58,999","Apple iPhone 14 (128 GB) - Midnight"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))



