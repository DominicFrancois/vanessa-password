import string
from random import sample, choice

chars = string.ascii_letters + string.digits
lenght = 20
gen = ''.join(choice(chars) for _ in range(lenght))       
plog = 'plog.txt'

with open(plog, 'a') as out:
    out.write(gen + '\n')

print("Password generated")
