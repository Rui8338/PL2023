import sys

soma=0
flag=True
number=False
valor=0
turn=0

for linha in sys.stdin:
    for n in linha:
        if n.isnumeric(): 
            if number is True:
                valor=valor*10+int(n)
            else: 
                number=True
                valor=int(n)
        else:
            if flag is True:
                soma+=valor
            valor=0
            number=False 
            if n=='o' or n =='O':
                turn=1
            elif (n=='n'or n=='N') and turn==1:
                flag=True
            elif n=='f' or n=='F':
                if turn==1:
                    turn+=1
                elif turn==2:
                    flag=False
            elif n=='=':
                print(soma)

    