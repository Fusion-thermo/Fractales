from tkinter import *
from math import sqrt,cos,sin,tan,pi
from cmath import phase

hauteur,largeur=650,1000
iteration=-1
couleurs=['#00008b', '#0000cd', '#0000ff', '#1c86ee', '#4f94cd', '#5cacee', '#00bfff', '#87cefa', '#7ec0ee', '#00c5cd', '#00f5ff', '#8ee5ee', '#7ac5cd', '#7ac5cd', '#b0e0e6']
zcouleurs=['#8b0000', '#8b2323', '#b22222', '#cd2626', '#cd3333', '#ee0000', '#ee2c2c', '#ee3b3b', '#ff3030', '#ff4040', '#ee6363', '#ff6a6a', '#f08080', '#fa8072', '#eeb4b4', '#ffc1c1']
zaacouleurs=['#ffff00', '#eee685', '#ffec8b', '#90ee90', '#7ccd7c', '#00ee00', '#00cd00', '#32cd32', '#006400', '#698b22', '#2e8b57', '#3cb371', '#008b45']
zzcouleurs=['#8b0000', '#a52a2a', '#b22222', '#ee0000', '#ff0000', '#ee2c2c', '#ee3b3b', '#ff3030', '#e066ff', '#b452cd', '#9400d3', '#800080', '#551a8b', '#1874cd', '#436eee', '#27408b', '#000080', '#191970']
zacouleurs=['#eeff00', '#ddff00', '#ccff00', '#bbff00', '#aaff00', '#99ff00', '#88ff00', '#77ff00', '#66ff00', '#55ff00', '#44ff00', '#33ff00', '#22ff00', '#11ff00', '#00ff00']
zazzcouleurs=['#ee0011', '#dd0022', '#cc0033', '#bb0044', '#aa0055', '#990066', '#880077', '#770088', '#660099', '#5500aa', '#4400bb', '#3300cc', '#2200dd', '#1100ee', '#0000ff']

def rgb_to_hex(rgb):
	return '#'+'%02x%02x%02x' % rgb

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# #personnaliser la couleur
# r=255
# g=0
# b=0
# pas=15
# l=[]
# for i in range(pas):
# 	r-=int(255/pas)
# 	b+=int(255/pas)
# 	rgb=(r,g,b)
# 	print(rgb)
# 	l.append(rgb_to_hex(rgb))
# print(l)


def arbre():
	global cotes, iteration

	if iteration<0:
		iteration=int(Itera.get())
		Canevas.delete(ALL)
		Canevas.create_polygon((largeur/2-int(decalage.get()),hauteur),(largeur/2-int(decalage.get()),hauteur-2*int(decalage.get())),(largeur/2+int(decalage.get()),hauteur-2*int(decalage.get())),(largeur/2+int(decalage.get()),hauteur),fill=couleurs[0])
		cotes=[(largeur/2-int(decalage.get()),hauteur+0*int(decalage.get()),largeur/2+int(decalage.get()),hauteur+0*int(decalage.get()))]
	
	alpha=int(angle.get())*pi/180
	nouveaux_cotes=[]
	for cote in cotes:
		angle_au_sol=phase(cote[2]+cote[3]*1j-(cote[0]+cote[1]*1j))
		H12=sqrt((cote[3]-cote[1])**2+(cote[2]-cote[0])**2) * cos(alpha)**2
		AB12=H12 / cos(alpha)
		A=cote[0]+AB12*cos(alpha+angle_au_sol)
		B=cote[1]+AB12*sin(alpha+angle_au_sol)
		C=cote[0]-(B-cote[1])
		D=cote[1]+(A-cote[0])
		E=A-(B-cote[1])
		F=B+(A-cote[0])
		G=A-(cote[3]-B)
		H=B+(cote[2]-A)
		J=cote[2]-(cote[3]-B)
		K=cote[3]+(cote[2]-A)
		nouveaux_cotes.append((C,D,E,F))
		nouveaux_cotes.append((G,H,J,K))
		#Canevas.create_polygon((cote[0],2*hauteur-cote[1]-2*int(decalage.get())),(C,2*hauteur-D-2*int(decalage.get())),(E,2*hauteur-F-2*int(decalage.get())),(cote[2],2*hauteur-cote[3]-2*int(decalage.get())),(J,2*hauteur-K-2*int(decalage.get())),(G,2*hauteur-H-2*int(decalage.get())),fill=couleurs[int(Itera.get())-iteration+1] ,outline='')
		Canevas.create_polygon((cote[0],2*hauteur-cote[1]-2*int(decalage.get())),(C,2*hauteur-D-2*int(decalage.get())),(E,2*hauteur-F-2*int(decalage.get())),(cote[2],2*hauteur-cote[3]-2*int(decalage.get())),(J,2*hauteur-K-2*int(decalage.get())),(G,2*hauteur-H-2*int(decalage.get())),fill=couleurs[int(Itera.get())-iteration],outline='')
	cotes=nouveaux_cotes[:]

	recursif = fenetre.after(50,arbre)
	
	if iteration>0:
		iteration-=1
		numero.set(int(Itera.get())-iteration)
	else:
		fenetre.after_cancel(recursif)
		iteration=-1
		numero.set(0)

