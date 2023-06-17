# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:27:55 2022

@author: David Luby

# CS 410P - Program assignment 7P

# create 3 panel function for sin, cos, tan waves
"""

import numpy as np
import math

x = np.linspace(0,8*np.pi,100)

x89 = np.linspace(0,89*math.pi/180,100)
x180 = np.linspace(91*math.pi/180,np.pi,100)

s = np.sin(x)
c = np.cos(x)
t89 = np.tan(x89)
t180 = np.tan(x180)

import matplotlib.pyplot as plt

sct = plt.figure(1)
plt.subplots_adjust(wspace=.5,hspace=1.5)
sin = sct.add_subplot(311)
sin.plot(x,s)
sin.set_title("Sine, Cosine, and Tangent\nSine")
sin.set_xlabel("X in radians")
sin.set_ylabel("sin(x)")

cos = sct.add_subplot(312)
cos.plot(x,c,'r')
cos.set_title("Cosine")
cos.set_xlabel("X in radians")
cos.set_ylabel("cos(x)")

tan = sct.add_subplot(313)
t1 = tan.plot(x89,t89,'r^')
t2 = tan.plot(x180,t180,'g^')
tan.set_title("Tangent")
tan.set_xlabel("X in radians")
tan.set_ylabel("tan(x)")
tan.legend(('0-89','91-180'),loc = 'upper left',fontsize ='xx-small')
plt.show()


