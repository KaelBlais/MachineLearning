
import numpy as np
import pandas as pd

print("Hello World\n")

A = np.zeros((3, 2), dtype = float)
T0 = pd.read_html("https://www.capfriendly.com/browse/active")
T1 = pd.read_html("https://www.capfriendly.com/browse/active?pg=2")

# print("Test Matrix A: \n" + str(A))
# print(T0)
# print(T1)

# print("T0 type: " + str(type(T0))) 

# print("T0 row 0: " + str(T0[0]))


# print("Size of T0: " + str(T0.shape))

# print("Size of T0: " + str(T0.shape))

# print( "T0 first row: " + str(T0[0, :]))

# print( "T0 Len: " + str(len(T0)))

df = pd.DataFrame(T0)

# print("T0 as string: " + str(T0)[0:10])

'''
for i in T0:
    print( "Len of I: " + str(len(i)))
    print(i[0:5])
    for j in i[0:5]:
        print( "Len of J: " + str(len(j)))
        print(str(j))
'''
for i in T0:
    B = i


# print("Type of B:" + str(type(B)))

print(B.columns)

C = B["PLAYER"].iloc[0]

print(C)



# print(df.size)