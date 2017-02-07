#!/usr/bin/python3

import sys

NUM_VALORES = 4

if len(sys.argv) != NUM_VALORES:
    sys.exit("Usage: python3 calculadora.py operacion operando1 operando2")

_, operacion, operando1, operando2 = sys.argv

try:
    operando1 = float(operando1)
    operando2 = float(operando2)
except ValueError:
    sys.exit("Los operandos han de ser floats. Gracias")

if operacion == "suma":
    print(operando1 + operando2)
elif operacion == "div":
    try:
        print(operando1 / operando2)
    except ZeroDivisionError:
        sys.exit("No sé dividir por cero")
