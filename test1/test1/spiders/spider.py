import scrapy
from test1.items import RentItem


class RentSpiderBJ(scrapy.spiders.Spider):
    name = "Rent_BJ"
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {'test1.pipelines.RentHouseBJ': 100}
    }
    for i in range(1, 55):
        start_urls.append("https://bj.lianjia.com/zufang/dongcheng/pg%d/#contentList/" % i)
    for i in range(1, 74):
        start_urls.append("https://bj.lianjia.com/zufang/xicheng/pg%d/#contentList/" % i)
    for j in range(0, 2):
        for i in range(1, 101):
            start_urls.append("https://bj.lianjia.com/zufang/chaoyang/pg%dl%d/#contentList/" % (i, j))
    for i in range(1, 85):
        start_urls.append("https://bj.lianjia.com/zufang/chaoyang/pg%dl2l3/#contentList/" % i)
    for i in range(1, 101):
        start_urls.append("https://bj.lianjia.com/zufang/haidian/pg%d/#contentList/" % i)
    for i in range(1, 101):
        start_urls.append("https://bj.lianjia.com/zufang/fengtai/pg%d/#contentList/" % i)
    for i in range(1, 35):
        start_urls.append("https://bj.lianjia.com/zufang/shijingshan/pg%d/#contentList/" % i)
    for i in range(1, 101):
        start_urls.append("https://bj.lianjia.com/zufang/haidian/pg%d/#contentList/" % i)
    for i in range(1, 63):
        start_urls.append("https://bj.lianjia.com/zufang/tongzhou/pg%d/#contentList/" % i)
    for i in range(1, 67):
        start_urls.append("https://bj.lianjia.com/zufang/changping/pg%d/#contentList/" % i)
    for i in range(1, 59):
        start_urls.append("https://bj.lianjia.com/zufang/daxing/pg%d/#contentList/" % i)
    for i in range(1, 14):
        start_urls.append("https://bj.lianjia.com/zufang/yizhuangkaifaqu/pg%d/#contentList/" % i)
    for i in range(1, 54):
        start_urls.append("https://bj.lianjia.com/zufang/shunyi/pg%d/#contentList/" % i)
    for i in range(1, 24):
        start_urls.append("https://bj.lianjia.com/zufang/fangshan/pg%d/#contentList/" % i)
    for i in range(1, 16):
        start_urls.append("https://bj.lianjia.com/zufang/mentougou/pg%d/#contentList/" % i)
    for i in range(1, 5):
        start_urls.append("https://bj.lianjia.com/zufang/huairou/pg%d/#contentList/" % i)
    for i in range(1, 7):
        start_urls.append("https://bj.lianjia.com/zufang/miyun/pg%d/#contentList/" % i)

    def parse(self, response):
        item = RentItem()
        for each in response.xpath('//*[@class="content__list--item"]'):
            name = each.xpath('.//div/p[1]/a/text()').extract()[0].strip('\n')
            item['name'] = name.strip()
            item['type'] = item['name'].split(" ")[1]
            item['location_1'] = each.xpath('.//div/p[2]/a[1]/text()').extract()[0]
            item['location_2'] = each.xpath('.//div/p[2]/a[2]/text()').extract()[0]
            item['forward'] = item['name'].split(" ")[2]
            area = each.xpath('.//div/p[2]/text()').extract()[4].replace("\n", "")
            item['area'] = area.replace(" ", "")
            item['price'] = each.xpath('.//div/span/em/text()').extract()[0]
            yield item


