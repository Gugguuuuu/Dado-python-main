# EXERCICIO 27
# USANDO RANDOM PARA SORTEA NOMES
import random
from time import sleep
print('Digite o nome de cinco pessoas para cada uma tentar acertar o valor do dado')

sleep(3)

n1 = str(input('Digite o nome da primeira pessoa : '))
n2 = str(input("Digite o nome da segunda pessoa : "))
n3 = str(input('Digite o nome da terceira pessoa : '))
n4 = str(input('Digite o nome da quarta pessoa : '))
n5 = str(input('Digite o nome da quinta pessoa : '))
dado = random.randint(1, 6)

print('O dado foi jogado. Pronto {}, {}, {}, {}, {} podem tentar um valor'.format(n1, n2, n3, n4, n5))

sleep(2)
c1 = int(input('Pronto {} pode tentar acerta o numero : '.format(n1)))
c2 = int(input('Pronto {} pode tentar acerta o numero : '.format(n2)))
c3 = int(input('Pronto {} pode tentar acerta o numero : '.format(n3)))
c4 = int(input('Pronto {} pode tentar acerta o numero : '.format(n4)))
c5 = int(input('Pronto {} pode tentar acerta o numero : '.format(n5)))

if c1 == dado:
    print('O resultado era : {}. O vencedor foi : {}!'.format(dado, n1))
elif c2 == dado:
    print('O resultado era : {}. O vencedor foi : {}!'.format(dado, n2))
elif c3 == dado:
    print('O resultado era : {}. O vencedor for : {}!'.format(dado, n3))
elif c4 == dado:
    print('O resultado era : {}. O vencedor foi : {}!'.format(dado, n4))
elif c5 == dado:
    print('O resultado era : {}. O vencedor foi : {}!'.format(dado, n5)) 
else:
    print('Todos erraram, tente novamente')       
  
# nomes = [
#     'João',
#     'Pedro',
#     'Isa',
#     'Flavia',
#     'Luciaena'
# ]
# nome = random.choice(nomes)
# print(nome)
