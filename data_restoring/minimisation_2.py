
from iminuit import Minuit
# # /////////////////////
# def to_min(a, b, c, d, e, f):
#     x = 1
#     res = abs(f1[x]*a + f2[x]*b + f3[x]*c + f4[x]
#               * d + f5[x]*e + f6[x]*f - f0[x])
#     return res


# m = Minuit(to_min, a=0.5, b=0.5, c=0.5, d=0.5, e=0.5, f=0.5)
# m.limits = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]
# # def cost_function(x, y, z):
# #     return (x - 2) ** 2 + (y - 3) ** 2 + (z - 4) ** 2
# # m = Minuit(cost_function, x=0, y=0, z=0)
# res = m.migrad()
# print(res)
# print('-------------')
# print('------------')
# to_min(0.5, 0.5, 0.5, 0.5, 0.5, 0.5)
# print('-------------')
# print('------------')
# valnew = list(res.values)
# newres = to_min(valnew[0], valnew[1], valnew[2],
#                 valnew[3], valnew[4], valnew[5])
# print(newres)
# # x = 1


# def mincol(f0, f1, f2, f3, f4, f5, f6):
#     def to_min(a, b, c, d, e, f):
#         res = abs(f1[x]*a + f2[x]*b + f3[x]*c + f4[x]
#                   * d + f5[x]*e + f6[x]*f - f0[x])

#     # def to_min(a, b, c, d):
#     #     res = abs(f1[x]*a + f2[x]*b + f3[x]*c + f4[x]*d - f0[x])
#         return res
#     coefs = np.zeros((len(f0), 6))
#     # coefs = np.zeros((len(f0), 4))
#     for x in range(len(f0)):
#         m = Minuit(to_min, a=0.5, b=0.5, c=0.5, d=0.5, e=0.5, f=0.5)
#         m.limits = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]
#         # m = Minuit(to_min, a=0.25, b=0.25, c=0.25, d=0.25)
#         # m.limits = [(0, 1), (0, 1), (0, 1), (0, 1)]
#         res = m.migrad()
#         coefs[x] = res.values
#         if x % 100 == 0:
#             print(x)
#     print(pd.DataFrame(coefs))
#     return coefs


# # def restore(coefs: np.ndarray, values=np.ndarray):
# #     res = np.sum(coefs*values, axis=1)
# #     print(res)
# #     res = pd.DataFrame(res)
# #     return res

# coefs = mincol(f0, f1, f2, f3, f4, f5, f6)
# # ////////////////////////////////////////////
