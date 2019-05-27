
class Stack:
    def __init__(self):
        self.stack = list()
    def push(self,data):
            self.stack.append(data)
            return True
    def pop(self):
        if len(self.stack)<=0:
            return ""
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def top(self):
        top=self.pop()
        self.push(top)
        return top

class Automato:
    def __init__(self):
        self.alfabeto = []
        self.estados = []
        self.qtEstados = int
        self.Matriz = {}
        self.estadoInicial = int
        self.estadofinal = int
        self.estadosfinais = []
        self.qtEstadosFinais = int

    def une_alfabeto(self, a, b):
        i = 0
        j = 0
        alfabtotal = []
        alfabtotal.append(a)
        while i < len(alfabtotal):
            while j < len(b):
                if alfabtotal[i] != b[j]:
                    j += 1
                else:
                    k = j
                    while k < len(b) - 1:
                        b[k] = b[k + 1]
                        k += 1
                    del (b[len(b) - 1])
            i += 1

        if len(b) != 0:
            alfabtotal.append(b)
        return alfabtotal

    def base(self, simbolo):
        base = Automato()
        base.alfabeto.append(simbolo)
        base.qtEstados = 2
        base.estados.append(0)
        base.estados.append(1)

        base.Matriz[(0, simbolo)] = 1

        # print(" 00:",self.Matriz[0][0].qtEstados )
        # print(" 10:",self.Matriz[1][0].qtEstados )
        base.estadoInicial = 0
        base.qtEstadosFinais = 1
        base.estadosfinais.append(1)
        return base

    def concatenacao(self, a1, a2):
        automato = Automato()
        automato.alfabeto = self.une_alfabeto(a1.alfabeto, a2.alfabeto)
        automato.qtEstados = a1.qtEstados + a2.qtEstados

        automato.estados = a1.estados.copy()
        for i in range(len(a2.estados)):
            automato.estados.append(a1.qtEstados + a2.estados[i])

        automato.Matriz = a1.Matriz.copy()
        for i in a2.Matriz.keys():
            try:
                automato.Matriz[(i[0] + a1.qtEstados, i[1])] = a2.Matriz.get(i) + a1.qtEstados
            except:
                b = list(a2.Matriz.get(i))
                lista = [x + a1.qtEstados for x in b]
                automato.Matriz[(i[0] + a1.qtEstados, i[1])] = tuple(lista)

        automato.Matriz[(a1.qtEstados - 1, '&')] = a1.qtEstados

        automato.estadoInicial = 0
        automato.estadosfinais.append(automato.qtEstados - 1)
        automato.qtEstadosFinais = 1

        # print("estado inicial:", automato.estadoInicial)
        # print("estado final:", automato.estadosFinais)

        return automato

    def uniao(self, a1, a2):
        automato = Automato()
        automato.alfabeto = self.une_alfabeto(a1.alfabeto, a2.alfabeto)
        automato.qtEstados = a1.qtEstados + a2.qtEstados + 2

        for i in range(automato.qtEstados):
            automato.estados.append(i)

        automato.Matriz[(0, '&')] = a1.estadoInicial + 1, a2.estadoInicial + a1.qtEstados + 1

        for i in a1.Matriz.keys():
            try:
                automato.Matriz[(i[0] + 1, i[1])] = a1.Matriz.get(i) + 1
            except TypeError:
                b = list(a1.Matriz.get(i))
                lista = [x + 1 for x in b]
                automato.Matriz[(i[0] + 1, i[1])] = tuple(lista)

        for i in a2.Matriz.keys():
            try:
                automato.Matriz[(i[0] + a1.qtEstados + 1, i[1])] = a2.Matriz.get(i) + a1.qtEstados + 1
            except TypeError:
                b = list(a2.Matriz.get(i))
                lista = [x + a1.qtEstados + 1 for x in b]
                automato.Matriz[(i[0] + a1.qtEstados + 1, i[1])] = tuple(lista)

        if ((a1.qtEstados, '&')) in automato.Matriz.keys():
            automato.Matriz[(a1.qtEstados, '&')] = a1.Matriz.get((a1.qtEstados, '&')), automato.qtEstados - 1
        else:
            automato.Matriz[(a1.qtEstados, '&')] = automato.qtEstados - 1

        if (a2.qtEstados + a1.qtEstados, '&') in automato.Matriz.keys():
            automato.Matriz[(a2.qtEstados + a1.qtEstados, '&')] = a2.Matriz.get(
                (a2.qtEstados + a1.qtEstados, '&')), automato.qtEstados - 1
        else:
            automato.Matriz[(a2.qtEstados + a1.qtEstados, '&')] = automato.qtEstados - 1

        automato.estadoInicial = 0
        automato.estadosfinais.append(automato.qtEstados - 1)
        automato.qtEstadosFinais = 1

        return automato

    def fechoDeKleene(self, automato):
        novo_automato = Automato()
        novo_automato.alfabeto = self.une_alfabeto([""], automato.alfabeto)

        novo_automato.qtEstados = automato.qtEstados + 2
        # preenchendo os estados do novo automato
        for i in range(novo_automato.qtEstados):
            novo_automato.estados.append(i)

        # preenchendo as transicoes do automato no automato novo
        for i in automato.Matriz.keys():
            try:
                novo_automato.Matriz[(i[0] + 1, i[1])] = automato.Matriz.get(i) + (
                            novo_automato.qtEstados - automato.qtEstados) - 1
            except:
                b = list(automato.Matriz.get(i))
                lista = [x + 1 for x in b]
                novo_automato.Matriz[(i[0] + 1, i[1])] = tuple(lista)

        novo_automato.Matriz[(0, '&')] = (1, novo_automato.qtEstados - 1)
        novo_automato.Matriz[(automato.qtEstados, '&')] = (
        novo_automato.qtEstados - automato.qtEstados - 1, novo_automato.qtEstados - 1)

        novo_automato.estadoInicial = 0
        novo_automato.estadosfinais.append(novo_automato.qtEstados - 1)
        novo_automato.qtEstadosFinais = 1
        return novo_automato



