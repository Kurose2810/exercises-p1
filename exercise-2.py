import table as tb
import util.log as log

# Elaborar un reporte de cosntos de produccion
def new_product():
    log.clear()
    log.section('NUEVO ARTICULO')
    description = log.question('Descripcion: ')
    up = log.question('Unidades Producidas: ', to=int)
    fc = log.question('Factor Costo: ', to=float)
    cf = log.question('Costo Fijo: ', to=float)
    cp = up * fc + cf
    return [description, up, fc, cf, cp]

report = tb.create_table('ARTICULO', 'UNIDADES PRODUCIDAS',
    'FACTOR COSTO', 'COSTO FIJO', 'COSTO DE PRODUCCION')

tb.append(report, new_product())
while log.question('AÑADIR ARTICULO?', qtype=log.OK_QUESTION):
    tb.append(report, new_product())

# 20 + 20 + 20 + 15 + 20
log.clear()
log.section('REPORTE')
log.message(95 * '-')
log.message('{title[0]:^20}{title[1]:^20}{title[2]:^20}{title[3]:^15}{title[4]:^20}'
    .format(title=tb.headings(report)))
log.message(95 * '-')
for product in tb.data(report):
    log.message('{title[0]:^20}{title[1]:^20}{title[2]:^20}{title[3]:^15}{title[4]:^20}'
        .format(title=product))
log.message(95 * '-')
msg_total = f'Total {len(tb.data(report))} articulos'
log.message(f'{msg_total:75}', end='')
log.message(f'{tb.sum_col(report, -1):^20}')