import os
for i in range(1, 11):
    for j in range(1, 11):
        print("{:3d} * {:3d} = {:3d}".format(j,i,i*j))
    if i < 10:
        print("\n---------------\n")
    else:
        print("\n")

os.system("pause")
