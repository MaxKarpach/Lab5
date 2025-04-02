MOD = 10 ** 9
def count_phone_numbers(N):
    if N == 1:
        return 8  # 1-9 без 0 и 8

    moves = {
        0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8],
        4: [3, 9, 0], 5: [], 6: [1, 7, 0],
        7: [2, 6], 8: [1, 3], 9: [2, 4]
    }

    prev = [0] * 10
    curr = [0] * 10

    for j in range(10):
        if j != 0 and j != 8:
            prev[j] = 1

    for i in range(2, N + 1):
        for j in range(10):
            curr[j] = sum(prev[k] for k in moves[j]) % MOD
        prev, curr = curr, prev

    return sum(prev) % MOD


with open("input.txt", "r") as f:
    N = int(f.readline().strip())

result = count_phone_numbers(N)

with open("output.txt", "w") as f:
    f.write(str(result) + "\n")