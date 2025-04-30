preço = float (input('Digite o preço do produto'))


desconto = preço - (preço * 0.05)

print ('O preço do produto é R${:.2f} , o desconto é de 5% então fica R${:.2f}'.format(preço,desconto))