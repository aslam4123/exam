from add import *
from sub import *
from mul import *
from div import *
from numbers import *

while True:
    print('''
    1.add
    2.sub
    3.mul
    4.div
    5.exit''')
    choice=int(input('enter the choice:'))
    if choice==1:
          a,b=num()
          add(a,b)
    elif choice==2:
          a,b=num()
          sub(a,b)
    elif choice==3:
          a,b=num()
          mul(a,b)
    elif choice==4:
          a,b=num()
          div(a,b)
    elif choice==5:
          break
    else:
          print('invalid')
       