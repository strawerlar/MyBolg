
# Python 学习测试文档

# 数据结构
## 元组（1,2,3） 元组不可变

## 列表  [1,2,3]    长度可变

## 字典  {1：‘张三’，‘zhangsan’:2}


```python
girls = ['athena','lulu','lux']
boys = ['lar','atom']

#数据生成式
s = [b + '+' + g for b in boys for g in girls if b[0]==g[0] ]
print(s)
```

    ['lar+lulu', 'lar+lux', 'atom+athena']
    

# 字典 以{} 的方式 包含key:value 的形式  跟JSON格式一样啊


```python
# 字典的创建
dictionary = {1:'zhangsan'}
dic = dictionary
dic
```




    {1: 'zhangsan'}




```python
# 字典添加元素    什么都不用管 直接加就是了
dic[2] = 'nihao'
dic
```




    {1: 'zhangsan', 2: 'nihao'}




```python
# 赋新值 直接覆盖
dic[2] = 'hello world'
dic
```




    {1: 'zhangsan', 2: 'hello world'}




```python
print('dic[2]:'+dic[2])  
print('dic[3]:'+dic[3]) # 查找没有的键值 会报错
```

    dic[2]:hello world
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-51-9c9beb1fcfed> in <module>()
          1 print('dic[2]:'+dic[2])
    ----> 2 print('dic[3]:'+dic[3])
    

    KeyError: 3



```python
dd = dic[3]   # 没有键值直接报错  不能返回空
dd
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-52-197873b0c5d3> in <module>()
    ----> 1 dd = dic[3]
          2 dd
    

    KeyError: 3



```python
# python 3 xrange 与 range 融合了  
# 写语句块的时候  要加 “：” 注意缩进
# print是函数 不再是语句 要用函数的方式调用，print(str,end='') 第二个参数设置以什么为结尾  默认是换行
for i in range(255):
    print(chr(i),end=' ')
```

              	 
                         ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~                                    ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ ­ ® ¯ ° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿ À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ 


```python
# 列表写斐波那契数列
# python的简介 真是令人发指  其中 fib[-1] 代表最后一个元素  负数索引 
# append() 函数在 扩展列表 添加数据  会修改列表
fib = [1,2]
for i in range(20):
    fib.append(fib[-2] + fib[-1])
```


```python
# append() 会把传入的参数作为一个元素扩展到目标中
a = [1,2,3]
b = [4,5,6]
a.append(b)
print(a)
print(b)
```

    [1, 2, 3, [4, 5, 6]]
    [4, 5, 6]
    


```python
# extend() 是扩展表  用d 扩展c表
c = [1,2,3]
d = [4,5,6]
c.extend(d)
print(c)
print(d)
```

    [1, 2, 3, 4, 5, 6]
    [4, 5, 6]
    


```python
# input()  Python 3 好像没有 raw_input了
name = input('input your name:')
print('nihao '+ name)
```

    input your name:张三
    nihao 张三
    


```python
# 导入包
from math import sqrt
```


```python
x = 4
xx = sqrt(x)
xx
```




    2.0




```python
x = sqrt  # 这样 x  就是 sqrt函数的引用 因为Python中是弱类型的  变量可以引用任何东西 包括函数
result = x(16)
result
```




    4.0




```python
#判断一个变量是不是可以执行的函数 
print(callable(x))       # x 现在指向的是sqrt函数  所以可以执行
print(callable(result))  # result指向的是4.0 不是函数 所以错误
```

    True
    False
    


```python

def hello(name):#创建函数      def 函数名（参数列表）：   ！！！！！！！！记得冒号！！！！！！！！
    '在这写函数的文档  通过__doc__可以查看到'
    print ("hello "+ name)   # 每行结束不需要添加分号  Python中的行物理行 就是逻辑行
hello("zhangsan")
hello("lisi")
```

    hello zhangsan
    hello lisi
    


```python
# 定义函数前写了注释的话  里面的函数文档就会被屏蔽掉了
print(hello.__doc__)
```

    在这写函数的文档  通过__doc__可以查看到
    


```python
help(hello)
```

    Help on function hello in module __main__:
    
    hello(name)
        在这写函数的文档  通过__doc__可以查看到
    
    


```python
#列表切片    包含做边界 不包含右边界  [ )
a = [1,2,3,4,5,6,7,8,9,0]
b = a[0:1]
print(b)# 切片操作
b = a[0:]
print(b)# 切片操作
b = a[:5]
print(b)# 切片操作
b = a[3:-1]
print(b)# 切片操作
```

    [1]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    [1, 2, 3, 4, 5]
    [4, 5, 6, 7, 8, 9]
    


```python
# 字典的玩法
name = {}
name[1] = {}
name[2] = {}
name
```




    {1: {}, 2: {}}




```python
# name[key] = value
name['zhang'] = 'san'
name
```




    {1: {}, 2: {}, 'zhang': 'san'}




```python
#name1 love name2
def love(name1='lar' ,name2='athena'):
    print(name1 + ' love ' + name2)
love('zhangsan','lisi')
love('athena','lar')
love(name2='athena',name1='lar')# 通过参数名赋值 可以无视参数顺序
love()#调用函数的默认值
love('mx')
love(name2='money')
```

    zhangsan love lisi
    athena love lar
    lar love athena
    lar love athena
    mx love athena
    lar love money
    


```python
#收集参数  * 收集多余的没有关键字的函数  **收集多余的 有关键字的函数  太OP了 函数随便玩？
def fun001(name,*par,**keys):
    print(name)
    print(par)
    print(keys)
fun001('zhangsan',1,2,3,4,5,6,name2='hahah',key='what',num=3)
```

    zhangsan
    (1, 2, 3, 4, 5, 6)
    {'key': 'what', 'num': 3, 'name2': 'hahah'}
    


```python

```
