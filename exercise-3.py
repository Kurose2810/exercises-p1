import table as tb
import util.log as log

# Elaborar un reporte de cosntos de produccion
def new_product():
    log.clear()
    log.section('NUEVO ARTICULO')
    description = log.question('Descripcion: ')
    cp = log.question('Costo De Produccion: ', to=float)
    u = cp * 1.2
    i = .15 * (cp + u)
    pv = cp + u + i
    return [description, cp, u, i, pv]
    
report = tb.create_table('ARTICULO', 'COSTO DE PRODUCCION',
    'UTILIDAD', 'IMPUESTO', 'PRECIO DE VENTA')

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
msg_total = f'Total {len(tb.data(report))}'
log.message(f'{msg_total:20}', end='')
cost_values = tb.data(report)[:,1:].astype(float)
log.message('{title[0]:^20.2f}{title[1]:^20.2f}{title[2]:^15.2f}{title[3]:^20.2f}'
    .format(title=cost_values.sum(axis=0)))