import util.log as log
from functools import reduce
from operator import add

log.clear()

history = []
name = log.question('NOMBRE: ')
amount = log.question('CANTIDAD INICIAL: ', to=float)
while log.question('Desea realizar un movimiento?', log.OK_QUESTION):
    mov = log.question('Inserte movimiento [+: depositos | -: retiros]: ', to=float)
    history.append(mov)

head = f'{"MOVIMIENTO":^15}{"DEPOSITO":^10}{"RETIRO":^10}{"SALDO":^10}'
width = len(head)

log.clear()
log.message(f'CUENTAHABIENTE: {name}')
log.message(f'SALDO INICAL: {amount}')
log.message(width * '-')
log.message(head)
log.message(width * '-')
for n, mov in enumerate(history):
    log.message(f'{n:^15}', end='')
    mov_space = f'{mov:>10}{10 * " "}' if mov >= 0 else f'{abs(mov):>20}'
    log.message(mov_space, end='')
    amount += mov
    log.message(f'{amount:^10}')
log.message(width * '-')
log.message('{msg:^15}{dep:^10}{ret:^10}{sal:^10}',
    msg='Totales',
    dep=reduce(
        lambda acc, curr: add(acc,curr) if curr >= 0 else acc, history, 0),
    ret=reduce(
        lambda acc, curr: add(acc, abs(curr)) if curr < 0 else acc, history, 0),
    sal=amount)
