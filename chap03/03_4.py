# ❖x^n을 구하는 프로그램


x = float(input('Type x : '))
n = int(input('Type n : '))
prod = 1
for i in range(1, n+1):
    prod = prod * x
print(prod) 