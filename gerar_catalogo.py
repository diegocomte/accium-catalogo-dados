import requests
import json

URL = "https://opensheet.elk.sh/1_GpGHG2x1Ob0scQs6yxZSuvwzHE7Rp2d5hxD1OhwGnA/produtos"

response = requests.get(URL)
data = response.json()

produtos = []

for p in data:
    produtos.append({
        "id": int(p["id"]),
        "nome": p["nome"],
        "categoria": p["categoria"],
        "descricao": p["descricao"],
        "imagem": p["imagem"]
    })

with open("catalogo.json", "w", encoding="utf-8") as f:
    json.dump(produtos, f, ensure_ascii=False, indent=2)

print("catalogo.json atualizado")
