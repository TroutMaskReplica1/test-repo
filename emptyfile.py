import random

i = 1

guess = int(input("Guess a digit  "))
x = random.randint(1,10)
if guess == x:
    print("winner!!1")
else:
    print(f"{x} was it")
    i + 1

y = random.randint(1,10)
guess2 = int(input("Try again <3 "))
if guess2 == y:
     print(f"Winner on try {i}")
else:print(f"try {i}, {y} was it :(")
i + 1

z = random.randint(1,10)
guess3 = int(input("try again <3"))
if guess3 == z:
     print(f"Winner on try {i}")
else:print(f"try {i}, {y} was it :(")
i + 1

a = random.randint(1,10)
guess4 = int(input("try again <3"))
if guess4 == a:
     print(f"Winner on try {i}")
else:print(f"try {i}, {z} was it :(")
i + 1

b = random.randint(1,10)
guess5 = int(input("try again <3"))
if guess5 == b:
     print(f"Winner on try {i}")
else:print(f"try {i}, {a} was it :(")
i + 1

c = random.randint(1,10)
guess6 = int(input("try again <3"))
if guess6 == c:
     print(f"Winner on try {i}")
else:print(f"try {i}, {b} was it :(")
i + 1

d = random.randint(1,10)
guess7 = int(input("try again <3"))
if guess7 == d:
     print(f"Winner on try {i}")
else:print(f"try {i}, {c} was it :(")
i + 1

e = random.randint(1,10)
guess8 = int(input("try again <3"))
if guess8 == e:
     print(f"Winner on try {i}")
else:print(f"try {i}, {d} was it :(")
i + 1

f = random.randint(1,10)
guess9 = int(input("try again <3"))
if guess9 == f:
     print(f"Winner on try {i}")
else:print(f"try {i}, {e} was it :(")
i + 1

g = random.randint(1,10)
guess10 = int(input("try again <3"))
if guess10 == g:
     print(f"Winner on try {i}")
else:print(f"try {i}, {f} was it :(")
i + 1