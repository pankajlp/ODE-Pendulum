
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:40:25 2020

@author: PANKAJ
"""

#Importing the required modules
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
from PIL import Image
import matplotlib.image as image
import glob


#Defining the function to return the value of dtheta_dt

def model(theta,t,b,g,l,m):
    theta1= theta[0]
    theta2=theta[1]
    dtheta1_dt=theta2
    dtheta2_dt=(-b/m)*theta2-(g/l)*math.sin(theta1)
    dtheta_dt=[dtheta1_dt,dtheta2_dt]
    return dtheta_dt

#Input values for the pendulum 
    
b=0.05
g=9.81
l=1.0
m=1.0


#Initial Condition
theta_0=[0,3]

#Time Intervals

t= np.linspace(0,20,200)

#Solving the differential equation
theta=odeint(model,theta_0,t,args=(b,g,l,m))

#Plotting  the results
#Plotting the angular displacement
plt.plot(t,theta[:,0],'b-',label=r'$\frac{d\theta1}{dt}=\theta2$')
#Plotting the angular velocity
plt.plot(t,theta[:,1],'r-',label=r'$\frac{d\theta2}{dt}=-\frac{b}{m}\theta2-\frac{g}{l}sin\theta1$')
plt.legend(loc='best')
plt.ylabel('Plot')
plt.xlabel('Time')
plt.show()


#Creating the Animation
c=1  #Creating the counter loop variables
frames = [] #Thee images created would be appended
imgs = glob.glob("*.png") #Using gllob method to extract .png files

for x in theta[:,0]:
    x0=0
    y0=0
    x1=l*math.sin(x)
    y1=-l*math.cos(x)
    #getting an image of wall as the base of the pendulum
    im = Image.open("Pendulum wall.png")
   
 
      
    filename=str(c)+'.png'
    c=c+1
    plt.figure()
    #plotting the image file and setting the axes and location
    fig, ax = plt.subplots() 
    
    ax.imshow(im,aspect='auto',extent=(-1.0,1.0,0.0,0.5),alpha=0.5)
    
    
    #PLotting the String of the Pendulum
    plt.plot([x0,x1],[y0,y1],'r')
    #PLotting the Ball of the Pendulum
    plt.plot(x1,y1,'o',markersize=20)
    
    plt.xlim([-1.5,1.5])
    plt.ylim([-1.5,1.5])
    plt.title('Animation of Pendulum using Python')
    #Saving the figures with their file names
    plt.savefig(filename)
    plt.close()
    for i in filename:
    			new_frame = Image.open(filename)
    			frames.append(new_frame)
 

		# Create the frames from the extracted files from glob

# Saving into a GIF file that loops forever
frames[0].save('Pendulum Animation.gif', format='GIF',append_images=frames[1:],save_all=True, duration=50, loop=0)
print('Done')
