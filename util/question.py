INPUT_QUESTION = 1
OK_QUESTION = 2

def qinput(question, dtype=str):
    ans = input(question)
    return dtype(ans)

def qagree(question: str):
    question = question[:-1] if question[-1] == '?' else question
    ans = input(question.strip() + ' [ YES / NO ] ? ')
    return True if ans[0] == 'Y' or ans[0] == 'y' else False
