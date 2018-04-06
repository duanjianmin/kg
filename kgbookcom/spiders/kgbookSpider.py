import scrapy
from ..items import KgbookcomItem


class kgbookSpider(scrapy.Spider):
    name = "kgbookSpider"
    allowed_domains = ['kgbook.com']
    start_urls = ["https://kgbook.com/xiandaiwenxue/"]
    img_urls = []
    # for i in range(2, 400):
    #     start_urls.append("http://699pic.com/people-"+str(i)+"-0-0-0-0-0-0.html")

    def parse(self, response):
        urllist = response.xpath('//*[@class="channel-item"]/div[2]/h3/a/@href').extract()
        for tempUrl in urllist:
            if (str(tempUrl).startswith('http')):
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
        print('----------------------------------')
        return item
