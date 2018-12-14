# algo test1
# 1~n까지의 합을 구하는 알고리즘.
#
# 1. n을 입력받는다.
# 2. 1~n까지의 값을 for each를 통해 하나씩 가져온다.
# 3. 현재 값 result에 += (더하기 대입) 한다.
# 4. result를 return한다.
class MyAlgo():
    def __init__(self):
        self.result = 0

    def cal(self, n):
        for i in range(1, n+1):
            self.result += i
        return self.result


# 교재에서 제시한 방법
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s+i
    return s
# 방법 2 더 간단하고 편한 방법.
def sum_n2(n):
    return n * (n + 1) // 2 # //는 정수 나눗셈.


class Prac():
    def __init__(self):
        self.result = 0
    # for문을 이용해 입력받은 숫자의 제곱의 합을 구하라.
    def jegop(self, n):
        for i in range(1, n+1):
            self.result += i ** 2
        return self.result

    def jegop2(self, n):
        return n * (n+1) * (2*n+1) // 6


if __name__=="__main__":
    n = int(input("범위 n 값을 입력 : "))
    my = Prac()
    print(my.jegop(n))
    print(my.jegop2(n))

