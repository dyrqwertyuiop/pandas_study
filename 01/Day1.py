# print('hello world')

# print() 输出函数 ,让用户看到运行结果
# input() 输入函数 ,让用户手动输入数据  input()输出的值的数据类型为字符串
# my_first_bl = int(input('请输入您的姓:'))#str转换成int
# b = input('输入一个数字:')
# print(my_first_bl) #调用时调用的是函数的值
# print (b)
# print (my_first_bl+b)
# type() 显示数据类型 需要跟print()连用
# print (type(my_first_bl))
# str to int: int('str')
# str to float:float('str')
# str to bool:bool('str')
# print (bool('True'))
# print (type('True'))
# print (type(bool('True')))
# int to str:str(1)
# float to str:str(1.1)
# bool to str:str(True)
# 二进制转十进制：从右到左，第一位*2的0次方+第二位*2的一次方....
#格式化输出
# 输出 我叫...,今年...岁
# name = input('请输入您的姓名:')
# age = input('请输入您的年龄:')
# 第一种
# print('我叫',name+',今年',age,'岁',sep='%')
#第二种：使用占位符% %s格式化字符串
# print ('我叫%s,今年%s岁'%(name,age))
#第三种
# print ('我叫'+name+',今年'+age+'岁')
# 第四种 调用format函数
# print ('我叫{},今年{}岁'.format(name,age))
# 第五种
# print (f'我叫{name},今年{age}岁')
# print (f'我叫{name}\n今年{age}岁')#\n换行 #\t空格
# print (rf'我叫{name}\n今年{age}岁')#\n换行 #\t空格 #取消转义字符
# 字符串
# 组成：值(字符-元素)+索引
# 元素：组成整体的最小单位
#字符串的索引：从左到右，从0开始依次增加，最后一位是 -1
# a='12345678910'
# # 截取多个字符(左包又不包)
# # print (a[0:2])
# # print (a[:11])
# # print (a[:])#":"前不写 默认从头到尾
#
# # 截取多个不连续的字符
# # print (a[::2])#步长
# print (a[1::2])


# 张三,李四,王五,赵六,杜艳荣,田七,狗八
b='张三,李四,王五,赵六,杜艳荣,田七,狗八'
print (b[:13:3]+b[16::3])
