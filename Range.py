
# coding: utf-8

# In[3]:


import numpy as np
from math import sqrt, cos, sin, asin, acos, tan, atan, degrees, fabs, pow,radians


# In[4]:


# Ввод времени каждого из сигналов в микросекундах
try:
    p0=float(input('Введие время основного сигнала на р0 (мкс): '))
    p0_otr=float(input('Введие время сигнала от поверхности на р0 (мкс): '))
    p1=float(input('Введие время основного сигнала на р1 (мкс): '))
    p1_otr=float(input('Введие время сигнала от поверхности на р1 (мкс): '))
    p2=float(input('Введие время основного сигнала на р2 (мкс): '))
    p2_otr=float(input('Введие время сигнала от поверхности на р2 (мкс): '))
    
    p3=float(input('Введие время основного сигнала на р3 (мкс): '))
    p3_otr=float(input('Введие время сигнала от поверхности на р3 (мкс): '))
except ValueError:
    print('Какие-то данные не введены, могут возникнуть проблемы в дальнейших расчётах')
    
'''
3879
6926
3297
6785
3879
6811
3914
6335
'''


# In[5]:


# Перевод времени сигналов в секунды
p0*=0.000001
p0_otr*=0.000001
p1*=0.000001
p1_otr*=0.000001
p2*=0.000001
p2_otr*=0.000001
p3*=0.000001
p3_otr*=0.000001
print(p0)
print(p1)
print(p2)
print(p3)


# In[6]:


# Константы

c = 1450   # Скорость звука для воды в 20 градусов
H = 3.0    # Глубина акватории
h = 0.82   # Высота пирамидки
h_d = 1.02 # Высота пирамидки до дна

p0_p1 = p0_p2 = p1_p2 = 0.96


# In[7]:


# Расстояния по задержкам
r0_r0_otr = (p0_otr-p0)*c
r1_r1_otr = (p1_otr-p1)*c
r2_r2_otr = (p2_otr-p2)*c

r0_1 = (p0-p1)*c
r1_0 = (p1-p0)*c
r0_2 = (p0-p2)*c
r2_0 = (p2-p0)*c
r0_3 = (p0-p3)*c
r3_0 = (p3-p0)*c
r1_2 = (p1-p2)*c
r2_1 = (p2-p1)*c
r1_3 = (p1-p3)*c
r3_1 = (p3-p1)*c
r2_3 = (p2-p3)*c
r3_2 = (p3-p2)*c


# In[8]:


# Определяем направление

def wherever ():
    p0_p1 = 0.96

    if p0<=p1 and p0<=p2:
        
        alpha = degrees(asin(r2_0/p0_p1))
        beta = degrees(asin(r1_0/p0_p1))
        
        
        if alpha>=beta:
            print ('фронт проходит через гидрофон p0, пеленг в {} градусов отностильено ребра p0_p2'.format(beta))

        if alpha<beta:
            print ('фронт проходит через гидрофон p0, пеленг в {} градусов отностильено ребра p0_p1'.format(alpha) )
            
        rast = (4*H**2 - r0_r0_otr**2)/(2*r0_r0_otr)
        
        return alpha, beta, rast

    elif p1<p0 and p1<p2:
        
        alpha = degrees(asin(r0_1/p0_p1))
        beta = degrees(asin(r2_1/p0_p1))
        

        if alpha>=beta:
            print ('фронт проходит через гидрофон p1, пеленг в {} градусов отностильено ребра p1_p0'.format(beta))

        if alpha<beta:
            print ('фронт проходит через гидрофон p1, пеленг в {} градусов отностильено ребра p1_p2'.format(alpha) )
            
        rast = (4*H**2 - r1_r1_otr**2)/(2*r1_r1_otr)
        
        return alpha, beta, rast
    
    elif p2<p0 and p2<p1:
        
        alpha=degrees(asin(r1_2/p0_p1))
        beta=degrees(asin(r0_2/p0_p1))
        

        if alpha>=beta:
            print ('фронт проходит через гидрофон p2, пеленг в {} градусов отностильено ребра p2_p0'.format(beta))

        if alpha<beta:
            print ('фронт проходит через гидрофон p2, пеленг в {} градусов отностильено ребра p2_p1'.format(alpha) )
        
        rast = (4*H**2 - r2_r2_otr**2)/(2*r2_r2_otr)
        
        return alpha, beta, rast
        
    else:
        print('Incorrect')
        
    #return alpha, beta


# In[9]:


alpha, beta, rast = wherever()

print ('Уголь альфа = {}, угол бета = {}'.format(alpha,beta))


# In[10]:


# Определяем вертикальный фронт
o_r = sqrt(pow(r3_1,2)-pow(h,2)) # Расстояние до плоского фронта от центра пирамиды у дна
def vert_peleng():
    
    if p0<=p1 and p0<=p2:
        r0_3 = (p0_otr-p3_otr)*c # задержка в получении сигнала от поверхности между верхним гидрофоном и нижним
        p3_o2 = h - r0_3 # расстояние от верхнего гидрофона до начала временной задержки
        vert_front = degrees(atan(p3_o2/o_r))
        print('Угол фронта, относительно дна, равен {} градусам'.format(vert_front))
        return vert_front
        
    elif p1<p0 and p1<p2:
        r1_3 = (p1_otr-p3_otr)*c # задержка в получении сигнала от поверхности между верхним гидрофоном и нижним
        p3_o2 = h - r1_3 # расстояние от верхнего гидрофона до начала временной задержки
        vert_front = degrees(atan(p3_o2/o_r))
        print('Угол фронта, относительно дна, равен {} градусам'.format(vert_front))
        return vert_front
        
    elif p2<p0 and p2<p1:
        r2_3 = (p2_otr-p3_otr)*c # задержка в получении сигнала от поверхности между верхним гидрофоном и нижним
        p3_o2 = h - r2_3 # расстояние от верхнего гидрофона до начала временной задержки
        vert_front = degrees(atan(p3_o2/o_r))
        print('Угол фронта, относительно дна, равен {} градусам'.format(vert_front))
        return vert_front  


# In[11]:


front=vert_peleng()
peleng=90-front

tangen=tan(radians(peleng))
print(peleng,tangen)


# In[12]:


def rastoyanie():
    
    # Расстояние до источника по отражению от поверхности
    
    rast_pov = (2*H)/(tangen)-o_r-h_d/(tangen)
    
    print('Расстояние до источника по сигналу, пришешему с поверхности, {} м'.format(rast_pov))
    return rast_pov
    


# In[13]:


rast_pov=rastoyanie()

# Расстояние до источника по дну

print('Расстояние до источника на прямую равно {} м'.format(rast))

