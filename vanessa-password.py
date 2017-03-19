#Password Generator
import string, random

#Password lenght
pl = 15 

#Accepted password characters
pc = string.printable[0:63]


print(*random.sample(pc,pl), sep='')