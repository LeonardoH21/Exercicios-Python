reais = float(input('Digite sua quantidade em reais (R$): '))

cotacao_dolar = 5.90
cotacao_bitcoin = 84100.00  


dolares = reais / cotacao_dolar


bitcoins = dolares / cotacao_bitcoin

# resultados 

print('Com R$ {:.2f} , voce pode comprar :'.format(reais))
print('- US$ {:.2f} dólares'.format(dolares))
print('- ₿{:.8f}'.format(bitcoins))