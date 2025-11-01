# import 直接导入
import math

#理解 if __name__ == '__main__' 作用
#这个判断让Python文件知道自己是被'直接启动'还是被'当作工具包调用'
#核心价值：
#代码复用：既可以独立运行，也可以作为模块被其他程序使用
#测试方便：在文件内写测试代码，不影响导入使用
#结构清晰：明确区分"定义"和"执行"

#在Python中，安装第三方模块，是通过包管理工具pip完成的
#第三方库都会在Python官方的pypi.python.org网站注册

import datetime

def get_current_time():
    return datetime.datetime.now()

if __name__ == '__main__':
    print(f'当地时间：{get_current_time()}')
    print('作战进行中！')
    
get_current_time()