class transicoes():
    def __init__(self):
        self.estado = [] #int
        self.qtEstado = 0

class automato():
    def __init__(self):
        self.alfabeto = [] # string
        self.estado = []   #int
        self.qtEstado = 0
        self.Transicao = [[transicoes()],[transicoes()]]
        self.estadoInicial = 0
        self.estadosFinais = [] #int
        self.qtEstFinais = 0

    def Automato_base(simbolo):
        base = automato()
        base.alfabeto = simbolo
        base.qtEstado = 2
        base.estado.append(0)
        base.estado.append(1)
        base.Transicao[0][0].qtEstado = 1
        base.Transicao[0][0].estado.append(1)
        base.Transicao[1][0].qtEstado = 0
        base.estadoInicial = 0
        base.qtEstFinais = 1
        base.estadosFinais.append(1)
        return base

#    def UneAlfabeto(a,b):

    def concatenacao(a,b):
        novo = automato()
        novo.alfabeto = UneAlfabeto(a.alfabeto,b.alfabeto)
        novo.qtEstado = a.qtEstado+b.qtEstado
        for i in range(novo.qtEstado):
            novo.estado.append(a.estado[i])



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

def ordena(self):
    if self.isalpha():
        return 1
    return 0
def show1(matriz):

    listaK=[]
    listaL = []
    print('\n\t\t')
    for i,j in matriz.items():
        q = j
        k,l=i
        listaK.append(k)
        listaL.append(l)
    print('\n')
    listaL = list(set(listaL))
    listaL.sort(key=ordena)
    print('\t\t X  ', end='')
    [print(i, end='     ') for i in listaL]
    print()
    for b in listaK:
        print('   - ', b,end='   ')
        for i in range(len(listaL)):
            if (b,listaL[i]) in matriz:
                _, c = (b, listaL[i])
            try:
                c = listaL.index(c)
            except:
                print()
                continue
            for i in range(c):
                print(' ',end='')
                c -= 1
            print(' ',q)
        print()



def show2(matriz):
    print('\n\n')
    for k,v in matriz.items():
        i,j = k
        print(f'Se no estado q{i} e entra o símbolo {j}, logo vai para os estado(s) q{v}')



def main():
    a = ''
    infixa = remove_espaco(input())
    infixa = insere_ponto(infixa)
    posfixa = transformacao_posfixa(infixa)
    expPos = posfixa
    print('Infixa = ',a.join(infixa))
    if posfixa != 0:
        print('Posfixa = ',a.join(comBarraViraOperando(posfixa)))
        posfixa = tratamento_expressoes(posfixa)
    else:
        print("\033[1;31m \n\t\tEXPRESSÃO INVÁLIDA!\033[0;0m")


    pilha = Stack()
    aut = Automato()
    operador = ['(', ')', '*', '+', '.']
    for x in range(0, len(expPos)):
        simbolo = expPos[x]

        if simbolo not in operador:
            pilha.push(aut.base(simbolo))
        else:
            if pilha.size() != 0:
                if simbolo == '*':
                    pilha.push(aut.fechoDeKleene(pilha.pop()))
                else:
                    op2 = pilha.pop()
                    if pilha.size() != 0:
                        op1 = pilha.pop()
                        if simbolo == '.':
                            pilha.push(aut.concatenacao(op1, op2))
                        else:
                            if simbolo == '+':
                                pilha.push(aut.uniao(op1, op2))

    afn = pilha.pop()
    a = afn.Matriz.keys()
    print(a)
    print("AUTOMATO FINAL", afn.Matriz)
    print("ESTADO INICIAL", afn.estadoInicial)
    print("ESTADOS FINAIS", afn.estadosfinais)
    print(show2(afn.Matriz))




main()