def demo_angle(angl):
	Canevas.delete(ALL)
	alpha=int(angle.get())*pi/180
	cote=(largeur/2-int(decalage.get()),hauteur+0*int(decalage.get()),largeur/2+int(decalage.get()),hauteur+0*int(decalage.get()))

	angle_au_sol=phase(cote[2]+cote[3]*1j-(cote[0]+cote[1]*1j))
	H12=(sqrt((cote[3]-cote[1])**2+(cote[2]-cote[0])**2) * tan(pi/2 - alpha))/(tan(alpha)+tan(pi/2 - alpha))
	ABH=H12 * tan(alpha)
	AB12=H12 / cos(alpha)
	A=cote[0]+AB12*cos(alpha+angle_au_sol)
	B=cote[1]+AB12*sin(alpha+angle_au_sol)
	C=cote[0]-(B-cote[1])
	D=cote[1]+(A-cote[0])
	E=A-(B-cote[1])
	F=B+(A-cote[0])
	G=A-(cote[3]-B)
	H=B+(cote[2]-A)
	J=cote[2]-(cote[3]-B)
	K=cote[3]+(cote[2]-A)
	Canevas.create_polygon((largeur/2-int(decalage.get()),hauteur),(largeur/2-int(decalage.get()),hauteur-2*int(decalage.get())),(largeur/2+int(decalage.get()),hauteur-2*int(decalage.get())),(largeur/2+int(decalage.get()),hauteur),fill=couleurs[0])
	Canevas.create_polygon((cote[0],2*hauteur-cote[1]-2*int(decalage.get())),(C,2*hauteur-D-2*int(decalage.get())),(E,2*hauteur-F-2*int(decalage.get())),(cote[2],2*hauteur-cote[3]-2*int(decalage.get())),(J,2*hauteur-K-2*int(decalage.get())),(G,2*hauteur-H-2*int(decalage.get())),fill=couleurs[1] ,outline='')
		


fenetre=Tk()
Canevas=Canvas(fenetre,height=hauteur,width=largeur)
Canevas.pack(side=LEFT)

Itera=StringVar()
Itera.set(10)
Choix_iteration=Spinbox(fenetre,from_=0,to_=16,increment=1,textvariable=Itera)
Choix_iteration.pack()

angle=StringVar()
angle.set(45)
echelle_angle=Scale(fenetre,  orient='horizontal',  from_=90,  to=0,  resolution=1,  \
tickinterval=20,  label='Angle',  variable=angle,  command=demo_angle)
echelle_angle.pack()

decalage=StringVar()
decalage.set(80)
echelle_decalage=Scale(fenetre,  orient='horizontal',  from_=0,  to=hauteur/2,  resolution=2,  \
tickinterval=100,  label='Taille carré',  variable=decalage, command=demo_angle)
echelle_decalage.pack()

Arbre = Button(fenetre,  text = 'Lancer la fractale',  command = arbre)
Arbre.pack()

numero=StringVar()
numero.set(0)
compteur=Label(fenetre,textvariable=numero)
compteur.pack()



Bouton1 = Button(fenetre,  text = 'Quitter',  command = fenetre.destroy)
Bouton1.pack(side=RIGHT)

demo_angle(45)

fenetre.mainloop()