from time import sleep
import os

hi = os.environ.get('HELLO')

seconds = 1

while(True):
    sleep(1)
    print("logging...", seconds, "Env Var: ", hi)
    seconds +=1