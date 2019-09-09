l = [1,2,3,4,5,6,7,8,9,0]
#新增单个数据用append
l.append(11)
print(l)
#在列表最后增多个数据用
s =[1,2,3]
l.extend(s)
print(l)
print(s)

#在列表某个位置新增单个数据
l.insert(5,12)
print(l)
#删除数据
#根据下标删除数据
print(l.pop())
print(l)
print(l.pop(-4))
print(l)
#根据内容删除数据（从左到右删除第一个#）
l.remove(2)
print(l)
#修改列表中的数据(下标)
l[2]=8
print(l)
#index更换数据
print(l.index(1))
l[l.index(1)]=9
print(l)
#排序 reverse排序规则False升序True降序
