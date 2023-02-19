import matplotlib.pyplot as plt

modelo=dict()

def readfile():
    f = open("myheart.csv")
    for linha in f:
        idade,sexo,tensão,colesterol,batimento,temDoença=linha.split(",")
        if temDoença in modelo:
            modelo[temDoença].append((idade,sexo,tensão,colesterol,batimento))
        else:
            modelo[temDoença] = [(idade,sexo,tensão,colesterol,batimento)]

def doencaporsexo():
    dist=dict([('M',0),('F',0)])
    for value in modelo['1\n']:
        if value[1] == 'M':
            dist['M']=dist['M']+1
        elif value[1] == 'F':
            dist['F']=dist['F']+1
    return dist

def doencaporidade():
    dist=dict()
    max= 0
    for value in modelo['1\n']:  
        if (int(value[0]))>max:
            max=int(value[0])
    i=30
    while i<max:
        if i+4>max:
            aux = {(i,max):0}
        else:
            aux = {(i,i+4):0}   
        dist.update(aux)
        i+=5
    for value in modelo['1\n']:
        for key in dist.keys():
            if key[0]<=int(value[0])<=key[1]:
                dist[key]=dist[key]+1
    return dist

def doencaporclestrol():
    dist=dict()
    max= 0
    for value in modelo['1\n']:  
        if (int(value[3]))>max:
            max=int(value[3])
    i=0
    while i<max:
        if i+9>max:
            aux = {(i,max):0}
        else:
            aux = {(i,i+9):0}   
        dist.update(aux)
        i+=10
    for value in modelo['1\n']:
        for key in dist.keys():
            if key[0]<=int(value[3])<=key[1]:
                dist[key]=dist[key]+1  
    return dist 


def imprimirtabela(tipo,dist):
    print('-'*24)
    print(f"|{tipo}|Total|")
    print('-'*24)
    for key in dist.keys():
        print("|{}-{:<10} | {:<5}|".format(key[0],key[1], dist[key]))
        print('-'*24)

def printDistSexo(dist):
    res = '-'*24 + '\n'
    res += f'|{"Sexo":<10} | {"Total":<5}|\n'
    res += '-'*24 + '\n'
    for key in dist.keys():
        res += "|{:<10} | {:<5}|\n".format(key, dist[key])
        res += '-'*24 + '\n'
    print(res)

def printDistribution(someDict,table_key,table_value):
    keys = list(someDict.keys())
    values = list(someDict.values())

    max_key_length = max([len(str(key)) for key in keys])
    max_value_length = max([len(str(value)) for value in values])

    if max_key_length < len(table_key) : max_key_length = len(table_key)
    if max_value_length < len(table_value) : max_value_length = len(table_value) 


    print(f"\n+{'-' * (max_key_length + 2)}-{'-' * (max_value_length + 2)}+")
    print(f"| {table_key.ljust(max_key_length)} | {table_value.ljust(max_value_length)} |")

    for i in range(len(keys)):
        print(f"|{'-' * (max_key_length + 2)}|{'-' * (max_value_length + 2)}|")
        print(f"| {str(keys[i]).ljust(max_key_length)} | {str(values[i]).ljust(max_value_length)} |")
    print(f"+{'-' * (max_key_length + 2)}-{'-' * (max_value_length + 2)}+")

def main():
    readfile()
    printDistribution(doencaporsexo(),"Sexo","Valor") 
    print("\n")
    printDistribution(doencaporidade(),"Idade","Valor") 
    print("\n")
    printDistribution(doencaporclestrol(),"Colestrol","Valor")    
    
    dist=doencaporsexo()
    
    plt.figure(figsize=(15,20))
    plt.style.use('_mpl-gallery')
    plt.subplot(2, 1, 1)
    barras=plt.bar(dist.keys(), dist.values(), width=1, edgecolor="white", linewidth=3)
    plt.title('Distribuição pelo sexo')
    plt.bar_label(barras, labels=dist.values())

    plt.style.use('_mpl-gallery-nogrid')
    plt.subplot(2, 1, 2)
    colors=['blue','yellow','green','pink','red', 'orange']
    plt.pie(dist.values(),labels=dist.keys(),colors=colors, autopct='%1.1f%%',radius=1.5)

    dist=doencaporidade()

    plt.figure(figsize=(30,30))
    plt.style.use('_mpl-gallery')
    plt.subplot(2, 1, 1)
    barras=plt.bar(list(map(lambda x: str(x).replace('(','[').replace(')',']'),dist.keys())), list(dist.values()), width=1, edgecolor="white", linewidth=2)
    plt.title('Distribuição por colestrol')
    plt.bar_label(barras, labels=dist.values())
    plt.xticks(rotation=45)

    plt.style.use('_mpl-gallery-nogrid')
    plt.subplot(2, 1, 2)
    plt.pie(dist.values(),labels=list(map(lambda x: str(x).replace('(','[').replace(')',']'),dist.keys())),colors=colors, autopct='%1.1f%%',radius=1)

    dist=doencaporclestrol()

    plt.figure(figsize=(15,20))
    plt.style.use('_mpl-gallery')
    plt.subplot(2, 1, 1)
    barras=plt.bar(list(map(lambda x: str(x).replace('(','[').replace(')',']'),dist.keys())), list(dist.values()))
    plt.title('Distribuição por colestrol')
    plt.bar_label(barras, labels=dist.values())
    plt.xticks(rotation=45)

    plt.style.use('_mpl-gallery-nogrid')
    plt.subplot(2, 1, 2)
    plt.pie(dist.values(),labels=list(map(lambda x: str(x).replace('(','[').replace(')',']'),dist.keys())),colors=colors, autopct='%1.1f%%',radius=1.5)

    plt.subplots_adjust(hspace=0.5)
    plt.show()
    

if __name__ == "__main__":
    main()
