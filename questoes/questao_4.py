## QUESTÃO 4 ##
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos 
# a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o 
# valor da prestação como sendo o valor da casa a comprar dividido pelo número de 
# meses a pagar.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    vcasa = float(input('Digite o valor da casa: R$'))
    salario = float(input('Digite o valor do salario: R$'))
    anos = float(input('Digite a quantidade de anos a pagar: '))

    prestacao = vcasa / (anos * 12)

    if prestacao < (salario * 0.3):
        print('Emprestimo aprovado')
    else:
        print('Emprestimo não aprovado')


    
if __name__ == '__main__':
    main()
