# -*- coding:utf-8 -*-
import json
import random
import re

import requests
from lxml import etree


# from info.models import *

class Crawl(object):
    def __init__(self):
        self.host = 'https://utzu3.package.qunar.com'
        self.entrance_url = 'http://utzu3.package.qunar.com/search/a-a-a-a-a---a----opt-desc--#vid=qb2c_frly&func=6Lef5Zui5ri4&pid=388238920&rid=28253804&vd=56aP5Lq65peF5ri4'
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
        ]
        self.headers = {
            'User-Agent': random.choice(self.user_agents),
            'Cookie': 'QN99=7702; QN300=auto_4e0d874a; QN1=eIQjmlzBqHFhRT6bDfWjAg==; QunarGlobal=10.86.213.150_21340582_16a546e783d_24cd|1556195442035; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN601=4405cb449f5f74e47e559d919c6908a8; _i=VInJOyfIzIYwCPO3ZDpzKOXMI-Yq; QN269=F1050570675511E99D43FA163E8B6C19; QN48=4f4d85f0-da3d-4546-a4f0-7f23c94889fd; fid=739f6953-eced-475f-a342-1c80358b10bb; QN49=28253804; _jzqx=1.1556195459.1556339418.2.jzqsr=dujia%2Equnar%2Ecom|jzqct=/pi/detail_28253804.jzqsr=utzu3%2Epackage%2Equnar%2Ecom|jzqct=/search/a-a-a-a-a---a----opt-desc--; _vi=pXoyH-6P3sxy37s_Qed-O8oYYruUZKPjDkuZk4piOJ0ajU43zyZrr3swuU7Ynm769UP2WfYUXkV64bx7ctRmVWW2kK36u-mhc-GWt76HyZHqJ3sA-6hvMvHZ4eU1lw8qQh9IWJCR4jeJrZ1oec3hbYAL9oMBSid30z52gq812gk_; _jzqckmp=1; csrfToken=A73mjrtJd5G89ADz4NCIaXhlth7xBEoZ; QN271=a714299d-7b3d-48c4-9812-a050b184bb48; _qzja=1.807867989.1556195458625.1556376179521.1556449335082.1556376357272.1556449335082..0.0.56.10; _qzjc=1; _qzjto=1.1.0; _jzqa=1.2817153281033170000.1556195459.1556376179.1556449335.10; _jzqc=1; _qzjb=1.1556449335081.1.0.0.0; _jzqb=1.2.10.1556449335.1; Hm_lvt_a8a41d37454fd880cdb23d6ef05d917b=1556195459,1556199009,1556365403,1556449335; Hm_lpvt_a8a41d37454fd880cdb23d6ef05d917b=1556449335; QN243=341'
        }
        self.schemes = []

    def get_schemes(self):
        # 获取每个套餐的入口地址
        response = requests.get(url=self.entrance_url, headers=self.headers).text
        html = etree.HTML(response)
        self.schemes = html.xpath('/html/body/div[2]/div[4]/div/div[2]/div[3]/dl/dt/a/@href')

    def get_details(self):
        scheme_url = self.host + self.schemes[0]
        pid = re.search(r'id=(\d+)', scheme_url).group(1)
        print(scheme_url)
        response = requests.get(url=scheme_url, headers=self.headers).text
        html = etree.HTML(response)

        name = html.xpath('//*[@id="page-root"]/div[2]/div[3]/div[2]/h1/text()')[1].strip()
        features = html.xpath('//*[@id="page-root"]/div[2]/div[3]/div[2]/h2/div/span/text()')
        feature_list = [str.strip() for str in features]
        feature = '\n'.join(feature_list)
        get_detail_api = '{}/user/detail/getDetail.json?pId={}'.format(self.host, pid)
        get_location_api = '{}/user/detail/getTrffcHtlInfo.json?pId={}'.format(self.host, pid)
        response = json.loads(requests.get(get_detail_api, headers=self.headers).text)
        introduce = response['data']['feature']['standardContent'][0]['content']
        contains_content = response['data']['feeInfo']['costIncludeDesc']
        response = json.loads(requests.get(get_location_api, headers=self.headers).text)
        originating = response['data']['TRAFFIC']['round'][0]['backs'][0].get('arrCity', None)
        if not originating:
            originating = response['data']['TRAFFIC']['round'][0]['backs'][0].get('gatherSpot', None)
        end_locale = response['data']['TRAFFIC']['round'][0]['backs'][0].get('depCity', None)
        if not end_locale:
            end_locale = response['data']['TRAFFIC']['round'][0]['backs'][0].get('arrStation', None)
        through_time = html.xpath('//*[@id="page-root"]/div[2]/div[3]/div[2]/div[3]/ul/li[2]/span/em[2]/text()')[
            0].strip()
        if len(list(through_time)) == 2:
            day = int(list(through_time)[0])
            night = 0
        else:
            day = int(list(through_time)[0])
            night = int(list(through_time)[2])
        print(name)
        print(feature)
        print(day)
        print(night)
        print(introduce)
        print(originating)
        print(end_locale)
        print(contains_content)

    def get_journey(self):
        scheme_url = self.host + self.schemes[0]
        pid = re.search(r'id=(\d+)', scheme_url).group(1)
        get_journey_api = '{}/user/detail/getSchedule.json?pId={}'.format(self.host, pid)
        print(get_journey_api)
        response = json.loads(requests.get(get_journey_api, headers=self.headers).text)
        for i in response['data']['dailySchedules']:
            # 循环每天的信息
            number = i['daySeq']
            hotel = i.get('hotelDesc', None)
            print('第{}天'.format(number))
            print('酒店:{}'.format(hotel))
            content = i['scheduleTours'][0]['data'].get('description', None)
            if not content and len(i['scheduleTours']) == 1:
                for experience in i['scheduleTours']:
                    if experience['type'] == 'visit':
                        time = experience['time']
                        content = experience['data']['description']
                        print(time)
                        print(content)
            else:
                print('内容:{}'.format(content))
                time = i['scheduleTours'][0]['time']
                print(time)
                details = i['scheduleTourDetails']
                if details is not None:
                    for detail in details:
                        print(detail['tourSpot'])  # 景点名
                        print(detail['tourImages'])  # 照片

    def get_ticket(self):
        scheme_url = self.host + self.schemes[0]
        pid = re.search(r'id=(\d+)', scheme_url).group(1)
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'referer': 'https://utzu3.package.qunar.com/user/id={}'.format(pid),
            'Cookie': 'QN99=7702; QN300=auto_4e0d874a; QN1=eIQjmlzBqHFhRT6bDfWjAg==; QunarGlobal=10.86.213.150_21340582_16a546e783d_24cd|1556195442035; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN601=4405cb449f5f74e47e559d919c6908a8; _i=VInJOyfIzIYwCPO3ZDpzKOXMI-Yq; QN269=F1050570675511E99D43FA163E8B6C19; QN48=4f4d85f0-da3d-4546-a4f0-7f23c94889fd; fid=739f6953-eced-475f-a342-1c80358b10bb; QN49=28253804; _jzqx=1.1556195459.1556339418.2.jzqsr=dujia%2Equnar%2Ecom|jzqct=/pi/detail_28253804.jzqsr=utzu3%2Epackage%2Equnar%2Ecom|jzqct=/search/a-a-a-a-a---a----opt-desc--; _vi=pXoyH-6P3sxy37s_Qed-O8oYYruUZKPjDkuZk4piOJ0ajU43zyZrr3swuU7Ynm769UP2WfYUXkV64bx7ctRmVWW2kK36u-mhc-GWt76HyZHqJ3sA-6hvMvHZ4eU1lw8qQh9IWJCR4jeJrZ1oec3hbYAL9oMBSid30z52gq812gk_; _jzqckmp=1; csrfToken=A73mjrtJd5G89ADz4NCIaXhlth7xBEoZ; _qzjc=1; _jzqa=1.2817153281033170000.1556195459.1556376179.1556449335.10; _jzqc=1; Hm_lvt_a8a41d37454fd880cdb23d6ef05d917b=1556195459,1556199009,1556365403,1556449335; QN271=d3c9888f-63e0-431d-a60d-d00c707a592e; QN243=344; _qzja=1.807867989.1556195458625.1556376179521.1556449335082.1556449335082.1556449710375..0.0.57.10; _qzjb=1.1556449335081.2.0.0.0; _qzjto=2.1.0; _jzqb=1.4.10.1556449335.1; Hm_lpvt_a8a41d37454fd880cdb23d6ef05d917b=1556449710'
        }
        get_ticket_api = '{}/api/calPrices.json?tuId=&pId={}&month=2019-06'.format(self.host, pid)
        print(get_ticket_api)
        response = json.loads(requests.get(get_ticket_api, headers=headers).text)
        for ticket in response['data']['team']:
            print(ticket['date'])
            print(ticket['prices']['adultPrice'])


def main():
    crawl = Crawl()
    crawl.get_schemes()
    crawl.get_details()
    crawl.get_journey()
    crawl.get_ticket()


if __name__ == '__main__':
    main()
