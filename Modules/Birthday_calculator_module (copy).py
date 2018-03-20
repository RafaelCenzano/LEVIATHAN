https://repl.it/@SavageCoder77/quadratic-formula

#IMPORT
import time
import math
from decimal import Decimal 

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return (x * y)

def divide(x, y):
  return x / y

def squareroot(x):
  return math.sqrt(x)

def dotprint():
  print ' '

def dotprint2():
  dotprint()
  dotprint()

def wait():
  time.sleep(1)

#MAIN

#title
print ('######################################################################')
print ('###             This is a Quadratic Formula Calculator             ###')
print ('###                        Created for Fun                         ###')
print ('######################################################################')

time.sleep(2)
dotprint2()
dotprint2()

#description
print ('This is a program that can calculate a Quadratic Equation using the Quadratic Formula')
dotprint2()
time.sleep(2)

print('What your base equation should be:')
print('ax^2 + bx + c = 0')
dotprint2()
wait()

#displaying quadratic formula
print('Quadratic Formula:')
print('          ___________')
print('-b  +-  -/ b^2 - 4ac ')
print('_____________________')
print('         2a          ')
dotprint2()

#asking a b c inputs
a = Decimal(raw_input('What is a: '))
b = Decimal(raw_input('What is b: '))
c = Decimal(raw_input('What is c: '))
dotprint2()

#formula with numbers
bneg = Decimal(multiply(int(b), -1))
print('your formula:')
print('          ____________________')
print('{}  +-  -/ {}^2 - 4({})({}) ').format(bneg, b, a, c)
print('______________________________')
print('            2({})            ').format(a)
dotprint2()
time.sleep(2)

bsq = Decimal(multiply(int(b), int(b)))
fourtimesa = Decimal(multiply(int(a), -4))
discriminent = Decimal(multiply(int(fourtimesa), int(c)))
bottom = Decimal(multiply(2, int(a)))
rightside = Decimal(add(int(discriminent), int(bsq)))

print('b squared')
print('{} * {}').format(b, b)
print('= {}').format(bsq)
dotprint()
wait()
print('finding the discriminent')
print('-4 * {}').format(a)
time.sleep(2)
print('then')
print('{} * {}').format(fourtimesa, c)
print('= {}').format(discriminent)
dotprint()
time.sleep(2)
print('{} + {}').format(bsq, discriminent)
print('= {}').format(rightside)
dotprint2()
time.sleep(2)

#post math formula
print('your formula after first step:')
print('This ')
print('         _______')
print('{}  +-  -/ {} ').format(bneg, rightside)
print('_________________')
print('        {}      ').format(bottom)
dotprint2()
wait()

print('Any simplifications from now might not be clean but they will be right')
dotprint2()
time.sleep(3)

if rightside >= 0:
  print('We will first try with square rooting {}').format(rightside)
  dotprint()
  sqrtright = (squareroot(Decimal(rightside)))
  print('{}  +-  {} ').format(bneg, sqrtright)
  print('_____________')
  print('     {}    ').format(bottom)
  dotprint2()
  wait()
  
  print('Now we will divide both sides by {}').format(bottom)
  dotprint()
  dividright = divide(Decimal(sqrtright), Decimal(bottom))
  dividbneg = divide(Decimal(bneg), Decimal(bottom))
  print('{} +- {}').format(dividbneg, dividright)
  dotprint2()
  wait()
  
  print('Now we will show all the simplifications')
  posanswer = add(Decimal(dividbneg), Decimal(dividright))
  neganswer = subtract(Decimal(dividbneg), Decimal(dividright))
  print('x = {}, {}').format(posanswer, neganswer)
  
else:
  print('This equation has no roots but two imaginary roots')