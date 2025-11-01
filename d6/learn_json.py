import json

#JSON 实例
{
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
    { "name":"google" , "url":"www.google.com" }, 
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}



#什么是 JSON ？
'''
JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
JSON 是轻量级的文本数据交换格式
JSON 独立于语言：JSON 使用 Javascript语法来描述数据对象，
但是 JSON 仍然独立于语言和平台。
JSON 解析器和 JSON 库支持许多不同的编程语言。 
目前非常多的动态（PHP，JSP，.NET）编程语言都支持 JSON
JSON 具有自我描述性，更易理解
'''

#JSON - 转换为 JavaScript 对象
'''
JSON 文本格式在语法上与创建 JavaScript 对象的代码相同。
由于这种相似性，无需解析器，
JavaScript 程序能够使用内建的 eval() 函数，
用 JSON 数据来生成原生的 JavaScript 对象。
'''
