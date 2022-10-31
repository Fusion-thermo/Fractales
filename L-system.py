from turtle import *
from tkinter import *

hauteur,largeur=400,400
def affichage(mot,longueur,angle,coos_depart):
    reset()
    speed("fastest")
    ht()
    up()
    goto(coos_depart)
    down()
    width(1)
    pile=[]
    for lettre in mot:
        if lettre=="A":
            forward(longueur)
        elif lettre=="B":
            forward(longueur)
        elif lettre=="g":
            left(angle)
        elif lettre=="d":
            right(angle)
        elif lettre=="a":
            up()
            forward(longueur)
            down()
        elif lettre=="[":
            pile.append((position(),heading()))
        elif lettre=="]":
            retour=pile.pop()
            up()
            goto(retour[0])
            down()
            setheading(retour[1])

def remplace(iteration,mot,chaine1,regle1,chaine2,regle2):
    if chaine2=="":
        for j in range(iteration):
            mot=mot.replace(chaine1,regle1)
    else:
        for j in range(iteration):
            nouveau_mot=""
            # je peux faire par lettre car ici les chaines à remplacer sont à chaque fois un seul caractère
            for lettre in mot:
                if lettre==chaine1:
                    nouveau_mot+=regle1
                elif lettre==chaine2:
                    nouveau_mot+=regle2
                else:
                    nouveau_mot+=lettre
            mot=nouveau_mot

    return mot

#Aurait mérité d'utiliser une classe

def dessin():
    choix=int(value.get())
    coos_depart=(0,0)
    angle=90
    longueur=10
    chaine2=""
    regle2=""
    if choix==1:
        mot="A"
        chaine1="A"
        regle="AgAdAdAgA"
        longueur=5
        iteration=4
        coos_depart=(-200,-200)
    elif choix==2:
        mot="AdAdAdA"
        chaine1="A"
        regle="AdAgAgAAdAdAgA"
        iteration=2
        coos_depart=(-100,50)
    elif choix==3:
        mot="AdAdAdA"
        chaine1="A"
        regle="AgAAdAAdAdAgAgAAdAdAgAgAAgAAdA"
        iteration=2
        coos_depart=(-50,50)
    elif choix==4:
        mot="AdAdAdA"
        chaine1="A"
        regle="AAdAdAdAdAA"
        iteration=3
        coos_depart=(-50,50)
    elif choix==5:
        mot="AdAdAdA"
        chaine1="A"
        regle="AAdAddAdA"
        iteration=3
        coos_depart=(-100,100)
    elif choix==6:
        mot="AdAdAdA"
        chaine1="A"
        regle="AAdAdAdAdAdAgA"
        iteration=2
        coos_depart=(0,100)
    elif choix==7:
        mot="AdAdAdA"
        chaine1="A"
        regle="AAdAgAdAdAA"
        iteration=3
    elif choix==8:
        mot="AdAdAdA"
        chaine1="A"
        regle="AdAAddAdA"
        iteration=3
    elif choix==9:
        mot="AdAdAdA"
        chaine1="A"
        regle="AdAgAdAdA"
        iteration=3
    elif choix==10:
        mot="AdBdB"
        chaine1="A"
        regle="AdBgAgBdA"
        chaine2="B"
        regle2="BB"
        iteration=5
        angle=-120
        coos_depart=(-50,-50)
    elif choix==11:
        mot="AX"
        chaine1="X"
        regle="XgYAg"
        chaine2="Y"
        regle2="dAXdY"
        iteration=9
    elif choix==12:
        mot="A"
        chaine1="A"
        regle="BdAdB"
        chaine2="B"
        regle2="AgBgA"
        angle=-60
        iteration=5
    elif choix==13:
        mot="A"
        chaine1="A"
        regle="AgBggBdAddAAdBg"
        chaine2="B"
        regle2="dAgBBggBgAddAdB"
        iteration=3
        angle=60
    elif choix==14:
        mot="AdAdAdA"
        chaine1="A"
        regle="AgadAAgAgAAgAagAAdagAAdAdAAdAadAAA"
        chaine2="a"
        regle2="aaaaaa"
        iteration=2
        coos_depart=(-200,200)
        longueur=8
    elif choix==15:
        mot="A"
        chaine1="A"
        regle="A[gA]A[dA][A]"
        iteration=4
        angle=25
        coos_depart=(-100,0)
    elif choix==16:
        mot="A"
        chaine1="A"
        regle="AAd[dAgAgA]g[gAdAdA]"
        iteration=3
        angle=30
        coos_depart=(-150,50)
    elif choix==17:
        mot="X"
        chaine1="A"
        regle="AA"
        chaine2="X"
        regle2="Ad[[X]gX]gA[gAX]dX"
        angle=25
        iteration=4
    elif choix==18:
        mot="A"
        chaine1="A"
        regle="A[gA]A[dA]A"
        iteration=4
        angle=25
        coos_depart=(-100,0)
    elif choix==19:
        mot="X"
        chaine1="A"
        regle="AA"
        chaine2="X"
        regle2="A[gX][X]A[gX]dAX"
        angle=25
        iteration=4
    elif choix==20:
        mot="X"
        chaine1="A"
        regle="AA"
        chaine2="X"
        regle2="A[gX]A[dX]AX"
        angle=25
        iteration=4

    mot=remplace(iteration,mot,chaine1,regle,chaine2,regle2)
    affichage(mot,longueur,angle,coos_depart)


