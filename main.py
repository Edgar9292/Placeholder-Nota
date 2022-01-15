disciplina = input('Digite a disciplina:')
nota_final = input('Digite a nota final(0 a 100):')
semestre = input ('Digite o semestre (1 a 4):')
if nota_final>='50' and int(semestre) !=1:
    print('Você foi aprovado com media final no valor de', disciplina,nota_final)
else:
    print('Você foi reprovado')