#文档类型：说明文件
#文档名称：selenium3+python3环境搭建
"""
步骤一：安装python3
	路径：E:\Users\mazhicheng\AppData\Local\Programs\Python\Python36
	环境变量：E:\\Users\\mazhicheng\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\;
			  E:\\Users\\mazhicheng\\AppData\\Local\\Programs\\Python\\Python36\\;
步骤二：使用pip安装selenium（pip的功能是安装python标准库）
	$:pip install selenium
	路径：E:\Users\mazhicheng\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium
步骤三：确定使用的浏览器的webdriver（安装chrome）	
	放置webdriver在python的安装目录下E:\Users\mazhicheng\AppData\Local\Programs\Python\Python36\chromedriver.exe
步骤四：测试环境搭建结果
		from selenium import webdriver
		driver = webdriver.Chrome()
		driver.get('https://www.baidu.com/')
"""

"""
技巧：

1. firepath安装	
	浏览器中插入：https://addons.mozilla.org/en-us/firefox/addon/firepath/

"""