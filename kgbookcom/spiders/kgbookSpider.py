import scrapy
from ..items import KgbookcomItem


class kgbookSpider(scrapy.Spider):
    name = "kgbookSpider"
    allowed_domains = ['kgbook.com']
    start_urls = ["https://kgbook.com/xiandaiwenxue/index.html"]
    for i in range(2, 7):
        start_urls.append("https://kgbook.com/xiandaiwenxue/index_"+str(i)+".html")
        start_urls.append("https://kgbook.com/gudianwenxue/index_"+str(i)+".html")
        start_urls.append("https://kgbook.com/wuxiaxiaoshuo/index_"+str(i)+".html")


    def parse(self, response):
        urllist = response.xpath('//*[@class="channel-item"]/div[2]/h3/a/@href').extract()
        for tempUrl in urllist:
            if (str(tempUrl).startswith('http')):
                print()
            else:
                tempUrl = "https://kgbook.com"+tempUrl
            yield scrapy.Request(tempUrl, callback=self.img_url)
    def img_url(self, response):
        imageUrls = response.xpath('//*[@id="news_picture"]/img/@src').extract()
        images = response.xpath('//*[@id="content"]/h1/text()').extract()
        item = KgbookcomItem()
        item['images'] = images
        item['image_paths'] = images
        urls = []

        for iurl in imageUrls:
            urls += ["https://kgbook.com"+iurl]
        item['image_urls'] = urls
        return item
