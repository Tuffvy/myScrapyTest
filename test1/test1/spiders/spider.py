import scrapy
from test1.items import NewItem
from test1.items import SecondItem


class NewSpider(scrapy.spiders.Spider):
    name = "lianjiaNew"
    start_urls = ["https://bj.fang.lianjia.com/loupan/pg3/"]
    custom_settings = {
        'ITEM_PIPELINES': {'test1.pipelines.NewHouse': 300}
    }

    def parse(self, response):
        item = NewItem()
        for each in response.xpath('//*[@class="resblock-list post_ulog_exposure_scroll has-results"]'):
            item['name'] = each.xpath('.//a[@class="name "]/text()').extract()
            item['type'] = each.xpath('.//span[@class="resblock-type"]/text()').extract()
            item['location'] = each.xpath('.//div[@class="resblock-location"]/span/text()').extract()+each.xpath('.//div[@class="resblock-location"]/a/text()').extract()
            item['houseType'] = each.xpath('.//a[@class="resblock-room"]/span/text()').extract()
            item['area'] = each.xpath('.//div[@class="resblock-area"]/span/text()').extract()
            item['unitPrice'] = each.xpath('.//div[@class="main-price"]/span/text()').extract()
            item['unitPrice'][1] = item['unitPrice'][1].replace(u'\xa0', '')
            item['totalPrice'] = each.xpath('.//div[@class="second"]/text()').extract()
            yield item

        for i in range(4, 8):
            url = "https://bj.fang.lianjia.com/loupan/pg%d/" % i
            yield scrapy.Request(url, callback=self.parse)


class SecondSpider(scrapy.spiders.Spider):
    name = "lianjiaOld"
    start_urls = ["https://bj.lianjia.com/ershoufang/pg3/"]
    custom_settings = {
        'ITEM_PIPELINES': {'test1.pipelines.SecondHouse': 400}
    }

    def parse(self, response):
        item = SecondItem()
        for each in response.xpath('//*[@class="clear LOGVIEWDATA LOGCLICKDATA"]'):
            item['name'] = each.xpath('.//div[@class="title"]/a/text()').extract()
            item['location'] = each.xpath('.//div[@class="positionInfo"]//a/text()').extract()
            item['houseType'] = each.xpath('.//div[@class="houseInfo"]/text()').extract()[0].split(" | ")[0]
            item['area'] = each.xpath('.//div[@class="houseInfo"]/text()').extract()[0].split(" | ")[1]
            item['unitPrice'] = each.xpath('.//div[@class="unitPrice"]/span/text()').extract()
            item['totalPrice'] = each.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()').extract()
            yield item

        for i in range(4, 8):
            url = "https://bj.lianjia.com/ershoufang/pg%d/" % i
            yield scrapy.Request(url, callback=self.parse)