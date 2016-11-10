from scrapy.exceptions import Item
class CleanPipeline(object):
    def process_item(self, item, spider):
        if item['desc']:
            item['desc'] = item['desc'].strip().lower().replace('#$','')
            return item
#We need to derive the age from DOB. We used Python's date functions to achieve this:

from scrapy.exceptions import Item
import datetime
import datetime
class AgePipeline(object):
    def process_item(self, item, spider):
        if item['DOB']:
            item['Age'] = (datetime.datetime.strptime(item['DOB'], '%d-%m-%y').date()-datetime.datetime.strptime('currentdate, '%d-%m-%y').date()).days/365
            return item

#We also need to remove the duplicates. Python has the set() data structure that only contains unique values:
from scrapy import signals
from scrapy.exceptions import Item
class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()
    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
#Let's finally write the item in the JSON file:
import json
class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.txt', 'wb')
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item