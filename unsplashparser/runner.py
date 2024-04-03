from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

# from bookparser.spiders.book24 import Book24Spider
from spiders.unspalsh import UnspalshSpider

if __name__ == '__main__':
    install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
    configure_logging()
    process  = CrawlerProcess(get_project_settings())
    # query = input('Enter genre, for example space: ')
    query = 'food'
    process.crawl(UnspalshSpider, query=query )
    process.start()
