## QUESTÃO 1 ##
# Faça um programa que receba cinco inteiros e diga qual deles é o maior e qual o menor.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    c = int(input('Terceiro valor: '))
    d = int(input('Quarto valor: '))
    e = int(input('Quinto valor: '))

    if a<b and a<c and a<d and a<e:
        menor = a
    if b<a and b<c and b<d and b<e:
        menor = b
    if c<a and c<b and c<d and c<e:
        menor = c
    if d<a and d<b and d<c and d<e:
        menor = d
    if e<a and e<b and e<c and e<d:
        menor = e


    if a>b and a>c and a>d and a>e:
        maior = a
    if b>a and b>c and b>d and b>e:
        maior = b
    if c>a and c>b and c>d and c>e:
        maior = c
    if d>a and d>b and d>c and d>e:
        maior = d
    if e>a and e>b and e>c and e>d:
        maior = e

    print('O menor numero foi {} e o maior foi {}'.format(menor,maior))


if __name__ == '__main__':
    main()