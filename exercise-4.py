import util.log as log
import table as tb

def new_product(owner: str):
    log.clear()
    cap = owner.upper()
    log.section(f'NUEVO ARTICULO: {cap}')
    des = log.question('Descripcion: ')
    amount = log.question('Cantidad de articulos: ', to=int)
    pu = log.question('Precio Unitario: ', to=float)
    pt = amount * pu
    return [des, amount, pu, pt]

factura = tb.create_table('ARTICULO', 'CANTIDAD',
    'PRECIO UNITARIO', 'TOTAL')
name = log.question('NOMBRE DEL CLIENTE: ')
tb.append(factura, new_product(name))

while log.question('Ingresar otro articulo? ', qtype=log.OK_QUESTION):
    tb.append(factura, new_product(name))

width = len(tb.headings(factura)) * 20
log.clear()
log.message(f'Nombre del cliente: {name}')
log.message( width * '-')
for k in tb.headings(factura):
    heading = log.trim(k, 20)
    log.message(f'{heading:^20}', end='')
log.message('')
log.message(width * '-')
for row in tb.data(factura):
    for content in row:
        trimmed = log.trim(content, size=20) if isinstance(content, str) else content
        log.message(f'{trimmed:^20}', end='')
    log.message('')
log.message(width * '-')
subtotal = tb.sum_col(factura, -1)
i = subtotal * .15
total = subtotal + i
log.message(f'Subtotal: {subtotal}')
log.message(f'Impuesto: {i}')
log.message(f'Total: {total}')
log.message(width * '-')