fenetre=Tk()
fenetre.title("L-systèmes")

demarrer = Button(fenetre,  text = 'Dessiner',  command = dessin)
demarrer.grid(row=0,column=0)

value=StringVar()
value.set(11)
Choix1=Radiobutton(fenetre, text="Flocon de Koch",variable=value, value=1)
Choix2=Radiobutton(fenetre, text="2",variable=value, value=2)
Choix3=Radiobutton(fenetre, text="3",variable=value, value=3)
Choix4=Radiobutton(fenetre, text="4",variable=value, value=4)
Choix5=Radiobutton(fenetre, text="5",variable=value, value=5)
Choix6=Radiobutton(fenetre, text="6",variable=value, value=6)
Choix7=Radiobutton(fenetre, text="7",variable=value, value=7)
Choix8=Radiobutton(fenetre, text="8",variable=value, value=8)
Choix9=Radiobutton(fenetre, text="9",variable=value, value=9)
Choix10=Radiobutton(fenetre, text="Triangle de Sierpinski",variable=value, value=10)
Choix11=Radiobutton(fenetre, text="Courbe du dragon",variable=value, value=11)
Choix12=Radiobutton(fenetre, text="Variante Sierpinski",variable=value, value=12)
Choix13=Radiobutton(fenetre, text="Courbe de Gosper",variable=value, value=13)
Choix14=Radiobutton(fenetre, text="14 avancer sans tracer",variable=value, value=14)
Choix15=Radiobutton(fenetre, text="Thym",variable=value, value=15)
Choix16=Radiobutton(fenetre, text="Petite algue",variable=value, value=16)
Choix17=Radiobutton(fenetre, text="Fenouil",variable=value, value=17)
Choix18=Radiobutton(fenetre, text="Plante",variable=value, value=18)
Choix19=Radiobutton(fenetre, text="Fenouil 2",variable=value, value=19)
Choix20=Radiobutton(fenetre, text="Herbe des prés",variable=value, value=20)
Choix1.grid(row=1,column=0)
Choix2.grid(row=2,column=0)
Choix3.grid(row=3,column=0)
Choix4.grid(row=4,column=0)
Choix5.grid(row=5,column=0)
Choix6.grid(row=6,column=0)
Choix7.grid(row=7,column=0)
Choix8.grid(row=8,column=0)
Choix9.grid(row=9,column=0)
Choix10.grid(row=1,column=1)
Choix11.grid(row=2,column=1)
Choix12.grid(row=3,column=1)
Choix13.grid(row=4,column=1)
Choix14.grid(row=5,column=1)
Choix15.grid(row=6,column=1)
Choix16.grid(row=7,column=1)
Choix17.grid(row=8,column=1)
Choix18.grid(row=9,column=1)
Choix19.grid(row=10,column=1)
Choix20.grid(row=11,column=1)

Bouton1 = Button(fenetre,  text = 'Quitter',  command = fenetre.destroy)
Bouton1.grid(row=0,column=1)

scene = Screen()
scene.setup(width=0.7, height=0.7, startx=-1, starty=0)
exitonclick()

fenetre.mainloop()