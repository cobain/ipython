
# -*- coding:utf-8 -*-
import requests,re
o = open('data.txt','a')
e = open('error.txt','a')
baseUrl = 'http://www.iluohe.com/'
r = requests.get('http://www.iluohe.com/all.shtml',)
links = re.findall('<a href="(city/.*?/.*?)" target',r.content.decode("gbk").encode("utf-8"))
for link in links:
    link = baseUrl+link
    cityData = requests.get(link)
    if cityData.status_code >= 300 :
        e.writelines(link+"\n")
    else:
        cityData = cityData.content.decode("gbk").encode("utf-8")
        provinceTemp = re.findall('<div class="NameSzu"><a href=".*?">(.*?)</a></div>',cityData)
        if provinceTemp:
            province = provinceTemp[0]
            city = re.findall('<meta name="description" content="(.*?)共有',cityData)[0]
            tempData = re.findall('<div class="ab_menu.*?</span>(.*?) \(.*?</div>.*?<ul>(.*?)</ul>',cityData)
            for temp in tempData:
                carrier = temp[0]
                numbers = re.findall('">(.*?)</a></li>',temp[1])
                for number in numbers:
                    text = number + "," + carrier + "," + city + "," + province
                    o.writelines(text)
                    o.writelines('\n')
        else:
            e.writelines(link+"\n")
o.close()
print "over!"