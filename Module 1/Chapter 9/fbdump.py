import facebook
import json
fo = open("fdump.txt",'w')
ACCESS_TOKEN = 'XXXXXXXXXXX' # https://developers.facebook.com/tools/
explorer
fb = facebook.GraphAPI(ACCESS_TOKEN)
compeny_page = "326249424068240"
content = fb.get_object(compeny_page)
fo.write(json.dumps(content))