from math import log, prod
from itertools import combinations, combinations_with_replacement


# Задача №1
def domain_name(url):
    if "//" in url:
        url = url.split("//")[1]
    url = url.removeprefix("www.").split(".")
    return url[0]


# Задача №2
def int32_to_ip(int32):
    bin_str = f"{int32:b}".rjust(32, "0")
    list_ip = [int(bin_str[i:i + 8], 2) for i in range(0, 32, 8)]
    ip_4 = ".".join(map(str, list_ip))
    return ip_4


# Задача №3
def zeros(n):
    if n < 1:
        return 0
    k_max = int(log(n, 5))
    z = 0
    for k in range(1, k_max+1):
        z += int(n / 5**k)
    return int(z)


# Задача №4
def bananas(s):
    result = set()
    for comb in combinations(range(len(s)), len(s) - 6):
        arr = list(s)
        for i in comb:
            arr[i] = '-'
        candidate = ''.join(arr)
        if candidate.replace('-', '') == 'banana':
            result.add(candidate)
    return result


# Задача №5
def count_find_num(primesL, limit):
    l = primesL.copy()
    l.sort()
    min_num = l.pop(0)
    solution = limit
    all_comb = []
    all_comb_fit = []
    result = [0, 0]
    max_len_comb = int(log(solution, min_num)) + len(l)

    for n in l:
        solution //= n
    if solution < min_num:
        return []

    for len_comb in range(len(primesL), max_len_comb + 1):
        all_comb.extend(list(combinations_with_replacement(primesL, len_comb)))

    for comb in all_comb:
        if all(num in comb for num in primesL) and prod(comb) <= limit:
            all_comb_fit.append(comb)
            if prod(comb) > result[1]:
                result[1] = prod(comb)

    result[0] = len(all_comb_fit)

    return result
