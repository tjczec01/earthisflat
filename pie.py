# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:00:15 2020

@author: tjcze
"""

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