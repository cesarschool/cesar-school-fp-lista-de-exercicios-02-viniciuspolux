## QUESTÃO 8 ##
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    ano = int(input('Informe o ano: '))
    bisexto = ano % 4
    bisexto2 = ano % 400
    if bisexto == 0:
        if ano % 100 != 0:
            bi = True
        else:
            bi = False
    elif bisexto2 == 0:
        if ano % 100 != 0:
            bi = True
        else:
            bi = False
    else:
        bi = False

    if bi == True:
        mes = int(input('Informe o mes em numero: '))
        dia = int(input('Informe o dia: '))
        if mes == 2:
            if dia <= 28:
                dia += 1
            elif dia == 29:
                dia = 1
                mes = mes + 1
        elif mes != 2:
            if dia <= 29:
                dia += 1
            elif dia == 30:
                dia = 1
                mes = mes + 1
            elif dia == 31 and mes == 12:
                dia = 1
                mes = 1
                ano += 1
    elif bi == False:
        mes = int(input('Informe o mes em numero: '))
        dia = int(input('Informe o dia: '))
        if mes == 2:
            if dia <= 27:
                dia += 1
            elif dia == 28:
                dia = 1
                mes = mes + 1
        elif mes != 2:
            if dia <= 29:
                dia += 1
            elif dia == 30:
                dia = 1
                mes = mes + 1
            elif dia == 31 and mes == 12:
                dia = 1
                mes = 1
                ano += 1

    print('O dia seguinte é {}-{}-{}'.format(dia, mes, ano))


    
if __name__ == '__main__':
    main()
