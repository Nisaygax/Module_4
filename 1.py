# def counter(s):
#     for i in s:
#         k = 0
#         for w in s:
#             if i == w:
#                 k += 1
#         print(i, k)

# counter('abcd')

# # O(N*N)




# def counter(s):
#     for n in set(s):
#         k = 0
#         for m in s:
#             if n == m:
#                 k += 1
#         print(n, k)

# counter('abbcccdddd')

# # O(N*M)





# def counter(s):
#     lits = {}
#     for n in s:
#         lits[n] = lits.get(n, 0) + 1
#     for n, k in lits.items():
#         print(n, k)

# counter('aabbccdd')

# # O(N)