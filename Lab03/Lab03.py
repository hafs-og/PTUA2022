# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 14:31:59 2022

@author: admin
"""




x = y =2
print(x)

import math

r=5

volume=4/3*math.pi*r**3

print(volume)

book = 24.95
discount = 0.40
shipping_cost= 3

for i in range(60):
    price = book -(book*discount)
    if i == 1:
        price = price + shipping_cost
    if i > 1:
        price = price + 0.75

print(price)

