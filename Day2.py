#!/bin/python3

import math
import os
import random
import re
import sys


def solve(meal_cost, tip_percent, tax_percent):
    tip = (tip_percent*meal_cost)/100
    tax= (tax_percent*meal_cost)/100
    total = meal_cost + tip + tax
    y = round(total,0)
    print(int(y))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
