# Day 2

## List의 주요 함수

len(a) 리스트의 길이를 구한다.

append(x) 자료 x를 리스트의 **맨 뒤**에 추가한다.

insert(i, x) 자료 x를 인덱스 i번째 위치에 추가한다.

pop(i) 인덱스 i번에 있는 값을 결과값으로 반환한다. i를 입력하지 않으면 맨 마지막 값을 리턴함

clear() 리스트의 모든 자료를 지운다.

x  in a  a리스트에 x값이 있는지 검사한다. 있으면 True 없으면 False

x not in a a에 x가 없으면 True 있으면 False



## 최댓값 찾기

a = [17, 92, 18, 33, 58, 7, 33, 42] 중에서 최대값을 찾아보자.

```python
    def find_max(self, a):
        n = len(a)
        max_v = a[0]
        for i in range(1, n):
            if a[i] > max_v:
                max_v = a[i]
        return print(max_v)

```

처음에 기준 값을 a[0]으로 잡고,

+1되는 인덱스에 담긴 값과 "비교"를 통해서 비교한 값이 더 크면 그 비교한 값을 최대값으로 담는다. 이런 방법을 반복한다.

자료 n개 중에 최댓값을 찾으려면 비교를 n-1번 해야한다. (-1은 초기 기준값은 0번 인덱스로 잡혀있기 때문에, **비교**의 횟수는 n-1번임.)



입력크기 n이 커지면 비교해야하는 계산 횟수도 정비례로 늘어나므로 정비례로 늘어난다고 할 수 있다. 그러므로 빅오 표기법으로 보면 이는

O(n)과 같다고 볼 수 있다.



## 응용문제

리스트에 숫자가 n개 있을 때 가장 큰 값이 있는 위치 번호를 돌려주는 알고리즘을 만들어 보라.

```python

    def find_max_index(self, a):
        n = len(a)
        max_idx = 0
        for i in range(1, n):
            if a[i] > a[max_idx]:
                max_idx = i
            return max_idx
```



## 연습문제

숫자 n개를 리스트로 입력받아서 최솟값을 구하는 프로그램.

```python
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

```

