import json

# Função de Quicksort para ordenar os jogos pelo preço
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # Separando os jogos com preço menor ou igual ao pivot e maior que o pivot
        menores = [x for x in arr[1:] if float(x["preco"].replace("R$", "").replace(",", ".")) <= float(pivot["preco"].replace("R$", "").replace(",", "."))]
        maiores = [x for x in arr[1:] if float(x["preco"].replace("R$", "").replace(",", ".")) > float(pivot["preco"].replace("R$", "").replace(",", "."))]
        return quicksort(menores) + [pivot] + quicksort(maiores)

# Abrindo o arquivo JSON que contém os jogos
with open('jogos_precos.json', 'r', encoding='utf-8') as f:
    jogos = json.load(f)

# Ordenando os jogos pelo preço
jogos_ordenados = quicksort(jogos)

# Salvando o JSON ordenado
with open('jogos_precos_ordenados.json', 'w', encoding='utf-8') as f:
    json.dump(jogos_ordenados, f, ensure_ascii=False, indent=4)

# Exibindo os jogos ordenados
for jogo in jogos_ordenados:
    print(jogo)
