def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0

    wpd = dict()
    lc = [-1] * len(s)
    for i, c in enumerate(s):
        if c not in wpd:
            wpd[c] = [i]
        else:
            wpd[c].append(i)
            lc[i] = wpd[c][-2]

    r = 1
    dp = [1] * len(s)
    for i, c in enumerate(s):
        if i == 0:
            continue
        if lc[i] != -1:
            dp[i] = min(dp[i-1] + 1, i - lc[i])
        else:
            dp[i] = dp[i-1] + 1
        if dp[i] > r:
            r = dp[i]

    return r



print(lengthOfLongestSubstring('pwwkew'))
