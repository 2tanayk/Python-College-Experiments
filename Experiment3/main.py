import listmodule as lm
import math as m

while(True):
    print(''' Enter your choice:
     1)Summation
     2)Product
     3)Summation at even indices
     4)add element
     5)Exit''')

    choice=int(input())

    if choice==1:
        print(sum(lm.l))
    elif choice==2:
        print(m.prod(lm.l))
    elif choice==3:
        print(sum(lm.l[::2]))
    elif choice==4:
        lm.l.append(int(input()))
    else:
        break