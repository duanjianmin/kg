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
        kgbookitem = KgbookcomItem()
        namelist = response.xpath('//*[@class="channel-item"]/div[2]/h3/a/text()').extract()
        urllist = response.xpath('//*[@class="channel-item"]/div[2]/h3/a/@href').extract()

        kgbookitem['images'] = namelist
        for tempUrl in urllist:
            if (str(tempUrl).startswith('http')):
                yield scrapy.Request(tempUrl, callback=self.img_url)
        kgbookitem['image_urls'] = self.img_urls
        print('*******************************')
        print(self.img_urls)
        print('*******************************')
        yield kgbookitem

    def img_url(self, response):
        imageUrls = response.xpath('//*[@id="news_picture"]/img/@src').extract()
        for iurl in imageUrls:
            self.img_urls.append("https://kgbook.com"+iurl)
        print('----------------------------------')
