# -*- coding: utf-8 -*-
import re

import scrapy

from scrapy_splash import SplashRequest
from scrapy.http.request import Request

# from baojun002.baojun002.items import Baojun002Item
from baojun002.items import Baojun002Item


class TestSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        url = "https://tuan.qunar.com/vc/index.php?category=all_i"
        # url = "https://www.baidu.com/"
        r = SplashRequest(
            url=url,
            callback=self.parse_li,
            args={"wait": 3, 'viewport': '1024x2480', 'timeout': 90, 'images': 0, 'resource_timeout': 1,
                  'proxy': 'http://child-prc.intel.com:913'},
            splash_url='http://10.239.220.25:8050'
        )
        # print(r)
        yield r

    def parse_li(self, response):
        # li_list = response.xpath('//ul[@class="cf"]/li/a/@href').extract()
        li_list = response.xpath('//div[@id="list"]/ul/li')
        # title_list = response.xpath('//div[@class="nm"]/text()').extract()
        for i in li_list:
            url = i.xpath("./a[1]/@href").extract_first()
            url = "https:" + url
            title = i.xpath(".//div[@class='nm']/text()").extract_first()
            title = title.strip()
            price = i.xpath(".//div[@class='price']/span/em/text()").extract_first()
            # print(price)
            # print(url)
            # print(title)
            item = Baojun002Item()
            item["title"] = title
            item["price"] = int(price)
            # print(item)
            r = Request(
                url=url,
                callback=self.parse_url,
                meta={
                    "refer": url,
                    "item": item
                }

            )

            yield r
            # break

    def parse_url(self, response):
        # print(response.text)
        try:
            url = "https://" + re.search(r'//(.*?)\'', response.text).group(1)
        except Exception as e:
            print("url not return")
            return
        refer = response.meta["refer"]
        item = response.meta['item']
        # print(url)
        r = SplashRequest(
            url=url,
            callback=self.parse_detail,
            args={"wait": 3, 'viewport': '1024x2480', 'timeout': 90, 'images': 0, 'resource_timeout': 1,
                  'proxy': 'http://child-prc.intel.com:913', "refer": refer},
            splash_url="http://10.239.220.25:8050",
            meta={
                "item": item
            }

        )

        yield r

    def parse_detail(self, response):

        item = response.meta['item']
        try:
            subhead = response.xpath('//div[@class="summary"]/h1/text()').extract()[1]
            item["subhead"] = subhead.strip()
        except:
            return
        try:
            intro = response.xpath(
                '//div[@class="summary"]/h2/div/span/text()').extract()
            intro = [str.strip() for str in intro]
            intro = "\n".join(intro)

            item["intro"] = intro
            print(intro)
        except:
            return

        print(item)
        yield item
