from termcolor import colored
from time import sleep

def textZombieDice():
    for i in range(5):
        print(colored(" ZOMBIE DICE ".center(50, '='), 'red', attrs=['bold']))
        sleep(0.3)
        print(colored(" ZOMBIE DICE ".center(50, '='), 'blue', attrs=['bold']))
        sleep(0.3)