def count_prime(n):
    p = set(range(2, 2*n+1))
    for i in range(2, 2*int(n**0.5)+1):
        if i in p:
            p -= set(range(2*i, 2*n+1, i))
    p -= set(range(n+1))
    return len(p)

while True:
    num = int(input())
    if num == 0:
        break
    print(count_prime(num))