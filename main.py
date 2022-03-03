# This is a sample Python script.

def prime_numbers_v1(n):
    l = []
    q = 0
    d = 0
    for i in range(2, n+1):
        d = 0
        for j in range(1, i+1):
            if i % j == 0:
                d += 1
        if d == 2:
            l.append(i)
    for k in l:
        if k < n:
            q += 1
    print(f'q = {q}')


def prime_numbers_v2(n):
    q = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
            if i < n:
                q += 1
    print(f'q = {q}')





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print('q = 0')
    else:
        prime_numbers_v2(n)