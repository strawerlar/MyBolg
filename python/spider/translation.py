import urllib.request
import urllib.parse

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=dict2.index'
data = { }
data['i'] = 'i+love+you'
data['from'] = 'AUTO'
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1494416496191'
data['sign']='afce8748aa2d86d439371251880a83a4'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTON'
data['typoResult']='true'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
print(html)     
