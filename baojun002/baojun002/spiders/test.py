# -*- coding: utf-8 -*-
import re
import json
import random

import gevent
from gevent import monkey

monkey.patch_all()
import scrapy
import requests
from scrapy.http.request import Request
from scrapy_splash import SplashRequest

from baojun002.items import Baojun002Item


class TestSpider(scrapy.Spider):
    name = 'test'
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    ]
    headers = {
        'User-Agent': random.choice(user_agents),
        'Cookie': 'QN99=7702; QN300=auto_4e0d874a; QN1=eIQjmlzBqHFhRT6bDfWjAg==; QunarGlobal=10.86.213.150_21340582_16a546e783d_24cd|1556195442035; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN601=4405cb449f5f74e47e559d919c6908a8; _i=VInJOyfIzIYwCPO3ZDpzKOXMI-Yq; QN269=F1050570675511E99D43FA163E8B6C19; QN48=4f4d85f0-da3d-4546-a4f0-7f23c94889fd; fid=739f6953-eced-475f-a342-1c80358b10bb; QN49=28253804; _jzqx=1.1556195459.1556339418.2.jzqsr=dujia%2Equnar%2Ecom|jzqct=/pi/detail_28253804.jzqsr=utzu3%2Epackage%2Equnar%2Ecom|jzqct=/search/a-a-a-a-a---a----opt-desc--; _vi=pXoyH-6P3sxy37s_Qed-O8oYYruUZKPjDkuZk4piOJ0ajU43zyZrr3swuU7Ynm769UP2WfYUXkV64bx7ctRmVWW2kK36u-mhc-GWt76HyZHqJ3sA-6hvMvHZ4eU1lw8qQh9IWJCR4jeJrZ1oec3hbYAL9oMBSid30z52gq812gk_; _jzqckmp=1; csrfToken=A73mjrtJd5G89ADz4NCIaXhlth7xBEoZ; QN271=a714299d-7b3d-48c4-9812-a050b184bb48; _qzja=1.807867989.1556195458625.1556376179521.1556449335082.1556376357272.1556449335082..0.0.56.10; _qzjc=1; _qzjto=1.1.0; _jzqa=1.2817153281033170000.1556195459.1556376179.1556449335.10; _jzqc=1; _qzjb=1.1556449335081.1.0.0.0; _jzqb=1.2.10.1556449335.1; Hm_lvt_a8a41d37454fd880cdb23d6ef05d917b=1556195459,1556199009,1556365403,1556449335; Hm_lpvt_a8a41d37454fd880cdb23d6ef05d917b=1556449335; QN243=341'
    }

    def start_requests(self):
        url = "https://tuan.qunar.com/vc/index.php?category=all_i"
        r = SplashRequest(
            url=url,
            callback=self.parse_li,
            args={"wait": 5, 'viewport': '4096x2480', 'timeout': 90, 'images': 0, 'resource_timeout': 1,
                  'proxy': 'http://child-prc.intel.com:913', },
            splash_url='http://ub2-cm-test02.sh.intel.com:8050'
        )
        yield r

    def parse_li(self, response):
        li_list = response.xpath('//div[@id="list"]/ul/li')
        for i in li_list:
            url = i.xpath("./a[1]/@href").extract_first()
            url = "https:" + url
            title = i.xpath(".//div[@class='nm']/text()").extract_first()
            title = title.strip()
            price = i.xpath(".//div[@class='price']/span/em/text()").extract_first()
            item = Baojun002Item()
            item["title"] = title
            item['destination'] = title.split(' ')[0]
            item['departure'] = '上海'
            day_night = title.split(' ')[1]
            index_day = day_night.find('天')
            item['day'] = day_night[:index_day]
            item['night'] = day_night[index_day + 1:-1]
            item["price"] = int(price)
            r = Request(
                url=url,
                callback=self.parse_url,
                meta={
                    "refer": url,
                    "item": item
                }
            )
            yield r

    def parse_url(self, response):
        try:
            url = "https://" + re.search(r'//(.*?)\'', response.text).group(1)
            item = response.meta['item']
        except Exception as es:
            print("*" * 150)
            return
        refer = response.meta["refer"]
        r = SplashRequest(
            url=url,
            callback=self.parse_detail,
            args={"wait": 5, 'viewport': '4096x2480', 'timeout': 90, 'images': 0, 'resource_timeout': 1,
                  "refer": refer, 'proxy': 'http://child-prc.intel.com:913'},
            splash_url="http://ub2-cm-test02.sh.intel.com:8050",
            meta={
                "item": item,
                'url': url
            }
        )
        yield r

    def parse_detail(self, response):
        item = response.meta['item']
        try:
            subhead = response.xpath('//div[@class="summary"]/h1/text()').extract()[1]
            item["subhead"] = subhead.strip()
            include = response.xpath(
                '//*[@id="ss-costIncludeDesc"]/div/div[2]').extract_first().replace('\n', '')
            item["include"] = include

            intro = response.xpath('//*[@id="ss-line-feature"]/div/div[2]/div/div').extract_first().replace('\n', '')
            item['intro'] = intro

            url = response.meta['url']
            re_result = re.match(r'(.*?\.com)(.*?)id=(\d+)&(.*)', url)
            host = re_result.group(1)
            pid = re_result.group(3)
            get_journey_api = '{}/user/detail/getSchedule.json?pId={}'.format(host, pid)
            r = Request(
                url=get_journey_api,
                callback=self.get_journeys,
                headers=self.headers,
                meta={
                    "item": item,
                    'host': host,
                    'pid': pid
                }
            )
        except:
            return
        yield r

    def get_journeys(self, response):
        try:
            item = response.meta['item']
            item['scenic_images'] = []
            item['journeys'] = []
            journey_response = json.loads(response.text)
            gevent_pool = []
            print("-------------------------------------------------------------------------------------")
            for i in journey_response['data']['dailySchedules']:
                # 循环每天的信息
                number = i['daySeq']
                hotel = i.get('hotelDesc', '')
                content = i['scheduleTours'][0]['data'].get('description', '')
                if not content and len(i['scheduleTours']) == 1:
                    visit_address = []
                    time = ''
                    for experience in i['scheduleTours']:
                        if experience['type'] == 'visit':
                            time = experience['time']
                            content = experience['data']['description']
                            images = experience['tourDetails']['imagesJson']
                            tourSpot = experience['tourDetails']['tourSpot']
                            visit_address.append(tourSpot)
                            if images:
                                for img_url in images:
                                    if img_url.startswith('//'):
                                        img_url = 'https:' + img_url
                                    g = gevent.spawn(self.get_image, img_url)
                                    gevent_pool.append(g)
                                    path = 'media/images/scenic/{}'.format(''.join(img_url[-38::].split('/')))
                                    item['scenic_images'].append(path)
                    journey = {'day': number, 'hotel': hotel, 'time': time, 'content': content,
                               'visit_address': visit_address}
                    item['journeys'].append(journey)
                else:
                    if not content:
                        content = i['description']
                    time = i['scheduleTours'][0]['time']
                    if not time:
                        time = i['scheduleTours'][1]['time']
                    details = i['scheduleTourDetails']
                    visit_address = []

                    if details is not None:
                        for detail in details:
                            images = detail['tourImages']
                            tourSpot = detail['tourSpot']
                            visit_address.append(tourSpot)
                            for img_url in images:
                                if img_url.startswith('//'):
                                    img_url = 'https:' + img_url
                                g = gevent.spawn(self.get_image, img_url)
                                gevent_pool.append(g)
                                path = 'media/images/scenic/{}'.format(''.join(img_url[-38::].split('/')))
                                item['scenic_images'].append(path)
                        journey = {'day': number, 'hotel': hotel, 'time': time, 'content': content,
                                   'visit_address': visit_address}
                        item['journeys'].append(journey)
                    else:
                        journey = {'day': number, 'hotel': hotel, 'time': time, 'content': content,
                                   'visit_address': ''}
                        item['journeys'].append(journey)
        except Exception as es:
            print(es)
            return
        if not all([item['scenic_images'], item['journeys']]):
            return
        gevent.joinall(gevent_pool)
        host = response.meta['host']
        pid = response.meta['pid']
        get_ticket_api = '{}/api/calPrices.json?tuId=&pId={}&month=2019-09'.format(host, pid)
        r = Request(
            url=get_ticket_api,
            callback=self.get_ticket,
            headers=self.headers,
            meta={
                "item": item
            }
        )
        yield r

    def get_image(self, url):
        proxies = {'http': 'http://child-prc.intel.com:913',
                   'https': 'https://child-prc.intel.com:913'}
        img_data = requests.get(url=url, headers=self.headers,
                                proxies=proxies).content
        with open('C:\\Users\\sys_syscafhost\\Desktop\\ss\\git\\travel\\media\\images\\scenic\\{}'.format(
                ''.join(url[-38::].split('/'))), 'wb') as f:
            f.write(img_data)

    def get_ticket(self, response):
        try:
            item = response.meta['item']
            response = json.loads(response.text)
            item['tickets'] = []
            for ticket in response['data']['team']:
                try:
                    end_date = response['data']['team'][
                        response['data']['team'].index(ticket) + int(item['night'])]['date']
                    surplus = random.choice(range(500))
                    ticket = {'start_date': ticket['date'], 'end_date': end_date, 'surplus': surplus,
                              'unit_price': ticket['prices']['adultPrice']}
                    item['tickets'].append(ticket)
                except IndexError:
                    break
        except Exception as es:
            print(es)
            return
        yield item
