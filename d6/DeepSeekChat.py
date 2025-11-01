import requests
import json
import os

class DeepSeekChat:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    def send_message(self, message):
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system",
                 "content": "你是一个严厉的编程教练,用血腥语言激励学员学习AI开发"
                 },
                 {
                     "role": "user",
                     "content": message
                 }
            ],
            "temperature": 0.7
        }
        try:
            response = requests.post(self.api_url,headers=self.headers,json=data,timeout=10)
            response.raise_for_status()#检查HTTP错误

            result = response.json()
            return result['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            return f"API请求失败：{e}"
        except KeyError:
            return "解析响应数据失败"
        
    def chat_loop(self):
        print("🔥 DeepSeek教练已上线！输入'quit'退出")
        print("-"*50)

        while True:
            user_input = input("你问：")
            if user_input.lower() == 'quit':
                print("滚去写代码！！！")
                break

            answer=self.send_message(user_input)
            print(f"教练：{answer}")
            print("-" * 50)

print("The value of __name__ is:", __name__)
# 使用你的实际API密钥
if __name__ == "__main__":

    API_KEY = "你的DeepSeek_API密钥"
    #API_KEY = "" #真实密钥

    if API_KEY == "你的DeepSeek_API密钥":
        print("❌ 请先设置你的API密钥！")
    else:
        chat = DeepSeekChat(API_KEY)
        
        chat.chat_loop()
