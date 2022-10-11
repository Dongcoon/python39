a = 'Hello World!'

print(a*2)

class A:
    def __init__(self):
        print("생성자")
    def __del__(self):
        print("소멸자")
a = A()
del a

