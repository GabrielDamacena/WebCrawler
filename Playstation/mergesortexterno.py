import json
import os


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if float(left[i]["preco"].replace("R$", "").replace(",", ".")) < float(right[j]["preco"].replace("R$", "").replace(",", ".")):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


def external_merge_sort(input_file, output_file):
    
    with open(input_file, 'r', encoding='utf-8') as f:
        jogos = json.load(f)

    
    jogos_ordenados = merge_sort(jogos)

    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(jogos_ordenados, f, ensure_ascii=False, indent=4)


input_file = 'jogos_precos.json'  
output_file = 'jogos_precos_ordenados.json'  


external_merge_sort(input_file, output_file)


with open(output_file, 'r', encoding='utf-8') as f:
    jogos_ordenados = json.load(f)


for jogo in jogos_ordenados:
    print(jogo)
