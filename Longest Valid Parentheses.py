def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    begin, end = 0, len(s)
    '''
    for i, l in enumerate(s):
        if l == "(":
            begin = i
            break
    for i in range(len(s)-1, 0, -1):
        if s[i] == ")":
            end = i
            break
    end = end + 1
    '''
    #print(s[begin:end])
    open_paren = [0] * len(s)
    dp_valid_parentheses = [0] * len(s)
    r = 0

    dpindex = begin
    maxparen = 0
    count = 0
    stack = []
    for i in range(begin, end):
        if s[i] == '(':
            stack.append(i)
        if s[i] == ')':
            if stack:
                openparan_index = stack.pop()
                dp_valid_parentheses[i] = dp_valid_parentheses[i-1] + 1 + dp_valid_parentheses[openparan_index-1]
        if maxparen < dp_valid_parentheses[i]:
            maxparen = dp_valid_parentheses[i]
    print(dp_valid_parentheses)
    return maxparen*2


x = longestValidParentheses("))()()))()((((((")
print(x)

print(longestValidParentheses("))))()()))"))
print(longestValidParentheses("((((((()"))
print(longestValidParentheses("()(()"))