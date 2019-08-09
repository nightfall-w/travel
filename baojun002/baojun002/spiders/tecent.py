import scrapy
from scrapy_splash import SplashRequest


class TencentStockSpider(scrapy.Spider):
    name = "tecent"

    def start_requests(self):
        urls = [
            'http://www.baidu.com',
        ]

        for url in urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 0.5})

    def parse(self, response):
        print(response.text)
        sel = scrapy.Selector(response)
        links = sel.xpath(
            "//div[@class='qq_main']//ul[@class='listInfo']//li//div[@class='info']//h3//a/@href").extract()
        requests = []

        return requests