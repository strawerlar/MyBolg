#导入所需要的工具类
import urllib.request
import urllib.parse
import json
import time

#定义函数
def  get_html(url):
    result = []
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')

    #28
    time1 = html.find('<span class="uiVideo__time">')

    if time1 == -1:
        return -1
    while True:
        if time1 == -1:
            break
        time2 = html.find('</span>',time1)
        time = html[time1+28:time2]
        #33
        title1 = html.find('class="uiVideo__subtitle" title="',time1)
        title2 = html.find('">',title1)
        title  = html[title1+33:title2]
        #10
        count1 = html.find('data-num="',time1)
        count2 = html.find('">',count1)
        count  = html[count1+10:count2]

        record = 'time:'+time+' count:'+count+' title:'+title + '\n'
        result.extend(record)
         
        time1 = html.find('<span class="uiVideo__time">',time1+1)
        time2 = html.find('</span>',time1)
    return result
    
def get_url(url,page):
    if page == 1:
        return url
    else:
        return url[:-5]+'_'+ str(page) + url[-5:]

def save(records):
    with open('records.txt','w') as f:
        for each in records:
            f.write(each)

if __name__=="__main__": 
    page = 2
    url = 'http://video.duowan.com/lol/new.html'
    records = []
    for i in range(200):
        print('cawaling '+ str(i) +'...')
        temp = get_url(url,page=i+1)
        r = get_html(temp)
        if r == -1:
            break
        else:
            records.extend(r)
        time.sleep(1)
    save(records)
    
