"""snocones"""

import colors as c
from utils import ask

intro = c.magenta + '''LETS TEST HOW FABILOOS U ARE, YYYYAAAAAAAYYYYY!!!''' + c.reset

def q1():
    answer = ask(c.orange + 'What are the swaggiest animals ever?' + c.reset) 
    if answer =='narwhals':
        print('so nice and purty')
        return True
    print('incorect :(======')
    return False

def q2(): 
    answer = ask(c.magenta + 'are narwhals swaggy?')
    if answer == 'yes':
        print('yes')
        return True
    print('u make me sad :(=======')    
    return False

def q3():
    answer =ask(c.magenta + 'should narwhals be the dominant species of the world?')
    if answer == 'yes':
        print('yyyeeeeeaaaahhhh')
        return True
    print('eradicate from the world, }:(========')
    return False

def q4():
    answer =ask(c.magenta + 'what is the average life span of a narwhal in years?')
    if answer == '25-30':
        print('yes')
        return True
    print('no')
    return False



questions = [q1,q2,q3,q4]
