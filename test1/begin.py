from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from test1.spiders.spider import RentSpiderBJ
from test1.spiders.spider import RentSpiderSH
from test1.spiders.spider import RentSpiderSZ
from test1.spiders.spider import RentSpiderGZ
from test1.spiders.spider import RentSpiderBT
from twisted.internet import reactor

configure_logging()
runner = CrawlerRunner()
runner.crawl(RentSpiderBJ)
runner.crawl(RentSpiderSH)
runner.crawl(RentSpiderSZ)
runner.crawl(RentSpiderGZ)
runner.crawl(RentSpiderBT)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
