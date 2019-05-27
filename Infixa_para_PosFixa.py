def remove_espaco(infixa):
    final = []
    flag = 0
    for i in range(len(infixa)):
        if infixa[i] == ' ':
            flag = 0
            continue
        elif infixa[i] == '\\' and flag == 0:
            flag = infixa[i]
            flag += infixa[i+1]
            final.append(flag)
            flag = 1
        elif flag != 0:
            flag = 0
            continue
        else:
            final.append(infixa[i])

    return final

def insere_ponto(infixa):
    final = []
    operador = ['*','.','+']
    tam = len(infixa)
    for i in range(tam):
        if i+1 <= tam-1:
            if infixa[i] not in operador and infixa[i+1] not in operador:
                if infixa[i] == '(' or infixa[i+1] == ')':
                    final.append(infixa[i])
                    continue
                final.append(infixa[i])
                final.append('.')
            else:
                final.append(infixa[i])
                if infixa[i] == '*' and infixa[i+1] not in operador and infixa[i+1] != ')':
                    final.append('.')
        else:
            if infixa[i-1] == '*' and final[-1] != '.' and infixa[i] != '*':
                final.append('.')
            final.append(infixa[i])
    return final

def verifica_precedencia(pilha,infixa):
    if pilha == '*':
        return True
    elif pilha == '.' and (infixa == '.' or infixa == '+'):
        return True
    elif pilha == '+' and infixa == '+':
        return  True
    else:
        return False

def transformacao_posfixa(infixa):
    operador = ['*','.','+']
    posfixa = []
    pilha = []
    for i in range(len(infixa)):
        if infixa[i] not in operador and infixa[i] != '(' and infixa[i] != ')':
            posfixa.append(infixa[i])
        elif infixa[i] == '(':
            pilha.append(infixa[i])
        elif infixa[i] == ')':
            if pilha == []:
                return 0
            while pilha[-1] != '(':
                posfixa.append(pilha.pop())
            if pilha[-1] == '(':
                pilha.pop()
        elif infixa[i] in operador:
            if pilha != []:
                while verifica_precedencia(pilha[-1], infixa[i]):
                    posfixa.append(pilha.pop())
                    if pilha == []:
                        break
            pilha.append(infixa[i])
    while pilha != []:
        posfixa.append(pilha.pop())
    return posfixa

def tratamento_expressoes(posfixa):
    operador = ['*','.','+']
    pilha = []
    for i in range(len(posfixa)):
        simbolo = posfixa[i]
        if simbolo not in operador and simbolo != '(' and simbolo != ')':
            pilha.append(simbolo)
        else:
            if pilha != []:
                op2 = pilha.pop()
                if simbolo == '*':
                    pilha.append(op2+simbolo)
                else:
                    if pilha != []:
                        op1 = pilha.pop()
                        valor = op1+op2
                        pilha.append(valor)
                    else:
                        print("\033[1;31m \n\t\tEXPRESSÃO INVÁLIDA!\033[0;0m")
                        return
            else:
                print("\033[1;31m \n\t\tEXPRESSÃO INVÁLIDA!\033[0;0m")
                return
    if pilha != []:
        pilha.pop()
    else:
        print("\033[1;31m \n\t\tEXPRESSÃO INVÁLIDA!\033[0;0m")
        return
    if pilha == []:
        print("\033[0;32m\n\t\tEXPRESSÃO VÁLIDA!\033[0;0m")
        return
    else:
        print("\033[0;32m\n\t\tEXPRESSÃO VÁLIDA!\033[0;0m")
        return


def comBarraViraOperando(posfixa):
    final = []
    for i in posfixa:
        if '\\' in i:
            final.append(i[1])
            continue
        final.append(i)
    return final

def main():
    a = ''
    infixa = remove_espaco(input())
    infixa = insere_ponto(infixa)
    posfixa = transformacao_posfixa(infixa)
    print('Infixa = ',a.join(infixa))
    if posfixa != 0:
        print('Posfixa = ',a.join(comBarraViraOperando(posfixa)))
        posfixa = tratamento_expressoes(posfixa)
    else:
        print("\033[1;31m \n\t\tEXPRESSÃO INVÁLIDA!\033[0;0m")


main()