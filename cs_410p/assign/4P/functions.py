# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 08:55:05 2022

@author: David luby

# CS 410P - Program assignmetn 4P

# create a function to convert celsius to farenheit
    # include wind chill factor and heat index
        # print in columns
        # for integers between -20 and 50 C
        # continuous intake of ranges until non integer entered

"""


def compute_wind_chill(x,y):
    tempC = list(range(x,y+1,1))
    tempF = []
    velocity = list(range(5,45,5))
    wc = []
    for y in tempC:
        tempF.append(y *9/5 + 32)
    ext = 0
    for x in tempF:
        if x < 0:
            ext +=1
        for V in velocity:
            if x > 50:
                wc.append(000)
            else:
                wc.append(35.74 +.6215*x -35.75*V**.16 +.4275*x*V**.16)
    for k in wc:
        if k < 0:
            ext +=1
            
    print("\n{0:^10}{1:^10}{2:^10}{3:^10}{4:^10}{5:^10}{6:^10}{7:^10}{8:^10}{9:^10}"
          .format("Celcius","Fahr","5 mph","10 mph","15 mph","20 mph",
                  "25 mph","30 mph","35 mph","40 mph"))

    i = -8
    j = -1
    while j < len(tempC)-1:
        while i < len(wc):
            j +=1
            i +=8
            print("{0:^10}{1:^10.1f}{2:^10.2f}{3:^10.2f}{4:^10.2f}{5:^10.2f}"
              "{6:^10.2f}{7:^10.2f}{8:^10.2f}{9:^10.2f}".format(tempC[j],
              tempF[j],wc[i],wc[i+1],wc[i+2],wc[i+3],wc[i+4],wc[i+5],wc[i+6],
              wc[i+7]))
            if i == (len(wc)-7) or j == (len(tempC)-1):
                print("\nExtreme Cold: ",ext)
                break
    
    
def compute_heat_index(x,y):
    tempC = list(range(x,y+1,1))
    tempF = []
    H = list(range(40,110,10))
    hi = []
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -.22475541
    c5 = -.00683783
    c6 = -.05481717
    c7 = .00122874
    c8 = .00085282
    c9 = -.00000199
    for y in tempC:
        tempF.append(y *9/5 + 32)
    ext = 0
    for x in tempF:
        if x > 100:
            ext +=1
        for R in H:
            if x < 80:
                hi.append(000)
            else:
                hi.append(c1 +c2*x +c3*R +c4*x*R +c5*x**2 +c6*R**2 
                      +c7*R*x**2 +c8*x*R**2 +c9*(x**2)*R**2)
    for k in hi:
            if k > 100:
                ext +=1

    print("\n{0:^10}{1:^10}{2:^10}{3:^10}{4:^10}{5:^10}{6:^10}{7:^10}{8:^10}"
          .format("Celcius","Fahr","40%","50%","60%","70%","80%","90%",
                  "100%"))
    i = -7
    j = -1
    while j < len(tempC)-1:
        while i < len(hi):
            j +=1
            i +=7
            print("{0:^10}{1:^10.1f}{2:^10.2f}{3:^10.2f}{4:^10.2f}{5:^10.2f}"
              "{6:^10.2f}{7:^10.2f}{8:^10.2f}".format(tempC[j],
              tempF[j],hi[i],hi[i+1],hi[i+2],hi[i+3],hi[i+4],hi[i+5],hi[i+6]))
            if i == (len(hi)-7) or j == (len(tempC)-1):
                print("\nExtreme Heat: ",ext)
                break


