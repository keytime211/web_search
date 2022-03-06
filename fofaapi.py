import requests
import base64
import sys


fofa_email = r'fofa_email'
api_key = r'key'
api = r'https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}&size=1000'
# 搜索状态200 中国地区 子域名 
input_arg = 'status_code="200"&&country="CN"&&domain='+sys.argv[1]
input_host = base64.b64encode(arg.encode()).decode()
response = requests.get(api.format(fofa_email,api_key,input_host))
results = response.json()["results"]
print("共搜索到{}条记录！".format(len(results)))
# 获取各个字段
file_name = r"{}.txt".format(sys.argv[1])
f = open(file_name,"a")
for addr in results:
    host = ("host:"+addr[0]+"\n"+"ip:"+addr[1]+"\n"+"端口："+addr[2]+"\n\n")
    f.write(host)
f.close()
