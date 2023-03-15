#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

#a = sys.argv[1]
#operator = sys.argv[2]
#b = sys.argv[3]

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = sys.argv[1]
operator = sys.argv[2]
b = sys.argv[3]

operator = ['+', '-', '*', '/']
#for i in operator:
if not ('+' in sys.argv[2] or '-' in sys.argv[2] or '*' in sys.argv[2]  or '/' in sys.argv[2]):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

elif sys.argv[2] == '+':
    print("{} + {} = {}".format(a, b, add(int(a), int(b))))

elif sys.argv[2] == '-':
    print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
elif sys.argv[2] == '*':
    print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
else:
    print("{} / {} = {}".format(a, b, div(int(a), int(b))))



