from factorial.factorial import fac
from exp_root.exponentiation import *
from exp_root.root import *
from logarithm.logarithm import *

while True:
    print('\nEnter "fac" to calculate factorial')
    print('Enter "exp" to exponentiate')
    print('Enter "root" to calculate root')
    print('Enter "log" to calculate logarithm')

    while True:
        try:
            choice = input('Your choice: ')
            assert (choice == 'fac') or (choice == 'exp') or (choice == 'root') or (choice == 'log')
            break
        except:
            print('Error! Try again.')

    if choice == 'fac':
        while True:
            try:
                n = int(input('Enter a natural number: '))
                assert n >= 0
                break
            except:
                print('Error! Try again.')
        print('Result:', fac(n))

    if choice == 'exp':
        while True:
            try:
                pow = input('Enter power (2 / 3): ')
                assert (pow == '2') or (pow == '3')
                break
            except:
                print('Error! Try again.')
        while True:
            try:
                n = float(input('Enter a number: '))
                break
            except:
                print('Error! Try again.')
        if pow == '2':
            print('Result: ', exp2(n))
        if pow == '3':
            print('Result: ', exp3(n))

    if choice == 'root':
        while True:
            try:
                pow = input('Enter "2" for square root and "3" for cube root: ')
                assert (pow == '2') or (pow == '3')
                break
            except:
                print('Error! Try again.')
        while True:
            try:
                n = float(input('Enter a number: '))
                if pow == '2':
                    assert n > 0
                break
            except:
                print('Error! Try again.')
        if pow == '2':
            print('Result: ', round(root2(n), 4))
        if pow == '3':
            print('Result: ', round(root3(n), 4))

    if choice == 'log':
        print('\nEnter "log" to calculate logarithm')
        print('Enter "ln" to calculate natural logarithm')
        print('Enter "lg" to calculate common logarithm')
        while True:
            try:
                choice = input('Your choice: ')
                assert (choice == 'log') or (choice == 'ln') or (choice == 'lg')
                break
            except:
                print('Error! Try again.')
        if choice == 'log':
            while True:
                try:
                    a = float(input('Enter base: '))
                    assert (a > 0) and (a != 1)
                    break
                except:
                    print('Error! Try again.')
            while True:
                try:
                    b = float(input('Enter a number: '))
                    assert b > 0
                    break
                except:
                    print('Error! Try again.')
            print('Result:', round(log(a, b), 4))
        else:
            while True:
                try:
                    b = float(input('Enter a number: '))
                    assert b > 0
                    break
                except:
                    print('Error! Try again.')
            if choice == 'ln':
                print('Result:', round(ln(b), 4))
            if choice == 'lg':
                print('Result:', round(lg(b), 4))

    s = input('Enter "+" to continue and "-" to exit: ')
    while (s != "+") and (s != "-"):
        s = input('Error! Try again. ')
    if s == "+":
        continue
    else:
        break