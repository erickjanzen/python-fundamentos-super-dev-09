import requests

url_base =  "https://api.franciscosensaulas.com"

def consultar_requisicao():
    url = f"{url_base}/api/v1/biblioteca/categorias"

    resposta = requests.get(url)

    print("Status Code:", resposta.status_code)
    print("Response:", resposta.text)

consultar_requisicao()