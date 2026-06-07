import os 

os.path.exists("students.txt")
if os.path.exists("students.txt"):
    print("file exists ")
else:  print("file not found")

import random
names =["faizal","Ayesha","Zara"]
print(random.choice(names))

from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%m-%Y"))


import math
print(math.sqrt(144))