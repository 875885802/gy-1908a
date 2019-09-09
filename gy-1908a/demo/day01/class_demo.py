#对方法进行封装
class ClassDemo():
    def aaa(self):
        print("我是aaa")
    def bbb(self):
        print("我是bbb")
        self.aaa()
if __name__ == '__main__':
    c = ClassDemo()
    c.aaa()
    c.bbb()
class ClassDemo():
    def aaa(self):
        print("我是aaa")
    def bbb(self):
        print("我是bbb")
        self.aaa()
if __name__ == '__main__':
    c = ClassDemo()
    c.aaa()
class ClassDemmo():
    def aaaa(self):
        print("我是aaa啊")
    def bbbb(self):
        print("我是bbb啊")