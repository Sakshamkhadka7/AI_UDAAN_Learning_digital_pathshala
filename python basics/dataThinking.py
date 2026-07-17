numbers=[10,20,30,40]

add5=[]
for number in numbers:
    number+=5
    add5.append(number)

print(add5)


import numpy as np

data=np.array([10,20,30,40])
print(data+5)