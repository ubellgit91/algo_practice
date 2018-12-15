# 최댓값 구하기.


class MyAlgo():
    # 예제.
    def find_max(self, a):
        n = len(a)
        max_v = a[0]
        for i in range(1, n):
            if a[i] > max_v:
                max_v = a[i]
        return print(max_v)

    def find_max_index(self, a):
        n = len(a)
        max_idx = 0
        for i in range(1, n):
            if a[i] > a[max_idx]:
                max_idx = i
            return max_idx

# 기준이 될 최솟값을 0번 인덱스로 지정
# 입력받은 n만큼 리스트안의 값을 하나씩 꺼내봄
# 꺼내온 값과 기준값과 비교
# 만약 꺼내온 값이 기준값보다 작으면 최솟값을 갱신
# 리스트에 담긴 요소들 길이만큼 반복

class TestAlgo():
    def find_min(self, a):
        n = len(a)
        min_v = a[0]
        for i in range(1, n):
            if a[i] < min_v:
                min_v = a[i]
        return min_v



if __name__ == '__main__':
    a = [17, 92, 18, 33, 58, 7, 33, 42]
    b = [2, 54, 26, 678, 45, 5, 66, 34, 64, 87, 11]
    print(max(a)) # 만들어져 있는 함수 max를 이용
    my2 = TestAlgo()
    print(my2.find_min(a))
    print(my2.find_min(b))
