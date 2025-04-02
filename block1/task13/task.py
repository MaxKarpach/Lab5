def partitionIntoThree(a):
    totalSum = sum(a)
    if totalSum % 3 != 0:
        return 0
    target = totalSum // 3

    dp = {0: {0: {0}}}

    for v in a:
        newDp = {}
        for s1 in dp:
            for s2 in dp[s1]:
                for s3 in dp[s1][s2]:
                    newDp.setdefault(s1, {}).setdefault(s2, set()).add(s3)
                    if s1 + v <= target:
                        newDp.setdefault(s1 + v, {}).setdefault(s2, set()).add(s3)
                    if s2 + v <= target:
                        newDp.setdefault(s1, {}).setdefault(s2 + v, set()).add(s3)
                    if s3 + v <= target:
                        newDp.setdefault(s1, {}).setdefault(s2, set()).add(s3 + v)
        dp = newDp

    return 1 if target in dp and target in dp[target] and target in dp[target][target] else 0

with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    a = list(map(int, f.readline().strip().split()))

with open("output.txt", "w") as f:
    f.write(str(partitionIntoThree(a)))