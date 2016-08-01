import os
import json
import urllib.request
from pprint import pprint

url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?symbol="
quote = input("Enter a correct stock quote: ")
url = url + quote + "&callback=a"

data = urllib.request.urlopen(url).read()
formatted = data.decode('utf-8')
#print(formatted)

test_string_format = formatted[1:]
final_string_format = test_string_format.strip('(')
final_string_format=final_string_format.rstrip(')')
#print(final_string_format)

data_json = json.loads(final_string_format)
pprint(data_json)