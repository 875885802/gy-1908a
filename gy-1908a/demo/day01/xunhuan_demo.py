# for循环
"""
for i in range（可以看成一个列表，但不是列表）（0，10）：
    代码块
"""
for i in range(1,100,2):
    print(i)
for i in range(1,100):
    if(i%2 ==1):
        print(i)
for i in range(100):
    if(i%6 ==0):
        continue
    print(i)
for i in range(99):
    if(i ==9):
      break
    print(i)


sum=0
for number in range(100):
    number = number+1
    sum = sum + number
    print(number)
print(sum)

g = 0
for i in range(0, 100):
    g = g + (i+1)
print(g)

# 求出1+2+3.。。+100和
s = 0
for i in range(1,101):
    s += i
print(s)

s = 1
for i in range (1,100):
    s = s *(i+1)
print(s)
# 求出100! 1*2*3*4....*100
s = 1
for i in range(1,101):
    s *= i
print(s)
# 求出100以内的质数
for i in range (2 ,100):
    print(i)
    for k in range (2 ,i) :
      if ( k % i == 0):
          break
# 99乘法表
for i in range (1,10):
    for k in range (1 , i+1):
        print(k,"X",i,"=",i*k,"\t",end ="")
    print()
# 冒泡排序
h = [90,63,5,54,20,6]
for i in range(len(h)-1,0,-1):
    for j in range(i):
        if ( h[j] > h[j+1] ):
            h[j] , h[j+1] = h[j+1] , h[j]
print(h)
a = 1
b = 2
print(a+b)
#方法定义
def jia_fa():
    a = 1
    b = 2
    print(a+b)
#方法定义
def jia_fa(a,b):
    print(a+b)
#方法调用
jia_fa(3,5)
jia_fa(66,75)
#无参数，有返回值的方法
def jian_fa():
    a = 7
    b = 5
    return a -b
c = jian_fa()
print(c)
#有参数，有返回值的方法
def jian_fa(a,b):
    return a - b
c = jian_fa(7,6)
print(c)
def aa (*args,**kwargs):
    print(args)
    #元祖里边，不指定的，
    print(kwargs)
    #字典形式，指定的
    # 默认值放最后边
aa(1,3,5,a =[2,6,8],b = [5,6,8])

def aaa(*args ,**kwargs):
    print(args)
    print(kwargs)
aaa({"name":"xuesheng"},5,6,7)
if __name__ == '__main__':
    print("main方法程序会自动执行，一个文件只能用一次main方法")