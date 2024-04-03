from typing import Any
import scrapy
from scrapy.http import HtmlResponse
from items import UnsplashparserItem
from scrapy.loader import ItemLoader

class UnspalshSpider(scrapy.Spider):
    name = "unspalsh"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]    

    def parse(self, response: HtmlResponse):
        print()
        links = response.xpath("///div[@class='GFY23']//a[@class='rEAWd']")   
        for link in links:
            yield response.follow(link, callback=self.parse_photo)

    def parse_photo(self, response: HtmlResponse):
        loader = ItemLoader(item=UnsplashparserItem(), response=response)
        loader.add_xpath(field_name='name', xpath="//h1/text()")        
        loader.add_value(field_name='url', value=response.url)
        loader.add_xpath(field_name='photos', xpath="//div[@class='mfq0m']//div[@class='MorZF']")
        yield loader.load_item()

