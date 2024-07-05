import string
import random
import os
x=100

while not (x == 0) :
            
  tokens = (''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(16)))
  x -= 1
  a_file = open("nitro.txt", "a" )
  a_file.write('discord.gift/'+tokens + '\n')
  a_file.close()