class RentSpiderSH(scrapy.spiders.Spider):
    name = "Rent_SH"
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {'test1.pipelines.RentHouseSH': 200}
    }
    for i in range(1, 88):
        start_urls.append("https://sh.lianjia.com/zufang/jingan/pg%d/#contentList/" % i)
    for i in range(1, 80):
        start_urls.append("https://sh.lianjia.com/zufang/xuhui/pg%d/#contentList/" % i)
    for i in range(1, 46):
        start_urls.append("https://sh.lianjia.com/zufang/huangpu/pg%d/#contentList/" % i)
    for i in range(1, 63):
        start_urls.append("https://sh.lianjia.com/zufang/changning/pg%d/#contentList/" % i)
    for i in range(1, 64):
        start_urls.append("https://sh.lianjia.com/zufang/putuo/pg%d/#contentList/" % i)
    for i in range(1, 101):
        start_urls.append("https://sh.lianjia.com/zufang/pudong/pg%dl0l2l3/#contentList/" % i)
    for i in range(1, 98):
        start_urls.append("https://sh.lianjia.com/zufang/pudong/pg%dl1/#contentList/" % i)
    for i in range(1, 87):
        start_urls.append("https://sh.lianjia.com/zufang/baoshan/pg%d/#contentList/" % i)
    for i in range(1, 41):
        start_urls.append("https://sh.lianjia.com/zufang/hongkou/pg%d/#contentList/" % i)
    for i in range(1, 59):
        start_urls.append("https://sh.lianjia.com/zufang/yangpu/pg%d/#contentList/" % i)
    for i in range(1, 101):
        start_urls.append("https://sh.lianjia.com/zufang/minhang/pg%d/#contentList/" % i)
    for i in range(1, 4):
        start_urls.append("https://sh.lianjia.com/zufang/jinshan/pg%d/#contentList/" % i)
    for i in range(1, 42):
        start_urls.append("https://sh.lianjia.com/zufang/jiading/pg%d/#contentList/" % i)
    for i in range(1, 88):
        start_urls.append("https://sh.lianjia.com/zufang/jingan/pg%d/#contentList/" % i)
    start_urls.append("https://sh.lianjia.com/zufang/chongming/")
    for i in range(1, 17):
        start_urls.append("https://sh.lianjia.com/zufang/fengxian/pg%d/#contentList/" % i)
    for i in range(1, 66):
        start_urls.append("https://sh.lianjia.com/zufang/songjiang/pg%d/#contentList/" % i)
    for i in range(1, 48):
        start_urls.append("https://sh.lianjia.com/zufang/qingpu/pg%d/#contentList/" % i)

    def parse(self, response):
        item = RentItem()
        for each in response.xpath('//*[@class="content__list--item"]'):
            name = each.xpath('.//div/p[1]/a/text()').extract()[0].strip('\n')
            item['name'] = name.strip()
            item['type'] = item['name'].split(" ")[1]
            item['location_1'] = each.xpath('.//div/p[2]/a[1]/text()').extract()[0]
            item['location_2'] = each.xpath('.//div/p[2]/a[2]/text()').extract()[0]
            item['forward'] = item['name'].split(" ")[2]
            area = each.xpath('.//div/p[2]/text()').extract()[4].replace("\n", "")
            item['area'] = area.replace(" ", "")
            item['price'] = each.xpath('.//div/span/em/text()').extract()[0]
            yield item


