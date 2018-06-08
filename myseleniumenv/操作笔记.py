#操作笔记

"""

获取元素
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

元素定位子元素
username =browser.find_element_by_xpath("//input[@name='username']")
clear_button = browser.find_element_by_xpath("//form[@id='loginForm']/input[4]")

断言常用的有
assertLocation（判断当前是在正确的页面）、
assertTitle（检查当前页面的 title 是否正确）、
assertValue（检查 input 的值， checkbox 或 radio，有值为”on”无为”off”）、
assertSelected（检查 select 的下拉菜单中选中是否正确）、
assertSelectedOptions（检查下拉菜单中的选项的是否正确）、
assertText（检查指定元素的文本）、
assertTextPresent（检查在当前给用户显示的页面上是否有出现指定的文本）、
assertTextNotPresent（检查在当前给用户显示的页面上是否没有出现指定的文本）、
assertAttribute（检查当前指定元素的属性的值）、
assertTable（检查 table 里的某个 cell 中的值）、
assertEditable（检查指定的 input 是否可以编辑）、
assertNotEditable（检查指定的 input 是否不可以编辑）、
assertAlert（检查是否有产生带指定 message 的 alert 对话框）、
verifyTitle （检查预期的页面标题）
verifyTextPresent （验证预期的文本是否在页面上的某个位置）
verifyElementPresent（验证预期的UI元素，它的HTML标签的定义，是否在当前网页上）
verifyText（核实预期的文本和相应的HTML标签是否都存在于页面上）
verifyTable（验证表的预期内容）
waitForPageToLoad（暂停执行，直到预期的新的页面加载）
waitForElementPresent （等待检验某元素的存在。为真时，则执行。)

异常类型
AssertionError:assert语句失败
AttributeError:试图访问一个对象没有的属性
IOError:输入输出异常，基本是无法打开文件
ImportError:无法引入模块或者包，基本是路径问题
IndentationError:语法错误，代码没有正确的对齐
IndexError:下标索引超出序列边界
KeyError：试图访问字典里不存在的键
KeyboadrInterrupt:Ctrl+c被按下
NameError:使用一个还未赋值对象的变量
SyntaxError:python代码逻辑语法错误，不能执行
TypeError:传入的对象类型与要求不符
UnboundLocalError:试图访问一个还未设置的全局变量，基本上是由于另有一个同名的全局变量，导致你以为在访问
ValueError:传入一个不被期望的值，即使类型正确

unitTest框架中的断言
assertEqual(a,b)
assertNotEqual(a,b)
assertTrue(x)
assertFalse(x)
assertIs(a,b)
assertIsNot(a,b)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a,b)
assertNotIn(a,b)
assertIsInstance(a,b)
assertNotIsInstance(a,b)


"""

