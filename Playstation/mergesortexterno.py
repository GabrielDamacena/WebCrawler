import json
import os

# Função para mesclar duas listas ordenadas
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

# Função Merge Sort
def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

# Função principal para ler, ordenar e escrever o arquivo JSON
def external_merge_sort(input_file, output_file):
    # Lê o arquivo JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        jogos = json.load(f)

    # Ordena os jogos usando Merge Sort
    jogos_ordenados = merge_sort(jogos)

    # Escreve o resultado ordenado em um novo arquivo
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(jogos_ordenados, f, ensure_ascii=False, indent=4)

# Caminho do arquivo JSON
input_file = 'jogos_precos.json'  # Altere para o caminho correto se necessário
output_file = 'jogos_precos_ordenados.json'  # Caminho do arquivo de saída

# Executa a função
external_merge_sort(input_file, output_file)

# Para verificar os jogos ordenados
with open(output_file, 'r', encoding='utf-8') as f:
    jogos_ordenados = json.load(f)

# Exibindo os jogos ordenados
for jogo in jogos_ordenados:
    print(jogo)
