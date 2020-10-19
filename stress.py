'''
CPU Stressor
'''

from os import cpu_count
import threading

# I think the use of threads is holding it back, switch to processes?

def dummy_load(check):
    '''
    Trying to stress CPUs with Fibonacci sequence Could do with
    something more controllable, maybe only stress a certain percentage of
    the core? (e.g. 90%?)
    '''
    (x, y) = 1, 1
    while check():
        res = x + y
        x, y = y, res

class Stressor:
    run = False

    def __init__(self):
        self.cpus = cpu_count()
    def start(self):
        self.run = True
        for _ in range(self.cpus):
            threading.Thread(target=dummy_load, args=(lambda : self.run,)).start()
    def stop(self):
        self.run = False
