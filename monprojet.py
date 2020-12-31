from pylab import *
from scipy.integrate import quad #c'est une bibliothèque pour qu'on peut calculer l'integrale
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import tkinter.font as font
from numpy import sin ,cos,exp,log,sqrt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import matplotlib.pyplot as plt
from tkinter import messagebox as msg

class Trapezoidal(object):
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        I,r =quad(f, a, b) 
    def integrate(self,f):
        x=self.x
        y=f(x)
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] # ordonnees des sommets
            plot(x_rect, y_rect,"m")
        yflist_fine = f(xlist_fine)
        plt.plot(xlist_fine, yflist_fine)#plot de f(x)
        plt.plot(xl, yl,"cs")#point support
        plt.ylabel('f(x)')
        plt.title('Trapéze',color="#00cc00", font="weight:bold")

class Milieu(object): #class rectange 
    def __init__(self, a, b, n, f):#initialiser les paramètres du classe
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x# contiens les xi
        h = float(x[1] - x[0])
        s=0
        for i in range(self.n):
            s=s+f((x[i]+x[i+1])*0.5)
        return h*s
       
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl=f(xl);
        xlist_fine=np.linspace(self.a, self.b, resolution)
        
        for i in range(self.n):
            
            m=(xl[i]+xl[i+1])/2
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , f(m), f(m)  , 0     , 0   ] # ordonnees des sommets
            plot(x_rect, y_rect,"b")
            yflist_fine = f(xlist_fine)
            plt.plot(xlist_fine, yflist_fine)
            plt.plot(m,f(m),"y*")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Milieu' , color="#00cc00", font="weight:bold")
            
          #  text(0.5*(self.a+self.b), f(self.b), '$I_{%s}$ =%12.4f' % (self.n,self.integrate(f)), fontsize=15)        
class Rectangle(object): #class rectange 
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x# contiens les xi
        y=f(x)#les yi 
        h = float(x[1] - x[0])
        s = sum(y[0:-1])
        return h * s
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i]  , 0     , 0   ] # ordonnees des sommets
            plot(x_rect, y_rect,"g")
        yflist_fine = f(xlist_fine)
        plt.plot(xlist_fine, yflist_fine)
        plt.plot(xl, yl,"rd")
  
        plt.ylabel('f(x)')
        plt.title('Rectangle',color="#00cc00", font="weight:bold")
      #  text(0.5*(self.a+self.b), f(self.b), '$I_{%s}$ =%12.4f' % (self.n,self.integrate(f)), fontsize=15)
class Simpson(object):
    def __init__(self, a, b, n, f): #initialiser les paramètres du classe
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)#les pts supports
        self.f = f
        self.n = n #nombre de subdivision

    def integrate(self,f):#calculer la somme ((b-a)/6*n)*[f(a)+2*sum(xi)+4*sum(mi)+f(b)]
        x=self.x #les points supports xi #x(0)=a-->x(n)=b
        y=f(x) #yi variable local y(o)=f(xo)-->y(n)
        h = float(x[1] - x[0])#pas h=(b-a)/2*n
        n = len(x) - 1#nombre subdivision
        if n % 2 == 1:#si le reste de la division =1 impaire
            n -= 1#☺nombre de sub ywali paire
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        return h * s / 3.0
    def Graph(self,f,resolution=1001):#1000 points 1001 résolution juste pour dessiner f
        xl = self.x #pt support
        yl = f(self.x) #yi
        xlist_fine=np.linspace(self.a, self.b, resolution)
        # pour le graph de la fonction f #intervalle ab subdiviser en 1000 poitns
        for i in range(self.n):#range intervalle 0 à n
            xx=np.linspace(self.x[i], self.x[i+1], resolution)
            #pour chaque subdivisuion  on doit dessiner polynome dnc on doit aussi le subdiviser
            m=(xl[i]+xl[i+1])/2#pt milieu
            a=xl[i]#borne gauche
            b=xl[i+1]#borne droite
            l0 = (xx-m)/(a-m)*(xx-b)/(a-b)
            l1 = (xx-a)/(m-a)*(xx-b)/(m-b)
            l2 = (xx-a)/(b-a)*(xx-m)/(b-m)
            P = f(a)*l0 + f(m)*l1 + f(b)*l2#fonction dde polynome
            plot(xx,P,'m')#dessiner polynome d'interpolation
        yflist_fine = f(xlist_fine)#fontion f
        plt.plot(xlist_fine, yflist_fine,'g')
        plt.plot(xl, yl,'wp')#point support en bleu rond
        
        plt.ylabel('f(x)')
        plt.title('Simpson',color="#00cc00", font="weight:bold")
     


