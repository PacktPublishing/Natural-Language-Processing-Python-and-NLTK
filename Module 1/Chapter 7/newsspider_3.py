from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import NewsItem

class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['news.google.com']
    start_urls = ['https://news.google.com']

    rules = (
        # Extract links matching cnn.com
        Rule(SgmlLinkExtractor(allow=('cnn.com', ), deny=(http://edition.cnn.com/', ))),
       # Extract links matching 'news.google.com'
       Rule(SgmlLinkExtractor(allow=('news.google.com', )), callback='parse_news_item'),
    )
    def parse_news_item(self, response):
        sel = Selector(response)
        item = NewsItem()
        item['title'] = sel.xpath('//title/text()').extract()
        item[topic] = sel.xpath('/div[@class="topic"]').extract()
        item['desc'] = sel.xpath('//td//text()').extract()
        return item
