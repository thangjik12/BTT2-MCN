import math as m


def prob(n, p, N):
    C = m.factorial(N) / (m.factorial(n) * m.factorial(N - n))
    return C * (p ** n) * ((1 - p) ** (N - n))


def infoMeasure(n, p, N):
    return -m.log2(prob(n, p, N))


def sumProb(N, p):
    '''
    Giả sử p = 0.4, ta thử 1 vài giá trị của N như dưới và được kết quả
      N = 5 => sumProb(5, 0.4) = 0.95904
      N = 10 => sumProb(10, 0,4) = 0.9992659968
      N = 100 => sumProb(100, 0.4) = 1
      => Giá trị tiến đến 1
    '''
    sum = 0
    for i in range(0, N):
        sum += prob(i, p, N+1)
    return sum

#dùng để tính giá trị ví dụ bên trên
print(sumProb(5,0.4))
print(sumProb(10,0.4))
print(sumProb(100,0.4))

def approxEntropy(N, p):
    '''
    Giả sử p = 0.5, ta thử 1 vài giá trị của N như dưới và được kết quả
      N = 5 => approxEntropy(5, 0.5) = 2.041942411043098
      N = 10 => approxEntropy(10, 0,5) = 2.696663338227331
      N = 100 => approxEntropy(100, 0.5) = 4.369011409223017
      N = 1020 => approxEntropy(1020, 0.5) = 6.044272187826667
      => Giá trị tiến đến 6.044
    '''
    result = 0
    for i in range(0, N):
        result += prob(i, p, N) * infoMeasure(i, p, N)
    return result

print(approxEntropy(5,0.5))
print(approxEntropy(10,0.5))
print(approxEntropy(100,0.5))
print(approxEntropy(1020,0.5))