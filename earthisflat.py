# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 04:50:10 2020

@author: tjcze
"""
import math
import decimal

class pie():
       
       def __init__(self, ndigit):
               self.ndigit = int(ndigit)
               decimal.getcontext().prec=(ndigit+1)
       
       def chud(self):
              c1 = decimal.Decimal(12.0/(640320.0**(3.0/2.0)))
              
              c1 = decimal.Decimal(12.0)/decimal.Decimal(640320.0**(3/2))
              def digitsf(x):
                    return int(x)
              
              def factorial(n):
                  def factorialf(n):
                          fact = 1
                          for num in range(2, int(n + 1)):
                              fact *= num
                          return fact 
                  if n < 2:
                      return 1
                  else:
                      return decimal.Decimal(decimal.Decimal(n) * decimal.Decimal(factorialf(n-1)))
              pi = decimal.Decimal(0.0)
              for k in range(self.ndigit):
                     ki = decimal.Decimal(k)
                     top = decimal.Decimal(factorial(decimal.Decimal(6.0)*ki)) * decimal.Decimal((decimal.Decimal(13591409) + decimal.Decimal(545140134) * decimal.Decimal(int(ki))))
                     bottom = decimal.Decimal(factorial(decimal.Decimal(3.0)*ki)) * decimal.Decimal((factorial(decimal.Decimal(ki))**decimal.Decimal(3.0)) * (decimal.Decimal(-640320.0)**decimal.Decimal(decimal.Decimal(decimal.Decimal(3.0)*ki))))
                     pi = decimal.Decimal(pi) + decimal.Decimal(float(top/bottom))
              final = (c1*pi)**-1
              return final
       
       def srin(self):
              c2 = decimal.Decimal(decimal.Decimal(2.0)*(decimal.Decimal(2.0)**decimal.Decimal(1/2)))/decimal.Decimal(9801.0)
              def digitsf(x):
                    return int(x)
              
              def factorial(n):
                  def factorialf(n):
                          fact = 1
                          for num in range(2, int(n + 1)):
                              fact *= num
                          return fact 
                  if n < 2:
                      return 1
                  else:
                      return decimal.Decimal(decimal.Decimal(n) * decimal.Decimal(factorialf(n-1)))
              pi2 = decimal.Decimal(0.0)
              for k2 in range(self.ndigit):
                     kj = decimal.Decimal(k2)
                     top2 = decimal.Decimal(factorial(decimal.Decimal(4.0)*kj)) * decimal.Decimal((decimal.Decimal(1103) + decimal.Decimal(26390) * decimal.Decimal(int(kj))))
                     bottom2 = decimal.Decimal(factorial(kj)**decimal.Decimal(4.0)) * decimal.Decimal(decimal.Decimal(396.0)**decimal.Decimal(decimal.Decimal(4.0)*kj)) 
                     pi2 = decimal.Decimal(pi2) + decimal.Decimal(float(top2/bottom2))
              final2 = (c2*pi2)**-1
              return final2
       def pieavg(self):
              a1 = self.chud()
              a2 = self.srin()
              a3 = (a1 + a2)/2
              return a3

pie = float(pie(25).chud())
Mm = float(1E6)
RE = float(6.3781 * Mm)
circumferencea = float(2.0 * pie * RE) # [m]
circumference = circumferencea/1000.0 # [Km]
alpha = 360.0 / circumference
h1 = float(input("Height of inital object in meters --> "))
h2 = float(input("Height of measured object in meters --> "))
D1 = math.sqrt(2.0*RE*h1 + (h1**2.0))
D2 = math.sqrt(2.0*RE*h2 + (h2**2.0))
terma = 1.0 + (h1/RE)
alphab = math.acos(1.0/terma)
arclength = alphab*RE
D_t = round(D1 + D2)
D_tkm = round((D1 + D2)/1000.0, 1)
print("Angle of curvature of the earth {}° per kilometer".format(round(alpha, 3)))
print('Total distance from height of inital object to measured object = {:,} meters'.format(D_t))
print('Total distance from height of inital object to measured object = {} kilometers'.format(D_tkm))
print("Total arc length {:,} meters".format(round(arclength)))

       
       