from scrapy.contrib.spiders import SitemapSpider
class MySpider(SitemapSpider):
    sitemap_URLss = ['http://www.example.com/sitemap.xml']
    sitemap_rules = [('/electronics/', 'parse_electronics'), ('/apparel/', 'parse_apparel'),] 
    def 'parse_electronics'(self, response):
    	# you need to create an item for electronics,
		return 
    def 'parse_apparel'(self, response):
        #you need to create an item for apparel
	  	return 