import requests
from bs4 import BeautifulSoup
import sys

#get district number
district = sys.argv[1]

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '5426',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ASP.NET_SessionId=4xfa521x31weu1p0zlzibhzs; ASPSESSIONIDAGSDSBBC=KJLFCOEBFOBBFBALIFOCGLLO',
    'Host': 'www.opt-osfns.org',
    'Origin': 'https://www.opt-osfns.org',
    'Referer': 'https://www.opt-osfns.org/schoolfoodny/meals/default.aspx',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

data = {
    'ToolkitScriptManager1_HiddenField': ';;AjaxControlToolkit, Version=3.5.40412.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:47d532b1-93b1-4f26-a107-54e5292e1525:de1feab2:f2c8e708:720a52bf:f9cec9bc:589eaa30:698129cf:7a92f56c',
    '__EVENTTARGET': ' ',
    '__EVENTARGUMENT': ' ',
    '__LASTFOCUS': ' ',
    '__VIEWSTATE': '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',
    '__VIEWSTATEGENERATOR': '025A2AC0',
    '__VIEWSTATEENCRYPTED': ' ',
    '__EVENTVALIDATION': 'akeMF/0JgNik+L2VSPmhcIxXQd6VfknGCktfR4sjH8dAhlHCZcHXwV89gkXd6XFZ0pZPBGhL2t4iI1ZV/efLrmIeP3MucSSxbu+RN3GgOy+eixU+4JVr2xeZzB7hQSvn9ev62s8nJlf51zwhhxDnh/8qZODQ5tqHP0odqCmlNSDXssdeldAvWwBFCGAMtHfxsocJnvjD1paB0Q8Lra2wEWW2S42FViXWYKqeiR35VxtifswNw9g85N36ZT/0AS/mR8aEYVAl6GrDQpjFHfiLCOJeA++JeEdjUivA7/U32yJkHF0sR8+3+O191Mzyt8VbvFfnb/mKPQZ+dl5/SdYT/A2OTVrNyLrQPzNCR29/rn6NRH62Mor3YFhUIMGGKFbb61+gGqW5u3JJED6sIIoRlnpGfCTzmprMXJi5sVpo+WoHMMG9KkaGDL0tEqZr+4Vt+zTjami3wI+RSgOzs92oonL08BfK5aRLTHhvhuJ1sASZXi0uofESRcfTWno/TpL+uJIfi6Os2wjfNfBXpwSEDmsMy0QPzy87S5pvP46jNUnPKguuBzHbiA0iLMV2p3XJmxy695CvRta5fuDNq8g11imbOfr5eK3VhB17z5pZyguX9NHCCmGzLH/2qoe8YDmWiQ5GVhD2BiYTza0zOXjQNQUB5T2zYf846YBt28qKS1CUDkCpUR8uqMOHjfQmNt1ZRyJAoCo4H9VGFEZY/2h7S/co7QFvWfVcsSCE4RdNjKTKdcmwnlpdDVFHpb3G3VgXYwC3XQ5oIWCWc+wQhzpl74nXAdiPK3R7+QXz6VpuzhMF07nri4o5nYQG7JPfZimmQMdNOCBK72PYPlrIJ62+2wpy+tLvapUQogatyWj7US1chPObU+tKaOwK8Zb4y/vJrwenglIiRqrBMPKUVs4dk6TX+w8WFur7NEk59wREb+BPBWhlM9a2nmaRm3F1/tkvQr4iyO3mGNyGpoG0sy77zmYbRCdzT1O0rrvIX7tU9ko1o1ujLK/pydTKUoGd7eogx1XDbGCSKdbgwo1IOckgddTV0btMmuVg7Fy8iYMGFcqwsuuIwDTwJZLE9lAt1oTCTuBnwumiRZD1COQNVncMPUtEnkq80ttowWDQtvGiRmhbBpsELssVCgVh+so/ubx5ar3P9KdloWs9TW0H8hlF8C6mQcv0kPJabuF94oPNeovOsfBDtugbDQHIikUUrJ2QGswgLiWaS4mxm9rS+WYiM32QnXGoM4S1i/3BqvJ5wzgfxgPQHY4udSuALZWAKWESLdaDkDcoR2zPl931TfyYSjKlfcQqH55lAEzFW3z+M4FOArZyRbqHfiD0tDk=',
    'ddlBoro': '0',
    'ddlDistrict': district,
    'txtSchool': '',
    'ddlMile': '0',
    'btnGo': 'Search',
    'ddlRecords': '20',
    'hiddenInputToUpdateATBuffer_CommonToolkitScripts': '1'
}

# Get the page
# use .post
# send the data
url = "https://www.opt-osfns.org/schoolfoodny/meals/default.aspx"
response = requests.post(url, data=data)
doc = BeautifulSoup(response.text, 'html.parser')

# Grab all of the rows
row_tags = doc.find_all('tr')

# Let's print the first 5
for row in row_tags:
    print(row.text.strip())