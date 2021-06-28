#!/usr/bin/python

import sys
from urllib.request import Request, urlopen

if len(sys.argv) < 2:
    print('Zip Code must be used as arugemnt when executing programing')
    sys.exit()
    
zipcode = sys.argv[1]

def DataFilter(ident, offset, stop):
    position = content.find(ident)
    data = content[position + offset:position + offset + 50]

    result = ''

    for x in range(len(data)):
        testData = data[x:x + 1]
        if testData == stop:
            break
        result += data[x:x + 1]
    
    return result


req = Request('https://www.google.com/search?q=weather+' + zipcode)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.3')
content = urlopen(req).read().decode("utf8")

temperature = DataFilter('id="wob_tm"', 35, '<')
humitity = DataFilter('id="wob_hm"', 12, '%')
wind = DataFilter('id="wob_ws"', 12, ' ')
rain = DataFilter('id="wob_pp"', 12, '%')
sky = DataFilter('id="wob_dc"', 12, '<')
location = DataFilter('id="wob_loc"', 13, '<')
time = DataFilter('id="wob_dts"', 13, '<')
 
finalData = [temperature, humitity, wind, rain, sky, location, time]

for x in finalData:
    print(x)