class mclass:
    def __init__(self, window):
        self.window = window
        window.configure(bg="white")
        varTitle = StringVar()
        self.fr1 = Frame(window,highlightbackground="DarkOrange1", highlightthickness=2, width=100, height=200, bd= 5)
        varTitle.set("Calcule d'Intégrale")
        labelTitle = Label(window, textvariable=varTitle, fg="#FF6666", height=2,font="weight:bold",bg="white")
        labelTitle.grid(row=0, columnspan=3, sticky=S, padx=10)
        #labelTitle = font.Font(weight="bold")

        var1 = StringVar()
        var1.set("Calcule d'intégrale suivant les différents méthodes simpson, rectangle, trapézes et point milieu" ) #\n
        label1 = Label(window, textvariable=var1, height=1,fg="#0066ff",bg="white")
        label1.grid(row=1, columnspan=3, sticky=W, padx=20)


        var3 = StringVar()
        var3.set("choisissant les points de la fonction et la longeur de l'intervalle [a,b]. ")
        label3 = Label(window, textvariable=var3, height=1,fg="#0066ff",bg="white")
        label3.grid(row=2, columnspan=3, sticky=W, padx=20)

        varF = StringVar()
        varF.set("La fonction, f(x) :")
        labelF = Label(window, textvariable=varF, height=2,fg="#cc33ff", font="weight:bold",bg="white")
        labelF.grid(row=4, sticky=W, pady=10, padx=20)

        idF = StringVar()
        self.boxF = Entry(window, bd=4, width=40, textvariable=idF)
        self.boxF.grid(row=4, column=2, pady=10, padx=10)

        varA = StringVar()
        varA.set("La borne inférieur, a :")
        labelA = Label(window, textvariable=varA, height=2,fg="#cc33ff", font="weight:bold",bg="white")
        labelA.grid(row=5, sticky=W, pady=10, padx=20)

        idA = StringVar()
        self.boxA = Entry(window, bd=4, width=40, textvariable=idA)
        self.boxA.grid(row=5, column=2, pady=10, padx=10)

        varB = StringVar()
        varB.set("La borne supérieur, b :")
        labelB = Label(window, textvariable=varB, height=2,fg="#cc33ff", font="weight:bold",bg="white")
        labelB.grid(row=6, sticky=W, pady=10, padx=20)

        idB = StringVar()
        self.boxB = Entry(window, bd=4, width=40, textvariable=idB)
        self.boxB.grid(row=6, column=2, pady=10, padx=10)


        self.slider= Scale(window,from_=0, to=20, length=220, resolution=2, orient=HORIZONTAL, command= lambda val:print(val),fg="#0066ff",font="weight:bold",bg="white")
        varN = StringVar()
        varN.set("N (Nombre de points) :")
        labelN = Label(window, textvariable=varN, height=2,fg="#cc33ff", font="weight:bold",bg="white")
        labelN.grid(row=7, sticky=W, pady=10, padx=20)
        self.slider.grid(row=7, column=2, pady=15, padx=10)

        VarK = StringVar()
        VarK.set("Choisir Méthode:")
        labelK = Label(window, textvariable=VarK, height=2,fg="#cc33ff", font="weight:bold",bg="white")
        labelK.grid(row=8, sticky=W, pady=10, padx=20)
        self.meth = Combobox(window,values=["toutes les méthodes","Méthode de rectangle", "Méthode de trapéze","Méthode de point milieu","Méthode de Simpson"], state="readonly",width=40)
        self.meth.current(0)                                                                                                        
        self.meth.grid(sticky = E, row=8,column=2, pady=15, padx=10)
       
        self.button1 = Button(window, text="  Afficher  ", bg="#00cc00", fg="white",width=30 ,height=2 , command=self.plot)
        self.button1.grid(row=9, column=2, sticky=E, pady=20, padx=20)

        self.button2 = Button(window, text="  QUITTER  ",  bg="#FF6666", fg="white",width=30,height=2 , command=self.choice_box)
        self.button2.grid(row=9, column=1, sticky=E, pady=20, padx=20)


  
    def plot(self):
        try:
            N = int(self.slider.get())
            a = float(self.boxA.get())
            b = float(self.boxB.get())
            F = self.boxF.get().lower().replace(' ', '')

            f = lambda x: eval(F)

            X = np.linspace(a, b, N)
            p = np.polyfit(X, f(X), N - 1)
            t = np.linspace(a, b, 1000)
            S = Simpson(a, b, N, f)
            T = Trapezoidal(a, b,  N , f)
            M=Milieu(a,b,N,f)
            R = Rectangle(a, b, N, f)
            I,r =quad(f, a, b) #calcule d'integrale exacte
            fig = plt.figure()
            self.fig = plt.figure(figsize=(7.5, 5.5))
            # ax = fig.add_subplot(221) 
            grid()#grid on
            
            
            if self.meth.get() == "Méthode de trapéze":
                 self.a = self.fig.add_subplot(111)
                 self.a.grid(True)
           
                 self.a.plot(t, np.polyval(p, t), 'g', label="Integral Trapèze   = %12.4f" % (T.integrate(f)))
                 self.a.plot(t, f(t) - np.polyval(p, t), 'b', label="Erreur Trapèze     = %12.4f" % (I-T.integrate(f)))
                 self.a.set_title("Interpolation Equidistante", color="#5F4C0B")
                 self.a.legend()
                 T.Graph(f) 
         
            elif self.meth.get() == "Méthode de rectangle":
                 grid()

                 self.b = self.fig.add_subplot(111)
                 self.b.grid(True)
            #self.b.plot(t, f(t), 'r', label='f(x)')
            #self.b.plot(xi, yi, '.b')
                 self.b.plot(t, np.polyval(p, t),'g', label="Integral Rectangle = %12.4f" % (R.integrate(f)))
                 self.b.plot(t, f(t) - np.polyval(p, t), 'b',label="Erreur Rectangle   = %12.4f" % (I-R.integrate(f)))
            
                 self.b.legend()

                 R.Graph(f)
           # ax = fig.add_subplot(223)
            elif self.meth.get() == "Méthode de Simpson":
                 grid()
                 self.c = self.fig.add_subplot(111)
                 self.c.grid(True)
           # self.c.plot(t, f(t), 'r', label='f(x)')
            #self.b.plot(xi, yi, '.b')
                 self.c.plot(t, np.polyval(p, t),'g', label="Integral Simpson   = %12.4f" % (S.integrate(f)))
                 self.c.plot(t, f(t) - np.polyval(p, t), 'b',label="Erreur Simpson     = %12.4f" % (I-S.integrate(f)))
           
                 self.c.legend()
                 S.Graph(f)
            
            elif self.meth.get() == "Méthode de point milieu":

                 self.d = self.fig.add_subplot(111)
                 self.d.grid(True)
           
                 self.d.plot(t, np.polyval(p, t),'g', label="Integral Milieu    = %12.4f" % (M.integrate(f)))
                 self.d.plot(t, f(t) - np.polyval(p, t), 'b',label="Erreur Milieu      = %12.4f" % (I-M.integrate(f)))
            
                 self.d.legend()
                 M.Graph(f)
                 grid()
                 fig.tight_layout()
       
            
            elif self.meth.get() == "toutes les méthodes":
                grid()#grid on
                self.a = self.fig.add_subplot(221)
                self.a.grid(True)
                self.a.plot(t, np.polyval(p, t), 'g', label="Integral Trapèze   = %12.4f" % (T.integrate(f)))
                self.a.plot(t, f(t) - np.polyval(p, t), 'b', label="Erreur Trapèze     = %12.4f" % (I-T.integrate(f)))
                self.a.set_title("Interpolation Equidistante", color="#5F4C0B")
                self.a.legend()
                T.Graph(f) 
                grid()
                self.b = self.fig.add_subplot(222)
                self.b.grid(True)
           
                self.b.plot(t, np.polyval(p, t),'g', label="Integral Rectangle = %12.4f" % (R.integrate(f)))
                self.b.plot(t, f(t) - np.polyval(p, t), 'b',label="Erreur Rectangle   = %12.4f" % (I-R.integrate(f)))
                self.b.legend()
                R.Graph(f)
                grid()
                self.c = self.fig.add_subplot(223)
                self.c.grid(True)
                self.c.plot(t, np.polyval(p, t),'g', label="Integral Simpson   = %12.4f" % (S.integrate(f)))
                self.c.plot(t, f(t) - np.polyval(p, t), 'b',label="Erreur Simpson     = %12.4f" % (I-S.integrate(f)))
           
                self.c.legend()
                S.Graph(f)
                self.d = self.fig.add_subplot(224)
                self.d.grid(True)
                self.d.plot(t, np.polyval(p, t),'g', label="Integral Milieu    = %12.4f" % (M.integrate(f)))
                self.d.plot(t, f(t) - np.polyval(p, t), 'b',label="Erreur Milieu      = %12.4f" % (I-M.integrate(f)))
                self.d.legend()
                M.Graph(f)
                grid()
                fig.tight_layout()

            self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
            self.canvas.get_tk_widget().grid(row=3, column=3, rowspan=6, pady=10, padx=10)

           

        except ValueError:
            messagebox.showwarning("ValueError", "Veuillez vérifier votre saisie")

    def choice_box(self):
        answer = msg.askyesnocancel("Attention", "Vous êtes sur de quitter")
 
        if answer == True:
            self.window.quit()
if __name__ == '__main__':
  

 
    window = Tk()
    window.title('Calcule d intégrale')
    window.resizable(width=True, height=True)
    window.geometry('+0+0')
    start = mclass(window)
    window.mainloop()