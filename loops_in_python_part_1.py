''' loops concepts in python'''


# a = 1,2,3,4,5
# print(*a)                                                                                   # 1 2 3 4 5


# a = 4,5,6
# for code in a:
#     print(code,end=" ")                                                                       # 4 5 6

# for i in range(10):
#     print(i,end=" ")                                                                            # 0 1 2 3 4 5 6 7 8 9 


# w = int(input("Enter the value of w:"))
# for x in range(1,w+1):
#     print(x, end=" ")                                                                            # 1 2 3 4 5 6 7 8 9 10 


# for i in range(1,25,2):
#     print(i,end=" ")                                                                                # 1 3 5 7 9 11 13 15 17 19 21 23 


# for y in range(2,27,2):
#     print(y,end=' ')                                                                                # 2 4 6 8 10 12 14 16 18 20 22 24 26 


# for u in range(10,0,-1):
#     print(u,end=" ")                                                                                    # 10 9 8 7 6 5 4 3 2 1 


# for p in range (20,-1,-2):
#     print(p,end=' ')                                                                                    # 20 18 16 14 12 10 8 6 4 2 0 


g = [10,3.65,'Name',True]
for h in g[::-1]:
    print(h)                                                                                # True Name 3.65 10


j = "Programming"
for o in j[::2]:
    print(o,end=' ')                                                                                    # P o r m i g 


