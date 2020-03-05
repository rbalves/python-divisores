ler_matricula = lambda: int(input())

MENSAGEM_MAIOR_QUE_ZERO = "VALOR PRECISA SER MAIOR QUE 0"

eh_divisor = lambda dividendo, divisor: dividendo % divisor == 0

qtde_funcionarios = 2

matriculas = []

for i in range(qtde_funcionarios):
    matricula = ler_matricula()

    while matricula < 1:
        print(MENSAGEM_MAIOR_QUE_ZERO)
        matricula = ler_matricula()

    matriculas.append(matricula)

for matricula in matriculas:
    salario = 0
    for i in range(matricula):
        divisor = i + 1
        if eh_divisor(matricula, divisor):
            salario += divisor
    print(salario)
