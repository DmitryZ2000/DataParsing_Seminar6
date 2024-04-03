# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class UnsplashparserPipeline:
    def process_item(self, item, spider):
        print()
        return item

class UnsplashPhotosPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        try:
            if item['photos']:
                for img_url in item['photos']:
                    try:
                        yield scrapy.Request(img_url)
                    except Exception as e:                
                        print(e)
        except Exception as e:
            print(e)
