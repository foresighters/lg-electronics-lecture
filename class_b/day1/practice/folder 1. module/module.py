PI = 3.141592

class Math(object):
    def solv(self, r):
        return PI * (r ** 2)

def sum(a, b):
    return a+b

def div(a, b):
    return a / b

#__all__ = ['Math', 'sum', 'div']


if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI , 4.4))