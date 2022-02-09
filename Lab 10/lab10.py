
def power(x,n):
    if n == 0:
        return 1
    return x * power(x,n-1)

# print(power(2,5))


def interleave(L1,L2):
    if len(L2) == 0:
        return []
    return [L1[0]] + [L2[0]] + interleave(L1[1:],L2[1:])

L1 = [1, 2, 3]
L2 = [4, 5, 6]

# print(interleave(L1,L2))


def reverse_rec(L):
    if len(L) == 0:
        return []
    return [L[-1]] + reverse_rec(L[:-1])

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(reverse_rec(L))


def zigzag(L, i = 1):
    if i > len(L)//2:
        return ""
    elif i == 1:
        print (L[len(L)//2], end=" ")

    print(L[len(L)//2-i],L[len(L)//2+i], end=" ")

    print(zigzag(L,i+1), end=" ")
    return ""

# zigzag(L)


def is_balanced(s):
    count = 0
    if s == '':
        if count == 0:
            return False
    elif s[0] == "(" and s[-1] == ")":
        count += 1
        s = s[count:-count]
        is_balanced(s)
        return True
    return False

s = "(())()"
# print(is_balanced(s))