class RentSpiderSZ(scrapy.spiders.Spider):
    name = "Rent_SZ"
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {'test1.pipelines.RentHouseSZ': 300}
    }
    for i in range(1, 100):
        start_urls.append("https://sz.lianjia.com/zufang/luohuqu/pg%dl0l3/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://sz.lianjia.com/zufang/luohuqu/pg%dl1l2/#contentList" % i)
    for j in range(0, 3):
        for i in range(1, 101):
            start_urls.append("https://sz.lianjia.com/zufang/futianqu/pg%dl%d/#contentList" % (i, j))
    for i in range(1, 73):
        start_urls.append("https://sz.lianjia.com/zufang/futianqu/pg%dl3/#contentList" % i)
    for j in range(0, 4):
        for i in range(1, 79):
            start_urls.append("https://sz.lianjia.com/zufang/nanshanqu/pg%dl%d/#contentList" % (i, j))
    for i in range(1, 30):
        start_urls.append("https://sz.lianjia.com/zufang/yantianqu/pg%d/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://sz.lianjia.com/zufang/baoanqu/pg%dl0/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://sz.lianjia.com/zufang/baoanqu/pg%dl1l2l3/#contentList" % i)
    for i in range(1, 89):
        start_urls.append("https://sz.lianjia.com/zufang/longgangqu/pg%dl0/#contentList" % i)
        start_urls.append("https://sz.lianjia.com/zufang/longgangqu/pg%dl2/#contentList" % i)
        start_urls.append("https://sz.lianjia.com/zufang/longgangqu/pg%dl1l3/#contentList" % i)
    for i in range(1, 95):
        start_urls.append("https://sz.lianjia.com/zufang/longhuaqu/pg%dl1l2l3/#contentList" % i)
    for i in range(1, 78):
        start_urls.append("https://sz.lianjia.com/zufang/longhuaqu/pg%dl0rp1rp4rp5rp6rp7/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://sz.lianjia.com/zufang/longhuaqu/pg%dl0rp2/#contentList" % i)
        start_urls.append("https://sz.lianjia.com/zufang/longhuaqu/pg%dl0rp3/#contentList" % i)
    for i in range(1, 28):
        start_urls.append("https://sz.lianjia.com/zufang/guangmingqu/pg%d/#contentList" % i)
    for i in range(1, 20):
        start_urls.append("https://sz.lianjia.com/zufang/pingshanqu/pg%d/#contentList" % i)
    for i in range(1, 5):
        start_urls.append("https://sz.lianjia.com/zufang/dapengxinqu/pg%d/#contentList" % i)

    def parse(self, response):
        item = RentItem()
        for each in response.xpath('//*[@class="content__list--item"]'):
            flag = each.xpath('.//a[1]/@class').extract()[0]
            if flag == "link":
                continue
            name = each.xpath('.//div/p[1]/a/text()').extract()[0].strip('\n')
            item['name'] = name.strip()
            item['type'] = item['name'].split(" ")[1]
            item['location_1'] = each.xpath('.//div/p[2]/a[1]/text()').extract()[0]
            item['location_2'] = each.xpath('.//div/p[2]/a[2]/text()').extract()[0]
            item['forward'] = item['name'].split(" ")[2]
            area = each.xpath('.//div/p[2]/text()').extract()[4].replace("\n", "")
            item['area'] = area.replace(" ", "")
            item['price'] = each.xpath('.//div/span/em/text()').extract()[0]
            yield item


