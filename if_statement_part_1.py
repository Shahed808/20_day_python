''' if statements in python'''
# a = int(input("Enter the value of a :"))
# if a==12:                                                                       # 12
#     print("Yes equal")                                                          # Yes equal


# a,b = [int(x) for x in input("Enter the value :").split(" ")]                   # (10,23) (20,10)
# if a<b:
#     print(f"{a} < {b} is {a<b}")                                                # 10 < 23 is True 
# else:
#     print(f"{a} < {b} is {a<b}")                                                # 20 < 10 is False


''' multiple if statements are given in single output'''

# a,b = [int(x) for x in input("Enter the value :").split(" ")]                   # (15,10)
# if a>b : print(f"{a} > {b} is {a>b}")                                           # True
# if a<b : print(f"{a} < {b} is {a<b}")
# if a>=b : print(f"{a} >= {b} is {a>=b}")                                        # True
# if a<=b : print(f"{a} <= {b} is {a>=b}")
# if a==b : print(f"{a} == {b} is {a==b}")
# if a!=b : print(f"{a} != {b} is {a!=b}")                                        # True



a,b = [int(x) for x in input("Enter the value :").split(" ")]                   # (20,56)
if a>b : print(f"{a} > {b} is {a>b}")                                           
elif a<b : print(f"{a} < {b} is {a<b}")                                         # True
elif a>=b : print(f"{a} >= {b} is {a>=b}")                                        
elif a<=b : print(f"{a} <= {b} is {a>=b}")
elif a==b : print(f"{a} == {b} is {a==b}")
if  a!=b : print(f"{a} != {b} is {a!=b}")                                       # True    