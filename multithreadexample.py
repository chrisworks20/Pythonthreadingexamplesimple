
import time
from threading import Thread

def func1():
    print("Thread A")
    x = 20
    for i in range(x):
        print(i)
        time.sleep(1)
    print("Done A")   

def func2():
    print("Thread B")
    x = 35
    for i in range(x):
        time.sleep(0.5)
        print(i)
    print("Done B")

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()