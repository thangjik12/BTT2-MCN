import math as m


def prob(n, p, r):
    C = m.factorial(n - 1) / (m.factorial(r - 1) * m.factorial(n - r))
    return C * (p ** r) * ((1 - p) ** (n - r))


def infoMeasure(n, p, r):
    return -m.log2(prob(n, p, r))


def sumProb(N, p, r):
    '''
    Giả sử p = 0.4, r = 10 ta thử 1 vài giá trị của N như dưới và được kết quả
      N = 5 => sumProb(5, 0.4, 10) = 0
      N = 10 => sumProb(10, 0,4, 10) = 0.00010485760000000006
      N = 100 => sumProb(100, 0.4, 10) = 0.9999999999962238
      => Giá trị tiến đến 1
    '''
    sum = 0
    for i in range(r, N+1):
        sum += prob(i, p, r)
    return sum

#dùng để tính giá trị ví dụ bên trên
print(sumProb(5,0.4,10))
print(sumProb(10,0.4,10))
print(sumProb(100,0.4,10))

def approxEntropy(N, p, r):
    '''
    Giả sử p = 0.5, r = 10 ta thử 1 vài giá trị của N như dưới và được kết quả
      N = 5 => approxEntropy(5, 0.5) = 0
      N = 10 => approxEntropy(10, 0,5) = 0.009765625
      N = 100 => approxEntropy(100, 0.5) = 4.150775320863947
      N = 1000 => approxEntropy(1000, 0.5) = 4.150775320863947 
      => Giá trị tiến đến 4.150775320863947
    '''
    result = 0
    for i in range(r, N + 1):
        result += prob(i, p, r) * infoMeasure(i, p, r)
    return result

#dùng để tính giá trị ví dụ bên trên
print(approxEntropy(5,0.5,10))
print(approxEntropy(10,0.5,10))
print(approxEntropy(100,0.5,10))
print(approxEntropy(1000,0.5,10))