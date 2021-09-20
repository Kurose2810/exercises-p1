import util.log as log
# Aprender tablas de multiplicar

log.message('Programa para aprender las tablas de multiplicar')
n  = log.question('Con que numero quieres practicar ? ', to=int)
correctness = 0

for i in range(1, 11):
    ans = log.question(f'{i} * {n} = ', to=float)
    if ans == i * n:
        correctness += 1
        log.message('Valor correcto')
    else:
        log.message(f'Lo siento se he equivocado. La respuesta correcta era {i * n}')    

log.message(f'Has acertado {correctness} de 10 numeros')