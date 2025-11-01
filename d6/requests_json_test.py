import requests
import json

#测试API连接
def test_api():
    response = requests.get("https://api.github.com")
    print(f"状态码：{response.status_code}")
    print(f'响应头：{response.headers['content-type']}')

    if response.status_code == 200:
        print("✅ API连接成功！")
    else:
        print("❌ API连接失败！")

#获取并解析公开API数据
def get_weather_data():
    #使用公开天气API (无需密钥)
    url = "http://www.weather.com.cn/data/sk/101010100.html"

    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        data = response.json()

        print("=== 实时天气数据 ===")
        print(f"城市：{data['weatherinfo']['city']}")
        print(f"温度：{data['weatherinfo']['temp']}°C")
    except Exception as e:
        print(f"获取数据失败：{e}")

# 错误处理与超时
def robust_api_call():
    try:
        #设置超时防止卡死
        response = requests.get("https://httpbin.org/delay/2",timeout=5)
        print(f"请求成功：{response.status_code}")
    except requests.exceptions.Timeout:
        print("⚠️ 请求超时！")
    except requests.exceptions.ConnectionError:
        print("⚠️ 网络连接错误！")
    except Exception as e:
        print(f"⚠️ 其他错误: {e}")

test_api()
get_weather_data()
robust_api_call()


