import re
import json

def somalista(lista):
    soma = 0
    for elemento in lista:
        soma += int(elemento)
    return soma

def medialista(lista):
    soma = somalista(lista)
    media = soma / len(lista)
    return media

def main():
    with open("alunos.csv",'r') as f:
        cabecalho=f.readline()
        data = [s.strip() for s in f.readlines()]
        data =[s.split(',')for s in data]

    cabecalho=re.findall(r'(\w+)(?:\{(\d)(?:,(\d))?\}(?:\::(\w+))?)?',cabecalho)
    print(cabecalho)
    print('\n')
    
    data1=[]
    for line in data:
        dados=dict()
        i = 0;
        for argumento in cabecalho:
            if argumento[1] != "":
                lista=[]
                if argumento[2] != "":
                    for elem in range(int(argumento[2])):
                        if line[i] != "":
                            lista.append(line[i])
                        i+=1
                else:
                    for elem in range(int(argumento[1])):
                        lista.append(line[i])
                        i+=1
                if argumento[3] != "":
                    if argumento[3] == "sum":
                        dados[(str(argumento[0])+"_"+"sum")]=sum(map(lambda x: int(x), lista))
                    elif argumento[3] == "media":
                        dados[(str(argumento[0])+"_"+"media")]=medialista(lista)
                    elif argumento[3] == "max":
                        dados[(str(argumento[0])+"_"+"max")]=max(map(lambda x: int(x), lista))
                    elif argumento[3] == "min":
                        dados[(str(argumento[0])+"_"+"min")]=min(map(lambda x: int(x), lista))
                else:
                    dados[argumento[0]]=lista
            else:
                dados[argumento[0]]=line[i]
                i+=1
        print(dados)
        data1.append(dados)
    with open('output.json', 'w',encoding='utf-8') as f:
        json.dump(data1, f, ensure_ascii=False, indent=2)



if __name__ != "main":
    main()