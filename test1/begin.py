from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from test1.spiders.spider import NewSpider
from test1.spiders.spider import SecondSpider
from twisted.internet import reactor

configure_logging()
runner = CrawlerRunner()
runner.crawl(NewSpider)
runner.crawl(SecondSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
