print("|\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")

A = input("입력")
B = input("입력")
print(int(A) + int(B))

A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

A = input()
B = input()
print(int(A) * int(B[2]))
print(int(A) * int(B[1]))
print(int(A) * int(B[0]))
print(int(A) * int(B))

A, B = map(int, input().split())
print(A+B)

A, B = map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")


score = int(input())
if score <= 100 and score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
1999 % 4
2000 % 4

years = int(input())
if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
        print("1")
else:
    print("0")

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print("1")
    elif y < 0:
        print("4")
elif x < 0:
    if y > 0:
        print("2")
    elif y < 0:
        print("3")

H, M = map(int, input().split())
if M >= 45:
        print(H, M-45)
elif M < 45:
    if H >0:
        print(H-1, 15+M)
    elif H==0:
        print(23, 15+M)

N = int(input())
for i in range(1,10):
    print(N,"*", i,"=", i * N)

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)

N = int(input())
total=0
for i in range(N+1):
    total += i
print(total)

T = int(input())
import sys
for i in range(T):
    A, B = sys.stdin.readline().strip().split()
    print(int(A) + int(B))

N = int(input())
for i in range(N, 0, -1):
    print(i)

T = int(input())
import sys
for i in range(T):
    A, B = sys.stdin.readline().strip().split()
    print('Case #{}: {} + {} ='.format(i+1,A,B), int(A) + int(B))

T = int(input())
for i in range(1, T+1):
    print(' '* (T-i) + '*' * i)

import sys
N, X = sys.stdin.readline().strip().split()
A = sys.stdin.readline().strip().split()
total = []
for i in range(int(N)):
    if int(A[i]) < int(X):
        total.append(A[i])
    else:
        pass
print(" ".join(total))

import sys
N, X = map(int, input().split())
A = list(map(int, input().split()))
del A
while True:
    try: 
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

N = int(input())
i = 0
T = N
while True:
    if T < 10:
        sum = T
        print(sum)
    elif T >= 10 and T <=99:
        sum = T//10 + T%10
        print(sum)
    T = T % 10 * 10 + sum % 10
    i += 1
    if total == N:
        break



89//10
89%10

# 코드 추가 했당~~~
list = [1,2,3,4]