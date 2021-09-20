from util.question import INPUT_QUESTION, OK_QUESTION
import util.question as _questions
import os

def message(content, end='\n', trimed=False, size=20, **kwargs):
    text = content.format(**kwargs)
    if trimed:
        text = trim(text, size=size)
    print(text, end=end)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def section(section, decorator='---'):
    message(f'{decorator} {section} {decorator}')

def trim(s, size, end='...'):
    lenght = len(s)
    if lenght > size:
        return s[:size - len(end)] + end
    
    return s


def question(message, qtype=INPUT_QUESTION, to=None):
    ans = ''
    if qtype == INPUT_QUESTION:
        ans = _questions.qinput(message)
    elif qtype == OK_QUESTION:
        ans = _questions.qagree(message)
    return to(ans) if to else ans