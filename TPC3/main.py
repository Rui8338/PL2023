import re
import json

def parse(path):
    with open(path) as f:
        data = []
        for line in f:
            match = re.search(r'^(\d+)::(\d{4})-(\d{2})-(\d{2})::(.*)::(.*)::(.*)::(.*)::', line)
            if match:
                id_, ano,mes,dia, nome, pai, mae,info = match.groups()
                data.append({
                    'id': id_,
                    'ano': ano,
                    'mes': mes,
                    'dia': dia,
                    'nome': nome,
                    'pai': pai,
                    'mae': mae,
                    'info': info
                })
                
    return data

#a)------------------------------------------------
def proc_ano(data):
    res = {}
    for entry in data:
        if entry["ano"] not in res:
            res[entry["ano"]] = 0

        res[entry["ano"]] += 1

    return res

#b)------------------------------------------------
def namesAndSurnames(data):

    century_names = {}
    century_surnames = {}

    for i in range(0, 4):
        century_names[i] = {}
        century_surnames[i] = {}

    for p in data:
        year_str = p["ano"]
        year = int(year_str)
        century = (year // 100) - 16

        name_pattern = re.compile(r'(\w+)[\s\w]+\s(\w+)$')
        match = name_pattern.search(p["nome"])
        if match:
            first = match.group(1)
            surname = match.group(2)

            if first not in century_names[century]:
                century_names[century][first] = 0
            century_names[century][first] += 1

            if surname not in century_surnames[century]:
                century_surnames[century][surname] = 0
            century_surnames[century][surname] += 1

    result = []

    for i in range(0, 4):
        topNames = sorted(century_names[i], key=lambda x: century_names[i][x], reverse=True)[:5]
        topSurnames = sorted(century_surnames[i], key=lambda x: century_surnames[i][x], reverse=True)[:5]

        result.append((i + 17, topNames, topSurnames))

    return result

#c)------------------------------------------------
def relacoes(data):

    relacoes=dict()

    for entry in data:
        familiares=re.findall(r",(\w*[^.,]*)\.\s*Proc\.\d",entry["info"])
        #familiares=re.findall(r"(?i:irmao|tio|tia|pai|filho|filha|avo|mae|neto|bisavo|bisneto|bisneta)",entry["info"])
        for fam in familiares:
            if fam in relacoes:
                relacoes[fam]+=1
            else:
                relacoes[fam]=1

    return relacoes

#d)------------------------------------------------
def convert_to_json(data, file, number=20):
    with open(file, "w") as f:
        content = json.dump(data, f,indent=2)

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

def table(data):

    width = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]
    
    print('-' * (sum(width) + 7))
    print('|', end='')
    for i in range(len(data[0])):
        print(' {:{}} |'.format(str(data[0][i]), width[i]), end='')
    print('\n' + '-' * (sum(width) + 7))
    
    for row in data[1:]:
        print('|', end='')
        for i in range(len(row)):
            print(' {:{}} |'.format(str(row[i]), width[i]), end='')
        print('\n' + '-' * (sum(width) + 7))


def main():
    data = parse("processos.txt")
    printDistribution(proc_ano(data),"Ano","Frequencia")
    table(namesAndSurnames(data))
    printDistribution(relacoes(data),"Relação","Frequencia")
    convert_to_json(data[:20], "output.json")

if __name__ != "main":
    main()