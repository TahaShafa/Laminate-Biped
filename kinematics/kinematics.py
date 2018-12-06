# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:06:36 2018

@author: danaukes
"""
import numpy
import scipy.optimize
import math
from math import pi, sin, cos
import matplotlib.pyplot as plt
plt.ion()

l1 = 26.18
l2 = 23
l3 = 20
l4 = 40
l5 = 50
l6 = 54
l7 = 40
l8 = 52.5
l9 = 52.5
l10 = 100-52.5
l11 = 100
l12 = 20
l13 = 60
l14 = 20
l15 = 20
l16 = 37.59
l17 = 20
l18 = 20

def length(v):
    length_squared = v.dot(v)
    length = length_squared**(.5)
    return length

def inner_angle(v1,v2):
    costheta = v1.dot(v2)/(length(v1)*length(v2))
    theta = math.acos(costheta)
    return theta

def total_angle(v1,v2,v3):
    v1 = v1.flatten()
    if len(v1)==2:
        v1 = numpy.r_[v1,0]
    v2 = v2.flatten()
    if len(v2)==2:
        v2 = numpy.r_[v2,0]
    costheta = numpy.dot(v1,v2)
    sintheta  = numpy.cross(v1,v2)
    l_sintheta = length(sintheta)
    neg = sintheta.dot(v3)
    if neg<0:
        neg = -1
    else:
        neg=1
    theta = math.atan2(neg*l_sintheta,costheta)
    return theta

def plotv(p1,p2):
    v=numpy.array([p1,p2])
    plt.plot(*v.T)

def generate_solver(q1,q2,q3):
    def solver(args):
        
        x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13 = args
        
        p1 = numpy.array([x1,y1])
        p2 = numpy.array([x2,y2])
        p3 = numpy.array([x3,y3])
        p4 = numpy.array([x4,y4])
        p5 = numpy.array([x5,y5])
        p6 = numpy.array([x6,y6])
        p7 = numpy.array([x7,y7])
        p8 = numpy.array([x8,y8])
        p9 = numpy.array([x9,y9])
        p10 = numpy.array([x10,y10])
        p11 = numpy.array([x11,y11])
        p12 = numpy.array([x12,y12])
        p13 = numpy.array([x13,y13])
    #    p14 = numpy.array([x14,y14])
    #    p15 = numpy.array([x15,y15])
    #    p16 = numpy.array([x16,y16])
        
        zero = [
        length(p1-p2)-l1,
        length(p2-p3)-l2,
        length(p3-p4)-l3,
        length(p4-p5)-l4,
        length(p1-p5)-l5,
        length(p5-p6)-l6,
        length(p6-p7)-l7,
        length(p7-p8)-l8,
        length(p4-p8)-l9,
        length(p8-p9)-l10,
        length(p10-p3)-l11,
        length(p9-p10)-l12,
        length(p10-p11)-l13,
        length(p11-p12)-l14,
        length(p11-p13)-l17,
        length(p12-p13)-l16,
        inner_angle(p1-p5,p5-p6)-0.01,
        inner_angle(p4-p8,p8-p9)-0.01,
        inner_angle(p9-p10,p10-p11)-0.01,
        inner_angle(p10-p11,p11-p13)-0.01,
        x1--56,
        y1-63,
        total_angle(p5-p1,numpy.array((1,0)),[0,0,1])-0,
        total_angle(p2-p1,p5-p1,[0,0,1])-q1*pi/180,
        total_angle(p4-p5,p6-p5,[0,0,1])-q2*pi/180,
        total_angle(p7-p6,p5-p6,[0,0,1])-q3*pi/180
        ]
        
        zero= numpy.array(zero)
        zero = zero.flatten()
    #    zero = (zero**2).sum()
        return length(zero)
    #    length(p-p)-l
    #    length(p-p)-l
    #    length(p-p)-l
    #    length(p-p)-l
    return solver
def generate_solver2(x):
    def solver(args):
        
        x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13 = args
        
        p1 = numpy.array([x1,y1])
        p2 = numpy.array([x2,y2])
        p3 = numpy.array([x3,y3])
        p4 = numpy.array([x4,y4])
        p5 = numpy.array([x5,y5])
        p6 = numpy.array([x6,y6])
        p7 = numpy.array([x7,y7])
        p8 = numpy.array([x8,y8])
        p9 = numpy.array([x9,y9])
        p10 = numpy.array([x10,y10])
        p11 = numpy.array([x11,y11])
        p12 = numpy.array([x12,y12])
        p13 = numpy.array([x13,y13])
    #    p14 = numpy.array([x14,y14])
    #    p15 = numpy.array([x15,y15])
    #    p16 = numpy.array([x16,y16])
        
        zero = [
        length(p1-p2)-l1,
        length(p2-p3)-l2,
        length(p3-p4)-l3,
        length(p4-p5)-l4,
        length(p1-p5)-l5,
        length(p5-p6)-l6,
        length(p6-p7)-l7,
        length(p7-p8)-l8,
        length(p4-p8)-l9,
        length(p8-p9)-l10,
        length(p10-p3)-l11,
        length(p9-p10)-l12,
        length(p10-p11)-l13,
        length(p11-p12)-l14,
        length(p11-p13)-l17,
        length(p12-p13)-l16,
        inner_angle(p1-p5,p5-p6)-0.01,
        inner_angle(p4-p8,p8-p9)-0.01,
        inner_angle(p9-p10,p10-p11)-0.01,
        inner_angle(p10-p11,p11-p13)-0.01,
        x1--56,
        y1-63,
        total_angle(p5-p1,numpy.array((1,0)),[0,0,1])-0,
        total_angle(p2-p1,p5-p1,[0,0,1])-q1*pi/180,
        total_angle(p4-p5,p6-p5,[0,0,1])-q2*pi/180,
        total_angle(p7-p6,p5-p6,[0,0,1])-q3*pi/180
        ]
        
        zero= numpy.array(zero)
        zero = zero.flatten()
    #    zero = (zero**2).sum()
        return length(zero)
    #    length(p-p)-l
    #    length(p-p)-l
    #    length(p-p)-l
    #    length(p-p)-l
    return solver

#ini = [-55.99999818,  62.99999998, -51.45431671,  37.21765651,
#       -41.79103597,  16.34612165, -25.65337612,  28.16035001,
#        -5.99999878,  62.9991917 ,  47.99731308,  63.53805181,
#        55.33589364,  24.21699824,  13.2191361 ,  -7.12672588,
#        48.70699822, -38.69984397,  32.57009072, -50.5151007 ,
#       -16.19262978, -85.47503556,   3.76410315, -86.78992294,
#       -32.32952778, -97.29029876]

ini = [-56.00000073,  62.99999982, -60.54639098,  37.21778389,
       -44.30234921,  20.93493667, -25.65321163,  28.16056938,
        -6.00000192,  62.99950351,  47.99730506,  63.53861903,
        68.34204674,  29.09894105,  21.57794614,   5.23748706,
        64.51609652, -15.07421387,  45.8675778 , -22.30144384,
       -10.29191843, -43.42278492,   8.6414348 , -49.86701318,
       -28.94040845, -50.65009462]

ini = numpy.array(ini)


#ini.append([0,0])
#ini.append([0,0])
#ini.append([0,0])
#ini.append([0,0])
#ini.append([0,0])
#ini.append([0,0])


def plotresult(args,plotpoints = True,plotlengths = True):
    x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13 = args
    
    p1 = numpy.array([x1,y1])
    p2 = numpy.array([x2,y2])
    p3 = numpy.array([x3,y3])
    p4 = numpy.array([x4,y4])
    p5 = numpy.array([x5,y5])
    p6 = numpy.array([x6,y6])
    p7 = numpy.array([x7,y7])
    p8 = numpy.array([x8,y8])
    p9 = numpy.array([x9,y9])
    p10 = numpy.array([x10,y10])
    p11 = numpy.array([x11,y11])
    p12 = numpy.array([x12,y12])
    p13 = numpy.array([x13,y13])    
    
    plotv(p1,p2)
    plotv(p2,p3)
    plotv(p3,p4)
    plotv(p4,p5)
    plotv(p1,p5)
    plotv(p5,p6)
    plotv(p6,p7)
    plotv(p7,p8)
    plotv(p4,p8)
    plotv(p8,p9)
    plotv(p10,p3)
    plotv(p9,p10)
    plotv(p10,p11)
    plotv(p11,p12)
    plotv(p11,p13)
    plotv(p12,p13) 
    
    if plotpoints:
        plt.text(*p1,'p1')
        plt.text(*p2,'p2')
        plt.text(*p3,'p3')
        plt.text(*p4,'p4')
        plt.text(*p5,'p5')
        plt.text(*p6,'p6')
        plt.text(*p7,'p7')
        plt.text(*p8,'p8')
        plt.text(*p9,'p9')
        plt.text(*p10,'p10')
        plt.text(*p11,'p11')
        plt.text(*p12,'p12')
        plt.text(*p13,'p13')
    if plotlengths:
        plt.text(*(p1/2+p2/2),'l1')
        plt.text(*(p2/2+p3/2),'l2')
        plt.text(*(p3/2+p4/2),'l3')
        plt.text(*(p4/2+p5/2),'l4')
        plt.text(*(p5/2+p1/2),'l5')
        plt.text(*(p5/2+p6/2),'l6')
        plt.text(*(p6/2+p7/2),'l7')
        plt.text(*(p7/2+p8/2),'l8')
        plt.text(*(p8/2+p4/2),'l9')
        plt.text(*(p8/2+p9/2),'l10')
        plt.text(*(p3/2+p10/2),'l11')
        plt.text(*(p9/2+p10/2),'l12')
        plt.text(*(p11/2+p10/2),'l13')
        plt.text(*(p11/2+p13/2),'l17')
        plt.text(*(p11/2+p12/2),'l14')
        plt.text(*(p12/2+p13/2),'l16')
#        plt.text(*(p1/2+p2/2),'l1')
#    plt.text(*p14,'p1')
#    plt.text(*p15,'p1')
#    plt.text(*p16,'p1')

plt.figure()
result = scipy.optimize.minimize(generate_solver(100,120,-120),ini)
plotresult(result.x)
plt.axis('equal')
plt.savefig('kinematics.png')


plt.figure()
y = []
ini1 = ini
for theta in numpy.r_[0:2*pi:20j]:
    q1 = 10 * sin(theta)+100
    q2 = 10 * sin(theta)+120
    q3 = 10 * sin(theta+pi/2)-120
    
    result = scipy.optimize.minimize(generate_solver(q1,q2,q3),ini1)
   
    
    print(result.fun)    
    plotresult(result.x,plotlengths=False, plotpoints=False)
    y.append(result.x)
    ini1 = result.x


plt.axis('equal')
plt.savefig('path.png')


y = numpy.array(y)
path = y[:,20:22]
plt.figure()
plt.plot(path[:,0],path[:,1])
plt.axis('equal')
plt.savefig('path2.png')

#
#range_min = 0
#range_max = 13
#
#path = numpy.concatenate((path,v[:,None,:],v2[:,None,:]),1)
#
#f = plt.figure()
#a = f.add_subplot(111)
#
#for item in path[range_min:range_max]:
#    a.plot(item[(0,1,2,4,5,4,3,0),0],item[(0,1,2,4,5,4,3,0),1],'ro-')
#plt.axis('equal')
#plt.savefig('f3.png')
#
#y_out = v2[range_min:range_max]
#q_in = q_in[range_min:range_max]
#
#dy = y_out[2:,:]-y_out[:-2,:]
#dq = q_in[2:]-q_in[:-2]
#
##dy = numpy.concatenate((y_out[1:,:],y_out[0:1,:]),0)-numpy.concatenate((y_out[1:,:],y_out[0:1,:]),0)
##dq = numpy.concatenate((q_in[1:],q_in[0:1]),0)-q_in
##dq %= 360
#
#
#
#J=(dy.T/dq.T)
#J.shape
#
#m = 1 #kg
#g = 9.81 #m/s^2
#fx = -m*g
#fy = m*g #N
##f = numpy.zeros((2,len(y_out)))
##f[0,:] = fx
##f[1,:] = fy
#f = numpy.array([[fx,fy]]).T
#t = J.T.dot(f)
#
#t #N-m
#
#t.max()
#
#t.min()
#
#import foldable_robotics.dxf
#lwpoly = foldable_robotics.dxf.read_lwpolylines('C:/Users/danaukes/Desktop/path.dxf')