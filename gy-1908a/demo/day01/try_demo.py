

#除法
def d(a,b):
    try:
        c = a/b
    except ZeroDivisionError:

        print('除数不能为0')
        return
    return c


print(d(18,3))