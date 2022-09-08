from tkinter import *
from math import sqrt
from time import time

#VARIABLES DE BASE
widthfenetre=700
heigthfenetre=widthfenetre
x0=int(widthfenetre/2)
y0=int(heigthfenetre/2)
iteration_max=20
#precison : nombre entier, 1=le plus précis
precision=1
#On considère un cercle de rayon 2 inscrit dans la fenêtre. Fenêtre carrée.

#pour passer de y normale à (x;y)E [-2;2] : (y*4/heigth)-2 : les y sont inversés mais ce n'est pas
#grave car elle est symétrique par rapport à l'axe des abscisses

def rgb_to_hex(rgb):
	return '#'+'%02x%02x%02x' % rgb

#fenêtre carrée
fenetre=Tk()
Bouton1 = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
Bouton1.pack(side=TOP)
canvas=Canvas(fenetre,height=heigthfenetre,width=widthfenetre)
canvas.pack(padx=5,pady=5)


debut=time()
x=x0
for y in range(0,int((heigthfenetre+1)/2)+1,precision):
	x=int(x0-sqrt(x0**2-(y0-y)**2)) #on revient contre le cercle à gauche à chaque nouveau y
	x+=precision
	while (x-x0)**2+(y-y0)**2<x0**2:
		x+=precision
		#on écrit mandelbrot là, il sera donc calculé uniquement dans ce cercle
		a=(x*4/widthfenetre)-2
		b=(y*4/heigthfenetre)-2
		p=sqrt((a-1/4)**2+b*b)
		if a<p-2*p*p+1/4 or (a+1)**2+b*b<1/16:
			carre=canvas.create_rectangle(x,y,x+precision,y+precision,outline='blue',fill='blue')
			carre=canvas.create_rectangle(x,heigthfenetre-y,x+precision,(heigthfenetre-y)+precision,outline='blue',fill='blue')
		else:
			z=0
			c=a+b*1j
			iteration=0
			while abs(z)<2 and iteration<iteration_max:
				z=z*z+c
				iteration+=1
			
			if iteration==iteration_max:
				carre=canvas.create_rectangle(x,y,x+precision,y+precision,outline='blue',fill='blue')
				carre=canvas.create_rectangle(x,heigthfenetre-y,x+precision,(heigthfenetre-y)+precision,outline='blue',fill='blue')
			else:
				#couleur="#"+"1"*(3-len(str(iteration)))+str(iteration)+"0"*(3-len(str(iteration)))+str(iteration)+"0"*(3-len(str(iteration)))+str(iteration)
				r=255-iteration*255/iteration_max
				g=0
				b=iteration*255/iteration_max
				couleur=rgb_to_hex((int(r),int(g),int(b)))
				
				#couleur="#"+'0'*(2-len('%x' % int((iteration*255/iteration_max)))+'%x' % int((iteration*255/iteration_max))+'0'*len('%x' % int((iteration*255/iteration_max)))*2
				#couleur="#"+"0"*(2-len(hex(int(iteration*255/iteration_max))[2:]))+hex(int(iteration*255/iteration_max))[2:]+"0"*(2-len(hex(int(iteration*255/iteration_max))[2:]))+hex(int(iteration*255/iteration_max))[2:]+"0"*(2-len(hex(int(255))[2:]))+hex(int(255))[2:]
				#print(couleur)
				carre=canvas.create_rectangle(x,y,x+precision,y+precision,outline=couleur,fill=couleur)
				carre=canvas.create_rectangle(x,heigthfenetre-y,x+precision,(heigthfenetre-y)+precision,outline=couleur,fill=couleur)


print("Durée : ",time()-debut)









fenetre.mainloop()