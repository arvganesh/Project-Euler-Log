def pentagonal(n):
    return (n * ( 3 * n - 1)) / 2

def generatePentagonals(n):
    n = n-1
    lst = [0]
    num, ctr = 1, 1
    while True:
        lst.append(num)
        ctr += 1
        if ctr > n:
            break
        lst.append((-1)*num)
        ctr += 1
        num += 1
        if ctr > n:
            break
    pents = [pentagonal(x) for x in lst]
    return pents


def main(N):
    mod = 10 ** 6
    pents = generatePentagonals(N)
    partitions = [0] * N
    partitions[0] = 1

    num = 1
    while num < N:
        ctr = 1
        while num - pents[ctr] >= 0:
            pent = pents[ctr]
            partitions[num] += ((-1) ** ((ctr-1)/2)*partitions[num - pent]) % mod
            ctr += 1
        if partitions[num] % mod == 0:
            print num
        num += 1

main(100000)
