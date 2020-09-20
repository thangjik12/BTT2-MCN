import math as m

def prob(n, p):
    return ((1-p)**(n-1))*p


def infoMeasure(n, p):
    return -m.log2(prob(n, p))

def sumProb(N, p):
    '''
    Giả sử p = 0.4, ta thử 1 vài giá trị của N như dưới và được kết quả
      N = 5 => sumProb(1, 0.4) = 0.9222400000000001
      N = 10 => sumProb(10, 0,4) = 0.9939533824
      N = 100 => sumProb(100, 0.4) = 1
      => Giá trị tiến đến 1
    '''
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p)
    return sum

#dùng để tính giá trị ví dụ bên trên
print(sumProb(5,0.4))
print(sumProb(10,0.4))
print(sumProb(100, 0.4))

def approxEntropy(N, p):
    '''
    Ta có entropy của nguồn geometric với giá trị p = 0.5 bằng 2.
    Giả sử với p = 0.4, ta thử với các giá trị của N kết quả dựa trên phép tính bên dưới
      N = 5 => approxEntropy(5, 0.5) = 1.78125
      N = 10 => approxEntropy(10, 0.5) = 1.98828125
      N = 100 => approxEntropy(100, 0.5) = 1.9999999999999998
      => Giá trị tiến đến 2
    Suy ra hàm approxEntropy tính xấp xỉ entropy của nguồn tin geometric
    '''
    result = 0
    for i in range(1, N + 1):
        result += prob(i, p) * infoMeasure(i, p)
    return result

#dùng để tính giá trị ví dụ bên trên
print(approxEntropy(5,0.5))
print(approxEntropy(10,0.5))
print(approxEntropy(100, 0.5))