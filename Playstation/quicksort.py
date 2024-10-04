import json

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        
        menores = [x for x in arr[1:] if float(x["preco"].replace("R$", "").replace(",", ".")) <= float(pivot["preco"].replace("R$", "").replace(",", "."))]
        maiores = [x for x in arr[1:] if float(x["preco"].replace("R$", "").replace(",", ".")) > float(pivot["preco"].replace("R$", "").replace(",", "."))]
        return quicksort(menores) + [pivot] + quicksort(maiores)


with open('jogos_precos.json', 'r', encoding='utf-8') as f:
    jogos = json.load(f)


jogos_ordenados = quicksort(jogos)


with open('jogos_precos_ordenados.json', 'w', encoding='utf-8') as f:
    json.dump(jogos_ordenados, f, ensure_ascii=False, indent=4)


for jogo in jogos_ordenados:
    print(jogo)
