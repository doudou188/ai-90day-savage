#requests
#响应信息
#requests方法
#设置请求头
#附加请求参数

import requests
#发送请求
x = requests.get('https://www.runoob.com/')
#返回网页内容
#print(x.text)

#每次调用 requests 请求之后，会返回一个 response 对象，
# 该对象包含了具体的响应信息，如状态码、响应头、响应内容等：
print(x.status_code) #获取响应状态码(x即为response对象)
print(x.headers)   # 响应头
#print(x.content)    #响应内容
print(x.reason)     #响应状态的描述
print(x.apparent_encoding) #返回编码
x = requests.get('https://www.runoob.com/try/ajax/json_demo.json')
print(x.json())


#响应信息如下：
'''
apparent_encoding	编码方式
close()	关闭与服务器的连接
content	返回响应的内容，以字节为单位
cookies	返回一个 CookieJar 对象，包含了从服务器发回的 cookie
elapsed	返回一个 timedelta 对象，包含了从发送请求到响应到达之间经过的时间量，可以用于测试响应速度。比如 r.elapsed.microseconds 表示响应到达需要多少微秒。
encoding	解码 r.text 的编码方式
headers	返回响应头，字典格式
history	返回包含请求历史的响应对象列表（url）
is_permanent_redirect	如果响应是永久重定向的 url，则返回 True，否则返回 False
is_redirect	如果响应被重定向，则返回 True，否则返回 False
iter_content()	迭代响应
iter_lines()	迭代响应的行
json()	返回结果的 JSON 对象 (结果需要以 JSON 格式编写的，否则会引发错误)
links	返回响应的解析头链接
next	返回重定向链中下一个请求的 PreparedRequest 对象
ok	检查 "status_code" 的值，如果小于400，则返回 True，如果不小于 400，则返回 False
raise_for_status()	如果发生错误，方法返回一个 HTTPError 对象
reason	响应状态的描述，比如 "Not Found" 或 "OK"
request	返回请求此响应的请求对象
status_code	返回 http 的状态码，比如 404 和 200（200 是 OK，404 是 Not Found）
text	返回响应的内容，unicode 类型数据
url	返回响应的 URL
'''

#使用 requests.request() 发送 get 请求
x = requests.request('get','https://www.runoob.com')
print(x.status_code)
#requests 方法如下:
'''
delete(url, args)	发送 DELETE 请求到指定 url
get(url, params, args)	发送 GET 请求到指定 url
head(url, args)	发送 HEAD 请求到指定 url
patch(url, data, args)	发送 PATCH 请求到指定 url
post(url, data, json, args)	发送 POST 请求到指定 url
put(url, data, args)	发送 PUT 请求到指定 url
request(method, url, args)	向指定的 url 发送指定的请求方法
'''


kw = {'s':'python教程'}
#设置请求头：
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#params接收一个字典或字符串的查询参数，【字典类型自动转换为url编码，不需要urlencode（）】
response = requests.get("https://www.runoob.com/",params=kw,headers=headers)

print(response.status_code)
# 查看响应头部字符编码
print(response.encoding)
print(response.url)


#post() 方法可以发送 POST 请求到指定 url，一般格式如下：
#requests.post(url, data={key: value}, json={key: value}, args)
#url 请求 url。
#data 参数为要发送到指定 url 的字典、元组列表、字节或文件对象。
#json 参数为要发送到指定 url 的 JSON 对象。
#args 为其他参数，比如 cookies、headers、verify等。'''
x = requests.post('https://www.runoob.com/try/ajax/demo_post.php')
print(x.text)
#表单参数，参数名为 fname 和 lname
myobj = {'fname':'RUNOOB','Lname':'Boy'}
x = requests.post('https://www.runoob.com/try/ajax/demo_post2.php',data=myobj)
print(x.text)

'''
GET 和 POST 方法的比较：
后退按钮/刷新：GET 请求是无害的，而 POST 请求会重新提交数据。
书签：GET 请求可以被收藏为书签，POST 请求不能。
缓存：GET 请求可以被缓存，POST 请求不能。
编码类型：GET 请求使用 application/x-www-form-urlencoded，
POST 请求可以使用 application/x-www-form-urlencoded 或 multipart/form-data。
历史：GET 请求的参数保留在浏览器历史中，POST 请求的参数不会。
数据长度限制：GET 请求有长度限制，POST 请求没有。
数据类型限制：GET 请求只允许 ASCII 字符，POST 请求没有限制。
安全性：GET 请求的安全性较差，因为数据在 URL 中可见。POST 请求相对更安全。
'''

#附加请求参数
#发送请求我们可以在请求中附加额外的参数，例如请求头、查询参数、请求体等，例如：

headers = {'User-Agent': 'Mozilla/5.0'}  # 设置请求头
params = {'key1': 'value1', 'key2': 'value2'}  # 设置查询参数
data = {'username': 'example', 'password': '123456'}  # 设置请求体
response = requests.post('https://www.runoob.com', headers=headers, params=params, data=data)
#上述代码发送一个 POST 请求，并附加了请求头、查询参数和请求体。
#除了基本的 GET 和 POST 请求外，requests 还支持其他 HTTP 方法，如 PUT、DELETE、HEAD、OPTIONS 等
