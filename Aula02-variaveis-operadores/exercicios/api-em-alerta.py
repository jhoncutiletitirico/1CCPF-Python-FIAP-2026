#Descrição Uma API possui três endpoints. A matriz abaixo registra os códigos, HTTP das últimas requisições realizadas:
#Crie um programa que:
# 1. calcule a porcentagem de requisições bem-sucedidas de cada endpoint;
# 2. identifique o endpoint com mais erros;
# 3. verifique se algum endpoint teve dois erros seguidos;
# 4. classifique cada endpoint como:
# ▪ ESTÁVEL: pelo menos 80% de sucesso;
# ▪ INSTÁVEL: menos de 80%;
# ▪ CRÍTICO: dois erros consecutivos.


endpoints = ["/login", "/produtos", "/pedidos"]


status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 200, 500]

]

# Função Que Verifica Se Um Status Code HTTPS É Sucesso
# 200-299 = Sucess

def sucesso(status_code):
    return status_code >= 200 and status_code <=299

print(sucesso(200))