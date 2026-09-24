import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("10 + 5 =", servidor.soma(10, 5))
print("10 - 5 =", servidor.subtracao(10, 5))
print("10 * 5 =", servidor.multiplicacao(10 ,5))
print("10 / 5 =", servidor.divisao(10 ,5))
