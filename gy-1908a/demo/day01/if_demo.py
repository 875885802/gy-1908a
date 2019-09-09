# if()代码
# else：代码

# 小明去超市买酸奶，有 1 买一袋，没有 0 去下一个超市
a = 1
if(a == 1):
    print("买一袋")
else:
    print("去下一个超市")
# 小明考试成绩大于80为优秀，成绩大于60，成绩小于80为合格，成绩小于60为不合格
a = 60
if(a >= 80):
 print("小明成绩为优秀")
elif(a >= 60):
    print("小明成绩为合格")
elif(a < 60):
    print("小明成绩为不合格")
i = 1
while(i<101):
    print(i)
    i+=1
#dergakio   要求生成两个新的字符串  drai  和egko
b = "dergakio"
print(b [::2])
print(b [1::2])
#字符串切片
d = "用例名,充值金额,断言"
print(d.split(","))
f = "红豆 黑豆 黄豆"
print(f.split(" "))
c = '  dkjjdkfl   '
print(c.lstrip())  #去左空格
print(c.rstrip()) #去右空格
print(c.strip())  #去前后所有空格
c = '  dkjj  dkfl   '
# 去除所有空格
print(c.replace(" ", ""))
#替换
f ='hdkjsfyeihbjdcn"j8542124'
print(f.replace('"',"'"))
#查找
g ='guoyasoft'
print(g.find("ya"))
#长度
g ='guoyasoft'
print(len(g))
#GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
d = "GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1"
l =d.split(" ")
print(l)
