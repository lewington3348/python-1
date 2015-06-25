"""snocones"""

import colors as c
from utils import ask

intro = c.magenta + '''LETS TEST HOW FABILOOS U ARE, YYYYAAAAAAAYYYYY!!!''' + c.reset

def q1():
    answer = ask(c.orange + 'WHAT COLOR WERE THE FABILOOS UNICORNS?' + c.reset) 
    if answer =='pink':
        print('so nice and purty')
        return True
    print('incorect :(======')
    return False

def q2(): 
    answer = ask(c.magenta + 'WHAT WERE THE UNICORNS DANCING ON?')
    if answer.startswith ('rainbows'):
        print('also so nice an purty')
        return True
    print('u make me sad :(=======')    
    return False

def q3():
    answer =ask(c.magenta + 'use one word to describe the texture of their magical fur.')
    if answer == 'smiles':
        print('yyyeeeeeaaaahhhh')
        return True
    print('eradicate from the world, }:(========')
    return False

questions = [q1,q2,q3]
