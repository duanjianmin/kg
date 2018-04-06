# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline


class KgbookcomPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        print('))))))))))))))))))))))))))))))))')
        print(item['images'])
        print(item['image_urls'])
        print('))))))))))))))))))))))))))))))))')
        return item
