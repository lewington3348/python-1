"""hi"""

import colors as c  

def ask(question):
    print(question)
    answer = input('>' + c.green).lower().strip()
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear)
    name = ask('VUT IS UR NAME?')






