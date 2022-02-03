import random 
from tkinter import*
from tkinter import ttk, messagebox
from time import time
class forma(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("570x300")
        self.config(bg="Lightblue")
        self.lb1=Label(self,text="Programa de Sorts", font="Times 16 underline", bg="Lightblue")
        self.lb1.place(x=10,y=10)
        self.c=Entry(self, width=15)
        self.c.place(x=110,y=50)
        self.vector=StringVar()
        self.lb4=Label(self,text="Lista generada", font="Times 12", bg="Lightblue")
        self.lb4.place(x=10,y=80)
        self.c3=Entry(self, width=70, state=DISABLED,textvariable=self.vector)
        self.c3.place(x=110,y=80)
        self.lb2=Label(self,text="Tamaño", font="Times 12", bg="Lightblue")
        self.lb2.place(x=10,y=50)
        self.vectorf=StringVar()
        self.lb3=Label(self,text="Lista resultante", font="Times 12", bg="Lightblue")
        self.lb3.place(x=10,y=107)
        self.c2=Entry(self, width=70, state=DISABLED,textvariable=self.vectorf)
        self.c2.place(x=110,y=110)
        self.b1=Button(self,text="Sort", command=self.dosort)
        self.b1.place(x=120,y=140)
        self.combi=ttk.Combobox(self, width=15)
        self.combi.place(x=180,y=140)
        self.combi["values"]=["Bubble Sort","Sort de conteo","Sort de Incerción","Quick Sort"]
        self.vec=0
        #LABEL DE RESPUESTAS
        self.bubb=StringVar()
        self.conte=StringVar()
        self.incer=StringVar()
        self.qui=StringVar()
        self.lbb=Label(self,textvariable=self.bubb, font="Times 12", bg="Lightblue")#BUBBLE
        self.lbb.place(x=5,y=180)
        self.lbc=Label(self,textvariable=self.conte, font="Times 12", bg="Lightblue")#CONTEO
        self.lbc.place(x=5,y=210)
        self.lbi=Label(self,textvariable=self.incer, font="Times 12", bg="Lightblue")#INCERSIÓN
        self.lbi.place(x=5,y=240)
        self.lbq=Label(self,textvariable=self.qui, font="Times 12", bg="Lightblue")#QUICK SORT
        self.lbq.place(x=5,y=270)
        self.mainloop()
    def dosort(self):
        try:
            if(self.combi.get()=="Bubble Sort"):
                self.bubble()
                self.vec+=1
            if(self.combi.get()=="Sort de conteo"):
                self.conteo()
                self.vec+=1
            if(self.combi.get()=="Sort de Incerción"):
                self.incersion()
                self.vec+=1
            if(self.combi.get()=="Quick Sort"):
                t=int(self.c.get())
                if(self.vec==0 or int(self.c.get())!=len(self.vector1)):
                    self.dovector()
                    p=1
                vector=[0]*t
                for i in range(t):
                    vector[i]=self.vector1[i]
                self.comp=0
                self.intercambios=0
                tiempo1= time()
                print(self.Quick(vector))
                tiempof=time()-tiempo1
                respuesta="Quick Sort        : Tiempo: %.10f s." % tiempof+" Comparaciones: "+str(self.comp)+" Intercambios: "+str(self.intercambios)
                self.qui.set(respuesta)
                self.vectorf.set(self.Quick(vector))
                self.vec+=1
            if(self.combi.get()==""):
                messagebox.showerror("ERROR","Tiene que escoger una opción de la caja")
        except:
            messagebox.showerror("Error","Dato invalido")
    def incersion(self):
        if(self.vec==0 or int(self.c.get())!=len(self.vector1)):
            self.dovector()
        t=int(self.c.get())
        p=1
        #VECTOR TEMPORAL
        vector=[0]*t
        for i in range(t):
                vector[i]=self.vector1[i]
        comp=0
        inter=0
        tiempo1= time()
        #SORT
        while(p<t):
            j=p
            comp+=1
            while( j>0 and vector[j]<vector[j-1]):
                inter+=1
                temp=vector[j]
                vector[j]=vector[j-1]
                vector[j-1]=temp
                j-=1
            p+=1
        tiempof=time()-tiempo1
        respuesta="Sort Incerción   : Tiempo: %.10f s." % tiempof+" Comparaciones: "+str(comp)+" Intercambios: "+str(inter)
        self.incer.set(respuesta)
        print(self.vector1)
        print(vector)
        self.vectorf.set(vector)
    def bubble(self):
        if(self.vec==0 or int(self.c.get())!=len(self.vector1)):
            self.dovector()
        t=int(self.c.get())-1
        vector=[0]*(t+1)
        #VECTOR TEMPORAL
        for i in range(t+1):
                vector[i]=self.vector1[i]
        comp=0
        inter=0
        tiempo1= time()
        #SORT
        while t>0:
            i=0
            while i<t:
                comp+=1
                if(vector[i]>vector[i+1]):
                    inter+=1
                    vector[i],vector[i+1]=vector[i+1],vector[i]
                i+=1
            t-=1
        tiempof=time()-tiempo1
        print(self.vector1)
        print(vector)
        respuesta="Bubble sort       : Tiempo: %.10f s." % tiempof +" Comparaciones: "+str(comp)+" Intercambios: "+str(inter)
        self.bubb.set(respuesta)
        self.vectorf.set(vector)
    def Quick(self,vector):
        self.comp+=1
        if len(vector)<=1:
            return vector
        else:
            l1=[]
            l2=[]
            e=vector[0]
            for i in range(1,len(vector)):
                if vector[i]<e:
                    l1.append(vector[i])
                else:
                    l2.append(vector[i])
                self.intercambios+=1
            return self.Quick(l1)+[e]+self.Quick(l2)
    def conteo(self):
        if(self.vec==0 or int(self.c.get())!=len(self.vector1)):
            self.dovector()
        t=int(self.c.get())
        #VECTOR TEMPORAL 
        vector=[0]*(t)
        for i in range(t):
                vector[i]=self.vector1[i]
        comp=0
        inter=0
        tiempo1= time()
        #SORT
        vector2=[0]*t
        for i in range(t):
            c=0
            comp+=1
            for j in range(t):
                if (vector[j]<vector[i] or (vector[j]==vector[i] and j<i)):
                    c+=1
                    inter+=1  
            vector2[c]=vector[i]
        tiempof=time()-tiempo1
        print(self.vector1)
        print(vector2)
        respuesta="Sort de Conteo : Tiempo: %.10f s." % tiempof+" Comparaciones: "+str(comp)+" Intercambios: "+str(inter)
        self.conte.set(respuesta)
        self.vectorf.set(vector2)
    def dovector(self):
        t=int(self.c.get())
        self.vector1=[0]*t
        for i in range(t):
            self.vector1[i]=random.randint(1,50)
        self.vector.set(self.vector1)
app=forma()
#DOCUMENTACIÓN INTERNA
#Programador:Sofia  Velásquez
#Datos del programador: Sofiamishel2003@gmail.com
#Fin: Repasar  y experimentar con stacks 
#Lenguaje: python 3.7
#Net Framewor: 4.5
#Recursos: Python, visual studio
#Descripción: Desarrollar un programa que muestre las diferencias entre los 4 sorts
#Ultima modificación 03/05/2021

