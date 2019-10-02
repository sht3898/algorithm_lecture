stick = ['B', 'Y', 'RR']


# def makeStick(n, s):
#     if n == 0:
#         print(s)
#     else:
#         for i in stick:
#             if n >= len(i):
#                 makeStick(n - len(i), s + stick[i])
#
#
# makeStick(2, '')
#
# # ----------------------------------------
#
# def makeStick(n):
#     if n == 1: return 2
#     if n == 2: return 5
#     if memo[n] != -1: return memo[n]
#     momo[n] = makeStick(n - 1) * 2 + makeStick(n - 2)
#     memo[n] = memo