class RentSpiderGZ(scrapy.spiders.Spider):
    name = "Rent_GZ"
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {'test1.pipelines.RentHouseGZ': 400}
    }
    for i in range(1, 101):
        start_urls.append("https://gz.lianjia.com/zufang/tianhe/pg%dl0/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/tianhe/pg%dl1/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/tianhe/pg%dl2/#contentList" % i)
        if i <= 58:
            start_urls.append("https://gz.lianjia.com/zufang/tianhe/pg%dl3/#contentList" % i)
    for i in range(1, 99):
        start_urls.append("https://gz.lianjia.com/zufang/yuexiu/pg%dl0/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/yuexiu/pg%dl1/#contentList" % i)
        if i <= 65:
            start_urls.append("https://gz.lianjia.com/zufang/yuexiu/pg%dl2l3/#contentList" % i)
    for i in range(1, 65):
        start_urls.append("https://gz.lianjia.com/zufang/liwan/pg%dl0/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/liwan/pg%dl1/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/liwan/pg%dl2l3/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://gz.lianjia.com/zufang/haizhu/pg%dl0/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/haizhu/pg%dl1/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/haizhu/pg%dl2l3/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://gz.lianjia.com/zufang/panyu/pg%dl0/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/panyu/pg%dl1/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/panyu/pg%dl2/#contentList" % i)
        if i <= 70:
            start_urls.append("https://gz.lianjia.com/zufang/panyu/pg%dl3/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://gz.lianjia.com/zufang/baiyun/pg%dl0/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/baiyun/pg%dl1/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/baiyun/pg%dl2/#contentList" % i)
        if i <= 42:
            start_urls.append("https://gz.lianjia.com/zufang/baiyun/pg%dl3/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://gz.lianjia.com/zufang/huangpugz/pg%dl0l3/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/huangpugz/pg%dl2/#contentList" % i)
        if i <= 69:
            start_urls.append("https://gz.lianjia.com/zufang/huangpugz/pg%dl1/#contentList" % i)
    for i in range(1, 33):
        start_urls.append("https://gz.lianjia.com/zufang/conghua/pg%d/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://gz.lianjia.com/zufang/zengcheng/pg%dl1l3/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/zengcheng/pg%dl2/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://gz.lianjia.com/zufang/huadou/pg%dl0l1l2/#contentList" % i)
    for i in range(1, 101):
        start_urls.append("https://gz.lianjia.com/zufang/nansha/pg%dl0l1l3/#contentList" % i)
        start_urls.append("https://gz.lianjia.com/zufang/nansha/pg%dl2/#contentList" % i)

    def parse(self, response):
        item = RentItem()
        for each in response.xpath('//*[@class="content__list--item"]'):
            flag = each.xpath('.//a[1]/@class').extract()[0]
            if flag == "link":
                continue
            name = each.xpath('.//div/p[1]/a/text()').extract()[0].strip('\n')
            item['name'] = name.strip()
            item['type'] = item['name'].split(" ")[1]
            item['location_1'] = each.xpath('.//div/p[2]/a[1]/text()').extract()[0]
            item['location_2'] = each.xpath('.//div/p[2]/a[2]/text()').extract()[0]
            item['forward'] = item['name'].split(" ")[2]
            area = each.xpath('.//div/p[2]/text()').extract()[4].replace("\n", "")
            item['area'] = area.replace(" ", "")
            item['price'] = each.xpath('.//div/span/em/text()').extract()[0]
            yield item


class RentSpiderBT(scrapy.spiders.Spider):
    name = "Rent_BT"
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {'test1.pipelines.RentHouseBT': 500}
    }
    for i in range(1, 3):
        start_urls.append("https://baotou.lianjia.com/zufang/binhexinqu/pg%d/#contentList" % i)
    for i in range(1, 31):
        start_urls.append("https://baotou.lianjia.com/zufang/donghequ/pg%d/#contentList" % i)
    for i in range(1, 12):
        start_urls.append("https://baotou.lianjia.com/zufang/jiuyuanqu/pg%d/#contentList" % i)
    for i in range(1, 72):
        start_urls.append("https://baotou.lianjia.com/zufang/kundoulunqu/pg%d/#contentList" % i)
    for i in range(1, 53):
        start_urls.append("https://baotou.lianjia.com/zufang/qingshanqu/pg%d/#contentList" % i)
    for i in range(1, 6):
        start_urls.append("https://baotou.lianjia.com/zufang/xitugaoxinqu/pg%d/#contentList" % i)

    def parse(self, response):
        item = RentItem()
        for each in response.xpath('//*[@class="content__list--item"]'):
            name = each.xpath('.//div/p[1]/a/text()').extract()[0].strip('\n')
            item['name'] = name.strip()
            item['type'] = item['name'].split(" ")[1]
            item['location_1'] = each.xpath('.//div/p[2]/a[1]/text()').extract()[0]
            item['location_2'] = each.xpath('.//div/p[2]/a[2]/text()').extract()[0]
            item['forward'] = item['name'].split(" ")[2]
            area = each.xpath('.//div/p[2]/text()').extract()[4].replace("\n", "")
            item['area'] = area.replace(" ", "")
            item['price'] = each.xpath('.//div/span/em/text()').extract()[0]
            yield item
