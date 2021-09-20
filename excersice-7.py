import util.log as log

def new_student():
    name = log.question('Nombre: ')
    grade = 0
    for parcial in range(1, 4):
        tmp = log.question(f'Calificacion parcial {parcial}: ', to=float)
        if tmp > 7:
            grade += tmp
        else:
            grade = 'NA'
            return (name, grade)

    return (name, grade / 3)

alumnos = []
while log.question('Ingresar alumno?', qtype=log.OK_QUESTION):
    alumnos.append(new_student())

head = f'{"NOMBRE":^20}{"CALIFICACION":^15}'
width = len(head)
log.message(width * '-')
log.message(head)
log.message(width * '-')
for name, grade in alumnos:
    log.message(f'{name:20}', trimed=True, end='')
    log.message(f'{grade:>15.2}')

log.message(width * '-')
log.message(f'Alimnos {len(alumnos)}')

