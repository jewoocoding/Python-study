# 온라인 채점시스템에는 초등학생, 중고등학생, 대학생, 대학원생,
# 일반인, 군인, 프로그래머, 탑코더 등 아주 많은 사람들이 들어와 문제를 풀고 있는데,

# 실시간 채점 정보는 메뉴의 채점기록(Judge Status)을 통해 살펴볼 수 있다.

# 자! 여기서...잠깐..
# 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
# 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
print(d)