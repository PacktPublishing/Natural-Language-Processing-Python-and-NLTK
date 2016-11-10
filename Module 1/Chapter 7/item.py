from scrapy.item import Item, Field
class NewsItem(Item):
    title = Field()
    link = Field()
    desc = Field()
