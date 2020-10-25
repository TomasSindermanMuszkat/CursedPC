__version__ = '0.2.1'

from multiprocessing import Process, active_children, cpu_count, Pipe
import os
import signal
import sys
import time


FIB_N = 100
try:
    DEFAULT_CPU = cpu_count()
except NotImplementedError:
    DEFAULT_CPU = 1


def loop(conn):
    proc_info = os.getpid()
    conn.send(proc_info)
    conn.close()
    while True:
        fib(100)


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def sigint_handler(signum, frame):
    procs = active_children()
    for p in procs:
        p.terminate()
    os._exit(1)


signal.signal(signal.SIGINT, sigint_handler)

def stress(proc_num = cpu_count(), exec_time = 60):
    procs = []
    conns = []
    for i in range(proc_num):
        parent_conn, child_conn = Pipe()
        p = Process(target=loop, args=(child_conn,))
        p.start()
        procs.append(p)
        conns.append(parent_conn)

    for conn in conns:
        try:
            print(conn.recv())
        except EOFError:
            continue

    time.sleep(exec_time)

    for p in procs:
        p.terminate()