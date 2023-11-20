#模块(module)其实就是 py 文件，里面定义了一些函数、类、变量等
#包(package)是多个模块的聚合体形成的文件夹，里面可以是多个 py 文件，也可以嵌套文件夹
# 导入模块
import hello
# 现在可以调用模块里包含的函数了
hello.sayhello()

## 直接导入方法
from hello import sayhello
sayhello()

## 导入所有方法
from hello import *
sayhello()
world()

print("测试包的使用")

import cal.calculator
print(cal.calculator.add(1,2))


from cal import calculator
# 使用包的模块的方法
print(calculator.multiply(3,6))
print(calculator.reduce(3,1))
