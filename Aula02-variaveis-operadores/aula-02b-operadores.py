from skimage.transform import resize
from statsmodels.discrete.discrete_margins import margeff_cov_with_se

num1 = 4
num2 = 2

print(type(num1), type(num2))

resultado = num1 // num2
print(resultado, type (resultado))


# OPERADORES DE ATRIBUIÇÃO
num = 15
print() # pular uma linha
print(num)

num = num + 2 # acumulador
print(num)

print += 2
print(num)

# OPERADORES RELACIONAIS
idade = 18
print(idade)

logado = True
print(logado, type(logado))

maior_idade = idade >= 18
print(maior_idade, type(maior_idade))

# SRINGS
nome1 = "Marcos"
nome2 = "marcos"

print (nome1 == nome2)
