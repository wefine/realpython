def largest_proper_divisor(n):
    largest_divisor = 1  # 初始化为最小约数
    for i in range(1, int(n**0.5) + 1):  # 遍历到 sqrt(n)
        if n % i == 0:  # i 是 n 的因数
            # 获取因数对 (i, n // i)
            larger = n // i
            if larger != n:  # 确保因数不是 n 本身
                return larger  # 返回除 n 本身外的最大因数
            else:
                largest_divisor = i
    return largest_divisor  # 如果 n 是素数，只返回 1

# 示例
n = 7843
print(f"{n} 除自身以外最大的约数是：{largest_proper_divisor(n)}")
