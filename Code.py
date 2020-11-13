import pygame, sys
from pygame.locals import *
from random import randint


#VARIABLES GLOBALES

ancho=800 #dimension pantalla en x
alto=500 #dimension pantalla en y
listaEnemigos=[] #total de enemigos por nivel



class naveEspacial(pygame.sprite.Sprite):

    def __init__(self):
        #Metodo para poder usar los sprites
        pygame.sprite.Sprite.__init__(self)
        #Creamos la imagen del sprite
        self.ImageNave =pygame.transform.scale(pygame.image.load("spaceship.png"),(70,70))
        #Obtenemos el rectangulo proveniente de la img
        self.rect = self.ImageNave.get_rect()
        #Corrdenadas X y Y de cada 
        self.rect.centerx = ancho-400

        self.rect.centery = alto-100


        #Lista para almacenar disparos 
        self.listaDisparo = []
        #Vida inicial que la iniciamos siempre en True
        self.vida = True
        #Velocidad para moverse en pantalla
        self.velocidad=100
        #self.sonidoDisparo= pygame.mixer.Sound("laser2.wav")
        
    def movimiento(self):
        #Se restringe el movimiento dentro de la ventana
        if self.vida==True:
            
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>=800:
                self.rect.right=800
                
        


    
    def disparar(self,x,y):
        #Creacion del objeto proyectil con las coordenadas x y y
        miProyectil=proyectil(x, y, True,"disparoa.jpg")
        #self.sonidoDisparo.play()
        self.listaDisparo.append(miProyectil)
        
        

    
    #Se crea la img en la ventana
    def dibujar(self, superficie):
        #Pone la imagen de la nave en la ventana
        superficie.blit(self.ImageNave, self.rect)

class proyectil(pygame.sprite.Sprite):
    
    def __init__(self, posx, posy, personaje,ruta):

        pygame.sprite.Sprite.__init__(self)
        #cargamos la img de disparo
        self.disparo =pygame.transform.scale(pygame.image.load(ruta),(20,20))
        #Se obtiene el rectangulo
        self.rect = self.disparo.get_rect()
        
        #Atributos de colocacion y velocidad
        self.velocidadDisparo=10
        self.rect.top=posy
        self.rect.left=posx-10
        
        self.disparoPersonaje = personaje
        
    def trayectoria(self):
        if self.disparoPersonaje:
            self.rect.top=self.rect.top-self.velocidadDisparo
        else:
            self.rect.top=self.rect.top+self.velocidadDisparo
            
        
        
    def dibujar(self, superficie):
        superficie.blit(self.disparo, self.rect)

class Alienverdedef(pygame.sprite.Sprite):
    
    def __init__(self, posx, posy,velocidad,ruta):

        pygame.sprite.Sprite.__init__(self)

        self.alienverde =pygame.transform.scale(pygame.image.load(ruta),(50,50))
        self.rect = self.alienverde.get_rect()
        self.velocidadAlienverde=velocidad
        self.rect.y=posy#posicion del alien en y
        self.rect.x=posx#posicion del alien en x
        self.listaDisparos=[]
        self.disparo=True
        
        self.rango=10
        
        self.__ataque()
        
    def __disparo(self):
        x,y=self.rect.center
        miProyectil=proyectil(x, y, False, "disparo.jpg")
        self.listaDisparos.append(miProyectil )
        
    def __ataque(self):
        if(randint(0, 1500)<self.rango):
            self.__disparo()
        
    def dibujar(self, superficie):
        self.__ataque()
        superficie.blit(self.alienverde, self.rect)


class Alien2(pygame.sprite.Sprite):
    
    def __init__(self, posx, posy,velocidad,ruta):

        pygame.sprite.Sprite.__init__(self)

        self.alienverde =pygame.transform.scale(pygame.image.load(ruta),(50,50))
        self.rect = self.alienverde.get_rect()
        self.velocidadAlienverde=velocidad
        self.rect.y=posy#posicion del alien en y
        self.rect.x=posx#posicion del alien en x
        self.disparo=False
        
        
    def dibujar(self, superficie):
        superficie.blit(self.alienverde, self.rect)


def cargarEnemigos(enemigo):
    listaEnemigos.append(enemigo)
    
def detener():
    for enemigo in listaEnemigos:
        for disparo in enemigo.listaDisparos:
            enemigo.listaDisparos.remove(disparo)




def Juego():
    
    
    pygame.init()
    #Sonido de fondo
    pygame.mixer.init()
    pygame.mixer.music.load('song.wav')
    pygame.mixer.music.play(-1)

    #Creacion de la centana
    ventana = pygame.display.set_mode((ancho,alto))
    #Nombre de la ventana
    pygame.display.set_caption("Cow Protectors")

    #Imagen de fondo
    Fondo = pygame.image.load("fondo2.png")# cargar imagen de fondo
    Fondo= pygame.transform.scale(Fondo, (1200,600))
    
    
    #Imagen de la vaca 
    vaca= pygame.image.load("vaca.png")#Importar nave
    vaca= pygame.transform.scale(vaca, (70,40))#modificar tamano nave
    posXvaca,posYvaca=400,452
    #Activacion del mouse
    mouse=True
    #Para bloquear el juego cuando salen fondos
    enJuego= False 
    #creamos el objeto de la nave
    jugador = naveEspacial()
    disparo= proyectil(ancho,alto, True, "disparoa.jpg")

    #Datos Aliens:
    posXverde,posYverde=0,0
    posXverde2,posYverde2=posXverde+100,posYverde
    posXverde3,posYverde3=posXverde+200,posYverde
    posXverde4,posYverde4=posXverde+300,posYverde
    posXverde5,posYverde5=posXverde+400,posYverde
    posXverde6,posYverde6=0,posYverde-100
    posXverde7,posYverde7=posXverde+100,posYverde-100
    posXverde8,posYverde8=posXverde+200,posYverde-100
    posXverde9,posYverde9=posXverde+300,posYverde-100
    posXverde10,posYverde10=posXverde+400,posYverde-100
    
    derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
    derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
    
    velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1
    velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1


    #Cargar aliens que no disparan:
    alienv=Alien2(posXverde,posYverde,velocidad, "alienverde.png")
    alienv2=Alien2(posXverde2,posYverde2,velocidad2, "alienrojo.png")
    alienv3=Alien2(posXverde3,posYverde3,velocidad3, "alienamarillo.png")
    alienv4=Alien2(posXverde4,posYverde4,velocidad4, "alienrosado.png")
    alienv5=Alien2(posXverde5,posYverde5,velocidad5, "alienverde.png")

    #Cargar aliens que disparan
    alienv6=Alienverdedef(posXverde6,posYverde6,velocidad6, "alienrosado.png")
    alienv7=Alienverdedef(posXverde7,posYverde7,velocidad7, "alienamarillo.png")
    alienv8=Alienverdedef(posXverde8,posYverde8,velocidad8, "alienverde.png")
    alienv9=Alienverdedef(posXverde9,posYverde9,velocidad9, "alienrojo.png")
    alienv10=Alienverdedef(posXverde10,posYverde10,velocidad10, "alienrosado.png")

    #Ver si aliens estan vivos o muertos 
    muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
    muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False

    #Imagen de explosion Alien
    explosionAlien= pygame.image.load("explosionalien.png")#Importar explosion alien1
    explosionAlien= pygame.transform.scale(explosionAlien, (300,300))
    explosion= pygame.image.load("explosion.png")#Importar explosion 

    #Tiempo para que se vea la explosion
    tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
    tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
    
    #Copia de coordenada aliens:
    posXverdecopia,posYverdecopia=-1000,-1000
    posXverdecopia2,posYverdecopia2=-1000,-1000
    posXverdecopia3,posYverdecopia3=-1000,-1000
    posXverdecopia4,posYverdecopia4=-1000,-1000
    posXverdecopia5,posYverdecopia5=-1000,-1000
    posXverdecopia6,posYverdecopia6=-1000,-1000
    posXverdecopia7,posYverdecopia7=-1000,-1000
    posXverdecopia8,posYverdecopia8=-1000,-1000
    posXverdecopia9,posYverdecopia9=-1000,-1000
    posXverdecopia10,posYverdecopia10=-1000,-1000

    #Texto que indica que perdio
    textoFinal=pygame.font.SysFont(None, 50)
    textoFinal=textoFinal.render("Perdiste",0,(200,10,40))
    
    #Asignacion de vidas
    vidas=3
    
    #Texto que indica que indica las vidas
    textovida=pygame.font.SysFont(None, (50))
    textovidas=textovida.render("Vidas:"+str(vidas),0,(255,255,255))

    #Indica que esta en portada
    inicio=True

    #cargar portada
    portada= pygame.image.load("portada.png")# cargar imagen de fondo
    portada= pygame.transform.scale(portada, (ancho,alto))
    
    #cargar imagen de subir nivel
    levelup= pygame.image.load("levelup.png")# 
    levelup= pygame.transform.scale(levelup, (ancho,alto))

    #variable booleana para saber si se cambio de nivel
    subirnivel=False

    #contadorNivel:
    contadorNivel=1
    listaEnemigos=[1]
    #Texto que indica el nivel
    textolevel=pygame.font.SysFont(None, (50))
    textonivel=textolevel.render("Nivel:"+str(contadorNivel),0,(255,255,255))

    ganar=False
    perder=False
    #cargar imagen para ganar y perder
    gana= pygame.image.load("ganar.png")# 
    ganarimagen= pygame.transform.scale(gana, (ancho,alto))
    perde= pygame.image.load("perder.png")# 
    perderimagen= pygame.transform.scale(perde, (ancho,alto))
    
    while True:

        
        if inicio==True:
            #Aparece portada
            ventana.blit(portada,(0,0))
        if subirnivel==True:
            ventana.blit(levelup,(0,0))   
            sonidoLevelup=pygame.mixer.Sound("transicion.wav")
            i=1
            while i==1:
                sonidoLevelup.play()
                i+=1  
        if ganar==True:

            ventana.blit(ganarimagen,(0,0))   
            sonidoLevelup=pygame.mixer.Sound("victory.wav")
            i=1
            while i==1:
                sonidoLevelup.play()
                i+=1
        if perder==True:

            ventana.blit(perderimagen,(0,0))   
            sonidoLevelup=pygame.mixer.Sound("gameover.wav")
            i=1
            while i==1:
                sonidoLevelup.play()
                i+=1

        if inicio==False and subirnivel==False and ganar==False and perder==False:
            ##Lenamos el fondo
            ventana.blit(Fondo,(0,0))
            #Colocamos la vaca
            ventana.blit(vaca,(posXvaca,posYvaca))
            #Colocamos el pasto
            pygame.draw.line (ventana,(0,155,0),(0,alto),(ancho,alto),20)
            #Se llama al jugador
            disparo.trayectoria()
            jugador.movimiento()
            #Se colocan las posiciones y velocidades de los aliens:
            alienv.rect.y,alienv.rect.x,alienv.velocidadAlienverde=posYverde,posXverde,velocidad
            alienv2.rect.y,alienv2.rect.x,alienv2.velocidadAlienverde=posYverde2,posXverde2,velocidad2
            alienv3.rect.y,alienv3.rect.x,alienv3.velocidadAlienverde=posYverde3,posXverde3,velocidad3
            alienv4.rect.y,alienv4.rect.x,alienv4.velocidadAlienverde=posYverde4,posXverde4,velocidad4
            alienv5.rect.y,alienv5.rect.x,alienv5.velocidadAlienverde=posYverde5,posXverde5,velocidad5
            alienv6.rect.y,alienv6.rect.x,alienv6.velocidadAlienverde=posYverde6,posXverde6,velocidad6
            alienv7.rect.y,alienv7.rect.x,alienv7.velocidadAlienverde=posYverde7,posXverde7,velocidad7
            alienv8.rect.y,alienv8.rect.x,alienv8.velocidadAlienverde=posYverde8,posXverde8,velocidad8
            alienv9.rect.y,alienv9.rect.x,alienv9.velocidadAlienverde=posYverde9,posXverde9,velocidad9
            alienv10.rect.y,alienv10.rect.x,alienv10.velocidadAlienverde=posYverde10,posXverde10,velocidad5
            #Texto de vidas disponibles
            textovidas=textovida.render("Vidas:"+str(vidas),0,(255,255,255))
            textonivel=textolevel.render("Nivel:"+str(contadorNivel),0,(255,255,255))

        for evento in pygame.event.get():

            if evento.type == QUIT:

                pygame.quit()

                sys.exit()
            if enJuego==False:
                if inicio==True:
                    if evento.type ==pygame.KEYDOWN:
                        if evento.key==K_SPACE:
                            inicio=False
                            enJuego=True
                if inicio==False and subirnivel==True and ganar==False and perder==False:
                    if evento.type ==pygame.KEYDOWN:
                        if evento.key==K_s:
                            #Pasar ya a pantalla de juego
                            subirnivel=False
                            #Cambiar de nivel
                            contadorNivel+=1
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde-100
                            posXverde7,posYverde7=posXverde+100,posYverde-100
                            posXverde8,posYverde8=posXverde+200,posYverde-100
                            posXverde9,posYverde9=posXverde+300,posYverde-100
                            posXverde10,posYverde10=posXverde+400,posYverde-100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            
                if inicio==False and subirnivel==False and ganar==True and perder==False:
                    if evento.type ==pygame.KEYDOWN:
                        if evento.key==K_s:
                            #Pasar ya a pantalla de juego
                            ganar=False
                            #Reiniciar desde el nivel 1
                            contadorNivel=1
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde-100
                            posXverde7,posYverde7=posXverde+100,posYverde-100
                            posXverde8,posYverde8=posXverde+200,posYverde-100
                            posXverde9,posYverde9=posXverde+300,posYverde-100
                            posXverde10,posYverde10=posXverde+400,posYverde-100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]
                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            vidas=3
                        
                        if evento.key==K_n:
                            pygame.quit()

                            sys.exit()

                    
                if inicio==False and subirnivel==False and ganar==False and perder==True:
                    if evento.type ==pygame.KEYDOWN:
                        if evento.key==K_s:

                            #Pasar ya a pantalla de juego
                            perder=False
                            #Reiniciar desde el nivel 1
                            contadorNivel=1
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde-100
                            posXverde7,posYverde7=posXverde+100,posYverde-100
                            posXverde8,posYverde8=posXverde+200,posYverde-100
                            posXverde9,posYverde9=posXverde+300,posYverde-100
                            posXverde10,posYverde10=posXverde+400,posYverde-100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]
                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Restaurar vidas
                            vidas=3
                        
                        if evento.key==K_n:
                            pygame.quit()

                            sys.exit()                    
                            
                            

            elif enJuego==True:
                if evento.type ==pygame.KEYDOWN:#mover con las teclas la nave
                    if evento.key==K_LEFT:
                        jugador.rect.left-=jugador.velocidad #moverlo si se presiona tecla izquierda
                        mouse=False#si se usa una tecla izquierda ya se desactiva el mouse
                    elif evento.key==K_RIGHT:
                        jugador.rect.right+=jugador.velocidad #mover si se presiona tecla derecha
                        mouse=False#si se usa una tecla derecha ya se desactiva el mouse
                   #    Tecla que define el disparo
                    elif evento.key==K_SPACE :
                        sonidoDisparo=pygame.mixer.Sound("laser2.wav")
                        sonidoDisparo.play()
                        x,y=jugador.rect.center
                        jugador.disparar(x, y)
                        
    
                elif mouse==True:#se mueve la nave con el mouse
                    x2,y2=pygame.mouse.get_pos()
                
                    if x2<=765 and x2>=35:
                        jugador.rect.left=x2-35 # -35 para que el mouse indique el centro de la nave
                        jugador.rect.right=x2+35

        if inicio==False and subirnivel==False and ganar==False and perder==False:

                if derecha==True:#para que la imagen se vaya moviendo a la derecha
                    if posXverde<730:
                        posXverde+=alienv.velocidadAlienverde
                    else:
                        derecha=False#para que se mueva a la izquierda
                        posYverde+=100#para que en cada cambio se mueva para el frente
                if derecha==False:
                    if posXverde>1:
                        posXverde-=alienv.velocidadAlienverde
                    else:
                        derecha=True
                        posYverde+=100

                
                if contadorNivel>=2:
                    if derecha2==True:#para que la imagen se vaya moviendo a la derecha
                        if posXverde2<730:
                            posXverde2+=alienv2.velocidadAlienverde
                        else:
                            derecha2=False#para que se mueva a la izquierda
                            posYverde2+=100#para que en cada cambio se mueva para el frente
                    if derecha2==False:
                        if posXverde2>1:
                            posXverde2-=alienv2.velocidadAlienverde
                        else:
                            derecha2=True
                            posYverde2+=100

                if contadorNivel>=3:
                    if derecha3==True:#para que la imagen se vaya moviendo a la derecha
                        if posXverde3<730:
                            posXverde3+=alienv3.velocidadAlienverde
                        else:
                            derecha3=False#para que se mueva a la izquierda
                            posYverde3+=100#para que en cada cambio se mueva para el frente
                    if derecha3==False:
                        if posXverde3>1:
                            posXverde3-=alienv3.velocidadAlienverde
                        else:
                            derecha3=True
                            posYverde3+=100

                
                if contadorNivel>=4:
                    if derecha4==True:#para que la imagen se vaya moviendo a la derecha
                        if posXverde4<730:
                            posXverde4+=alienv4.velocidadAlienverde
                        else:
                            derecha4=False#para que se mueva a la izquierda
                            posYverde4+=100#para que en cada cambio se mueva para el frente
                    if derecha4==False:
                        if posXverde4>1:
                            posXverde4-=alienv4.velocidadAlienverde
                        else:
                            derecha4=True
                            posYverde4+=100
                if contadorNivel>=5:
                    if derecha5==True:#para que la imagen se vaya moviendo a la derecha
                        if posXverde5<730:
                            posXverde5+=alienv5.velocidadAlienverde
                        else:
                            derecha5=False#para que se mueva a la izquierda
                            posYverde5+=100#para que en cada cambio se mueva para el frente
                    if derecha5==False:
                        if posXverde5>1:
                            posXverde5-=alienv5.velocidadAlienverde
                        else:
                            derecha5=True
                            posYverde5+=100
                if contadorNivel>=6:
                    if derecha6==True:#para que la imagen se vaya moviendo a la derecha
                        if posXverde6<730:
                            posXverde6+=alienv6.velocidadAlienverde
                        else:
                            derecha6=False#para que se mueva a la izquierda
                            posYverde6+=100#para que en cada cambio se mueva para el frente
                    if derecha6==False:
                        if posXverde6>1:
                            posXverde6-=alienv6.velocidadAlienverde
                        else:
                            derecha6=True
                            posYverde6+=100
                if contadorNivel>=7:
                    if derecha7==True:#para que la imagen se vaya moviendo a la derecha
                        if posXverde7<730:
                            posXverde7+=alienv7.velocidadAlienverde
                        else:
                            derecha7=False#para que se mueva a la izquierda
                            posYverde7+=100#para que en cada cambio se mueva para el frente
                    if derecha7==False:
                        if posXverde7>1:
                            posXverde7-=alienv7.velocidadAlienverde
                        else:
                            derecha7=True
                            posYverde7+=100
                
                if contadorNivel>=8:
                    if derecha8==True:#para que la imagen se vaya moviendo a la derecha
                        if posXverde8<730:
                            posXverde8+=alienv8.velocidadAlienverde
                        else:
                            derecha8=False#para que se mueva a la izquierda
                            posYverde8+=100#para que en cada cambio se mueva para el frente
                    if derecha8==False:
                        if posXverde8>1:
                            posXverde8-=alienv8.velocidadAlienverde
                        else:
                            derecha8=True
                            posYverde8+=100

                if contadorNivel>=9:
                    if derecha9==True:#para que la imagen se vaya moviendo a la derecha
                        if posXverde9<730:
                            posXverde9+=alienv9.velocidadAlienverde
                        else:
                            derecha9=False#para que se mueva a la izquierda
                            posYverde9+=100#para que en cada cambio se mueva para el frente
                    if derecha9==False:
                        if posXverde9>1:
                            posXverde9-=alienv9.velocidadAlienverde
                        else:
                            derecha9=True
                            posYverde9+=100
                
                if contadorNivel>=10:
                    if derecha10==True:#para que la imagen se vaya moviendo a la derecha
                        if posXverde10<730:
                            posXverde10+=alienv10.velocidadAlienverde
                        else:
                            derecha10=False#para que se mueva a la izquierda
                            posYverde10+=100#para que en cada cambio se mueva para el frente
                    if derecha10==False:
                        if posXverde10>1:
                            posXverde10-=alienv10.velocidadAlienverde
                        else:
                            derecha10=True
                            posYverde10+=100

                #Se dibuja a la nave
                jugador.dibujar(ventana)
                
                #AQUI VAn solo los aliens que disparan
                if contadorNivel>=6:
                    if len(alienv6.listaDisparos)>0:
                        for x in alienv6.listaDisparos:
                        
                            x.dibujar(ventana)
                            x.trayectoria()
                            if x.rect.colliderect(jugador.rect):
                                if vidas<=1:
                                    alienv6.listaDisparos.remove(x)
                                    mouse=False
                                    jugador.velocidad=0
                                    velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                                    velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                                    vidas-=1
                                elif vidas>1:
                                    alienv6.listaDisparos.remove(x)
                                    #*************************Reinicio****************
                                    #Volver a poner jugar con el mouse
                                    mouse=True
                                    #Activar el modo juego
                                    enJuego= True 
                                    #Revivir a los aliens
                                    muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                                    muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                                    #Resetear las coordenadas de los aliens:
                                    posXverde,posYverde=0,0
                                    posXverde2,posYverde2=posXverde+100,posYverde
                                    posXverde3,posYverde3=posXverde+200,posYverde
                                    posXverde4,posYverde4=posXverde+300,posYverde
                                    posXverde5,posYverde5=posXverde+400,posYverde
                                    posXverde6,posYverde6=0,posYverde-100
                                    posXverde7,posYverde7=posXverde+100,posYverde-100
                                    posXverde8,posYverde8=posXverde+200,posYverde-100
                                    posXverde9,posYverde9=posXverde+300,posYverde-100
                                    posXverde10,posYverde10=posXverde+400,posYverde-100
                                    #Reiniciar movimiento a la derecha:
                                    derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                                    derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                                    #Velocidad de acuerdo al nivel, y lista de enemigos
                                    if contadorNivel==1:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                        listaEnemigos=[1]

                                    elif contadorNivel==2:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                        listaEnemigos=[1,2]

                                    elif contadorNivel==3:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                        listaEnemigos=[1,2,3]
                                    elif contadorNivel==4:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                        listaEnemigos=[1,2,3,4]
                                    if contadorNivel==5:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5]
                                    if contadorNivel==6:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6]
                                    if contadorNivel==7:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7]
                                    if contadorNivel==8:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8]
                                    if contadorNivel==9:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9]
                                    if contadorNivel==10:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                                    #Resetear el tiempo de explosion del alien:
                                    tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                                    tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                                    #Se resta una vida
                                    vidas-=1
                                
                        
                            if x.rect.top>505:
                                alienv6.listaDisparos.remove(x)
                
                if contadorNivel>=7:
                    if len(alienv7.listaDisparos)>0:
                        for x in alienv7.listaDisparos:
                        
                            x.dibujar(ventana)
                            x.trayectoria()
                            if x.rect.colliderect(jugador.rect):
                                if vidas<=1:
                                    alienv7.listaDisparos.remove(x)
                                    mouse=False
                                    jugador.velocidad=0
                                    velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                                    velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                                    vidas-=1
                                elif vidas>1:
                                    alienv7.listaDisparos.remove(x)
                                    #*************************Reinicio****************
                                    #Volver a poner jugar con el mouse
                                    mouse=True
                                    #Activar el modo juego
                                    enJuego= True 
                                    #Revivir a los aliens
                                    muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                                    muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                                    #Resetear las coordenadas de los aliens:
                                    posXverde,posYverde=0,0
                                    posXverde2,posYverde2=posXverde+100,posYverde
                                    posXverde3,posYverde3=posXverde+200,posYverde
                                    posXverde4,posYverde4=posXverde+300,posYverde
                                    posXverde5,posYverde5=posXverde+400,posYverde
                                    posXverde6,posYverde6=0,posYverde-100
                                    posXverde7,posYverde7=posXverde+100,posYverde-100
                                    posXverde8,posYverde8=posXverde+200,posYverde-100
                                    posXverde9,posYverde9=posXverde+300,posYverde-100
                                    posXverde10,posYverde10=posXverde+400,posYverde-100
                                    #Reiniciar movimiento a la derecha:
                                    derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                                    derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                                    #Velocidad de acuerdo al nivel, y lista de enemigos
                                    if contadorNivel==1:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                        listaEnemigos=[1]

                                    elif contadorNivel==2:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                        listaEnemigos=[1,2]

                                    elif contadorNivel==3:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                        listaEnemigos=[1,2,3]
                                    elif contadorNivel==4:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                        listaEnemigos=[1,2,3,4]
                                    if contadorNivel==5:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5]
                                    if contadorNivel==6:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6]
                                    if contadorNivel==7:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7]
                                    if contadorNivel==8:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8]
                                    if contadorNivel==9:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9]
                                    if contadorNivel==10:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                                    #Resetear el tiempo de explosion del alien:
                                    tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                                    tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                                    #Se resta una vida
                                    vidas-=1
                                
                        
                            if x.rect.top>505:
                                alienv7.listaDisparos.remove(x)

                if contadorNivel>=8:
                    if len(alienv8.listaDisparos)>0:
                        for x in alienv8.listaDisparos:
                        
                            x.dibujar(ventana)
                            x.trayectoria()
                            if x.rect.colliderect(jugador.rect):
                                if vidas<=1:
                                    alienv8.listaDisparos.remove(x)
                                    mouse=False
                                    jugador.velocidad=0
                                    velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                                    velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                                    vidas-=1
                                elif vidas>1:
                                    alienv8.listaDisparos.remove(x)
                                    #*************************Reinicio****************
                                    #Volver a poner jugar con el mouse
                                    mouse=True
                                    #Activar el modo juego
                                    enJuego= True 
                                    #Revivir a los aliens
                                    muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                                    muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                                    #Resetear las coordenadas de los aliens:
                                    posXverde,posYverde=0,0
                                    posXverde2,posYverde2=posXverde+100,posYverde
                                    posXverde3,posYverde3=posXverde+200,posYverde
                                    posXverde4,posYverde4=posXverde+300,posYverde
                                    posXverde5,posYverde5=posXverde+400,posYverde
                                    posXverde6,posYverde6=0,posYverde-100
                                    posXverde7,posYverde7=posXverde+100,posYverde-100
                                    posXverde8,posYverde8=posXverde+200,posYverde-100
                                    posXverde9,posYverde9=posXverde+300,posYverde-100
                                    posXverde10,posYverde10=posXverde+400,posYverde-100
                                    #Reiniciar movimiento a la derecha:
                                    derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                                    derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                                    #Velocidad de acuerdo al nivel, y lista de enemigos
                                    if contadorNivel==1:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                        listaEnemigos=[1]

                                    elif contadorNivel==2:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                        listaEnemigos=[1,2]

                                    elif contadorNivel==3:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                        listaEnemigos=[1,2,3]
                                    elif contadorNivel==4:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                        listaEnemigos=[1,2,3,4]
                                    if contadorNivel==5:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5]
                                    if contadorNivel==6:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6]
                                    if contadorNivel==7:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7]
                                    if contadorNivel==8:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8]
                                    if contadorNivel==9:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9]
                                    if contadorNivel==10:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                                    #Resetear el tiempo de explosion del alien:
                                    tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                                    tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                                    #Se resta una vida
                                    vidas-=1
                                
                        
                            if x.rect.top>505:
                                alienv8.listaDisparos.remove(x)

                if contadorNivel>=9:
                    if len(alienv9.listaDisparos)>0:
                        for x in alienv9.listaDisparos:
                        
                            x.dibujar(ventana)
                            x.trayectoria()
                            if x.rect.colliderect(jugador.rect):
                                if vidas<=1:
                                    alienv9.listaDisparos.remove(x)
                                    mouse=False
                                    jugador.velocidad=0
                                    velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                                    velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                                    vidas-=1
                                elif vidas>1:
                                    alienv9.listaDisparos.remove(x)
                                    #*************************Reinicio****************
                                    #Volver a poner jugar con el mouse
                                    mouse=True
                                    #Activar el modo juego
                                    enJuego= True 
                                    #Revivir a los aliens
                                    muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                                    muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                                    #Resetear las coordenadas de los aliens:
                                    posXverde,posYverde=0,0
                                    posXverde2,posYverde2=posXverde+100,posYverde
                                    posXverde3,posYverde3=posXverde+200,posYverde
                                    posXverde4,posYverde4=posXverde+300,posYverde
                                    posXverde5,posYverde5=posXverde+400,posYverde
                                    posXverde6,posYverde6=0,posYverde-100
                                    posXverde7,posYverde7=posXverde+100,posYverde-100
                                    posXverde8,posYverde8=posXverde+200,posYverde-100
                                    posXverde9,posYverde9=posXverde+300,posYverde-100
                                    posXverde10,posYverde10=posXverde+400,posYverde-100
                                    #Reiniciar movimiento a la derecha:
                                    derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                                    derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                                    #Velocidad de acuerdo al nivel, y lista de enemigos
                                    if contadorNivel==1:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                        listaEnemigos=[1]

                                    elif contadorNivel==2:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                        listaEnemigos=[1,2]

                                    elif contadorNivel==3:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                        listaEnemigos=[1,2,3]
                                    elif contadorNivel==4:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                        listaEnemigos=[1,2,3,4]
                                    if contadorNivel==5:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5]
                                    if contadorNivel==6:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6]
                                    if contadorNivel==7:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7]
                                    if contadorNivel==8:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8]
                                    if contadorNivel==9:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9]
                                    if contadorNivel==10:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                                    #Resetear el tiempo de explosion del alien:
                                    tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                                    tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                                    #Se resta una vida
                                    vidas-=1
                                
                        
                            if x.rect.top>505:
                                alienv9.listaDisparos.remove(x)
                
                if contadorNivel>=10:
                    if len(alienv10.listaDisparos)>0:
                        for x in alienv10.listaDisparos:
                        
                            x.dibujar(ventana)
                            x.trayectoria()
                            if x.rect.colliderect(jugador.rect):
                                if vidas<=1:
                                    alienv10.listaDisparos.remove(x)
                                    mouse=False
                                    jugador.velocidad=0
                                    velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                                    velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                                    vidas-=1
                                elif vidas>1:
                                    alienv10.listaDisparos.remove(x)
                                    #*************************Reinicio****************
                                    #Volver a poner jugar con el mouse
                                    mouse=True
                                    #Activar el modo juego
                                    enJuego= True 
                                    #Revivir a los aliens
                                    muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                                    muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                                    #Resetear las coordenadas de los aliens:
                                    posXverde,posYverde=0,0
                                    posXverde2,posYverde2=posXverde+100,posYverde
                                    posXverde3,posYverde3=posXverde+200,posYverde
                                    posXverde4,posYverde4=posXverde+300,posYverde
                                    posXverde5,posYverde5=posXverde+400,posYverde
                                    posXverde6,posYverde6=0,posYverde-100
                                    posXverde7,posYverde7=posXverde+100,posYverde-100
                                    posXverde8,posYverde8=posXverde+200,posYverde-100
                                    posXverde9,posYverde9=posXverde+300,posYverde-100
                                    posXverde10,posYverde10=posXverde+400,posYverde-100
                                    #Reiniciar movimiento a la derecha:
                                    derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                                    derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                                    #Velocidad de acuerdo al nivel, y lista de enemigos
                                    if contadorNivel==1:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                        listaEnemigos=[1]

                                    elif contadorNivel==2:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                        listaEnemigos=[1,2]

                                    elif contadorNivel==3:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                        listaEnemigos=[1,2,3]
                                    elif contadorNivel==4:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                        listaEnemigos=[1,2,3,4]
                                    if contadorNivel==5:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5]
                                    if contadorNivel==6:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6]
                                    if contadorNivel==7:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7]
                                    if contadorNivel==8:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8]
                                    if contadorNivel==9:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9]
                                    if contadorNivel==10:
                                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                        listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                                    #Resetear el tiempo de explosion del alien:
                                    tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                                    tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                                    #Se resta una vida
                                    vidas-=1
                                
                        
                            if x.rect.top>505:
                                alienv10.listaDisparos.remove(x)

                #Se dibuja el disparo en la ventana y si este se sale de la ventana solo lo remueve
        
                #Se dibuja el disparo en la ventana y si este se sale de la ventana solo lo remueve
                
             
        
                if muertealienv==False:
                    alienv.dibujar(ventana)
                if muertealienv==True and tiempoexplosionalienv<10:
                    if posXverde!=-1000 and posYverde!=-1000:
                        posXverdecopia,posYverdecopia=posXverde,posYverde
                    ventana.blit(explosionAlien,(posXverdecopia-100,posYverdecopia-100))
                    tiempoexplosionalienv+=1
                    posXverde,posYverde=-1000,-1000
                
                if contadorNivel>=2:
                    if muertealienv2==False:
                        alienv2.dibujar(ventana)
                    if muertealienv2==True and tiempoexplosionalienv2<10:
                        if posXverde2!=-1000 and posYverde2!=-1000:
                            posXverdecopia2,posYverdecopia2=posXverde2,posYverde2
                        ventana.blit(explosionAlien,(posXverdecopia2-100,posYverdecopia2-100))
                        tiempoexplosionalienv2+=1
                        posXverde2,posYverde2=-1000,-1000

                if contadorNivel>=3:
                    if muertealienv3==False:
                        alienv3.dibujar(ventana)
                    if muertealienv3==True and tiempoexplosionalienv3<10:
                        if posXverde3!=-1000 and posYverde3!=-1000:
                            posXverdecopia3,posYverdecopia3=posXverde3,posYverde3
                        ventana.blit(explosionAlien,(posXverdecopia3-100,posYverdecopia3-100))
                        tiempoexplosionalienv3+=1
                        posXverde3,posYverde3=-1000,-1000

                if contadorNivel>=4:
                    if muertealienv4==False:
                        alienv4.dibujar(ventana)
                    if muertealienv4==True and tiempoexplosionalienv4<10:
                        if posXverde4!=-1000 and posYverde4!=-1000:
                            posXverdecopia4,posYverdecopia4=posXverde4,posYverde4
                        ventana.blit(explosionAlien,(posXverdecopia4-100,posYverdecopia4-100))
                        tiempoexplosionalienv4+=1
                        posXverde4,posYverde4=-1000,-1000

                if contadorNivel>=5:
                    if muertealienv5==False:
                        alienv5.dibujar(ventana)
                    if muertealienv5==True and tiempoexplosionalienv5<10:
                        if posXverde5!=-1000 and posYverde5!=-1000:
                            posXverdecopia5,posYverdecopia5=posXverde5,posYverde5
                        ventana.blit(explosionAlien,(posXverdecopia5-100,posYverdecopia5-100))
                        tiempoexplosionalienv5+=1
                        posXverde5,posYverde5=-1000,-1000
                
                if contadorNivel>=6:
                    if muertealienv6==False:
                        alienv6.dibujar(ventana)
                    if muertealienv6==True and tiempoexplosionalienv6<10:
                        if posXverde6!=-1000 and posYverde6!=-1000:
                            posXverdecopia6,posYverdecopia6=posXverde6,posYverde6
                        ventana.blit(explosionAlien,(posXverdecopia6-100,posYverdecopia6-100))
                        tiempoexplosionalienv6+=1
                        posXverde6,posYverde6=-1000,-1000

                if contadorNivel>=7:
                    if muertealienv7==False:
                        alienv7.dibujar(ventana)
                    if muertealienv7==True and tiempoexplosionalienv7<10:
                        if posXverde7!=-1000 and posYverde7!=-1000:
                            posXverdecopia7,posYverdecopia7=posXverde7,posYverde7
                        ventana.blit(explosionAlien,(posXverdecopia7-100,posYverdecopia7-100))
                        tiempoexplosionalienv7+=1
                        posXverde7,posYverde7=-1000,-1000

                if contadorNivel>=8:
                    if muertealienv8==False:
                        alienv8.dibujar(ventana)
                    if muertealienv8==True and tiempoexplosionalienv8<10:
                        if posXverde8!=-1000 and posYverde8!=-1000:
                            posXverdecopia8,posYverdecopia8=posXverde8,posYverde8
                        ventana.blit(explosionAlien,(posXverdecopia8-100,posYverdecopia8-100))
                        tiempoexplosionalienv8+=1
                        posXverde8,posYverde8=-1000,-1000
                
                if contadorNivel>=9:
                    if muertealienv9==False:
                        alienv9.dibujar(ventana)
                    if muertealienv9==True and tiempoexplosionalienv9<10:
                        if posXverde9!=-1000 and posYverde9!=-1000:
                            posXverdecopia9,posYverdecopia9=posXverde9,posYverde9
                        ventana.blit(explosionAlien,(posXverdecopia9-100,posYverdecopia9-100))
                        tiempoexplosionalienv9+=1
                        posXverde9,posYverde9=-1000,-1000

                if contadorNivel>=10:
                    if muertealienv10==False:
                        alienv10.dibujar(ventana)
                    if muertealienv10==True and tiempoexplosionalienv10<10:
                        if posXverde10!=-1000 and posYverde10!=-1000:
                            posXverdecopia10,posYverdecopia10=posXverde10,posYverde10
                        ventana.blit(explosionAlien,(posXverdecopia9-100,posYverdecopia9-100))
                        tiempoexplosionalienv10+=1
                        posXverde10,posYverde10=-1000,-1000

                if jugador.rect.colliderect(alienv.rect):
                    if vidas<=1: 
                        mouse=False
                        jugador.velocidad=0
                        velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                        velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                        vidas-=1
                        
                    else:
                        #*************************Reinicio****************
                        #Volver a poner jugar con el mouse
                        mouse=True
                        #Activar el modo juego
                        enJuego= True 
                        #Revivir a los aliens
                        muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                        muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                        #Resetear las coordenadas de los aliens:
                        posXverde,posYverde=0,0
                        posXverde2,posYverde2=posXverde+100,posYverde
                        posXverde3,posYverde3=posXverde+200,posYverde
                        posXverde4,posYverde4=posXverde+300,posYverde
                        posXverde5,posYverde5=posXverde+400,posYverde
                        posXverde6,posYverde6=0,posYverde+100
                        posXverde7,posYverde7=posXverde+100,posYverde+100
                        posXverde8,posYverde8=posXverde+200,posYverde+100
                        posXverde9,posYverde9=posXverde+300,posYverde+100
                        posXverde10,posYverde10=posXverde+400,posYverde+100
                        #Reiniciar movimiento a la derecha:
                        derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                        derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                        #Velocidad de acuerdo al nivel, y lista de enemigos
                        if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                        elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                        elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                        elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                        if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                        if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=6,6,6,6,6# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=6,6,6,6,6
                                listaEnemigos=[1,2,3,4,5,6]
                        if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=7,7,7,7,7# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=7,7,7,7,7
                                listaEnemigos=[1,2,3,4,5,6,7]
                        if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=8,8,8,8,8# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=8,8,8,8,8
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                        if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=9,9,9,9,9# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=9,9,9,9,9
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                        if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=10,10,10,10,10# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=10,10,10,10,10
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                        #Resetear el tiempo de explosion del alien:
                        tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                        tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                        #Se resta una vida
                        vidas-=1
                        
                        
                if contadorNivel>=2:
                    if jugador.rect.colliderect(alienv2.rect):
                        if vidas<=1:
                            mouse=False
                            jugador.velocidad=0
                            velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                            velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                            vidas-=1
                        else:
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde+100
                            posXverde7,posYverde7=posXverde+100,posYverde+100
                            posXverde8,posYverde8=posXverde+200,posYverde+100
                            posXverde9,posYverde9=posXverde+300,posYverde+100
                            posXverde10,posYverde10=posXverde+400,posYverde+100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=6,6,6,6,6# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=6,6,6,6,6
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=7,7,7,7,7# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=7,7,7,7,7
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=8,8,8,8,8# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=8,8,8,8,8
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=9,9,9,9,9# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=9,9,9,9,9
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=10,10,10,10,10# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=10,10,10,10,10
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Se resta una vida
                            vidas-=1
                if contadorNivel>=3:
                    if jugador.rect.colliderect(alienv3.rect):
                        if vidas<=1:
                            mouse=False
                            jugador.velocidad=0
                            velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                            velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                            vidas-=1
                        else:
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde+100
                            posXverde7,posYverde7=posXverde+100,posYverde+100
                            posXverde8,posYverde8=posXverde+200,posYverde+100
                            posXverde9,posYverde9=posXverde+300,posYverde+100
                            posXverde10,posYverde10=posXverde+400,posYverde+100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=6,6,6,6,6# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=6,6,6,6,6
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=7,7,7,7,7# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=7,7,7,7,7
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=8,8,8,8,8# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=8,8,8,8,8
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=9,9,9,9,9# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=9,9,9,9,9
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=10,10,10,10,10# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=10,10,10,10,10
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Se resta una vida
                            vidas-=1
                
                if contadorNivel>=4:
                    if jugador.rect.colliderect(alienv4.rect):
                        if vidas<=1:
                            mouse=False
                            jugador.velocidad=0
                            velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                            velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                            vidas-=1
                        else:
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde+100
                            posXverde7,posYverde7=posXverde+100,posYverde+100
                            posXverde8,posYverde8=posXverde+200,posYverde+100
                            posXverde9,posYverde9=posXverde+300,posYverde+100
                            posXverde10,posYverde10=posXverde+400,posYverde+100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=6,6,6,6,6# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=6,6,6,6,6
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=7,7,7,7,7# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=7,7,7,7,7
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=8,8,8,8,8# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=8,8,8,8,8
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=9,9,9,9,9# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=9,9,9,9,9
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=10,10,10,10,10# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=10,10,10,10,10
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Se resta una vida
                            vidas-=1

                if contadorNivel>=5:
                    if jugador.rect.colliderect(alienv5.rect):
                        if vidas<=1:
                            mouse=False
                            jugador.velocidad=0
                            velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                            velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                            vidas-=1
                        else:
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde+100
                            posXverde7,posYverde7=posXverde+100,posYverde+100
                            posXverde8,posYverde8=posXverde+200,posYverde+100
                            posXverde9,posYverde9=posXverde+300,posYverde+100
                            posXverde10,posYverde10=posXverde+400,posYverde+100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=6,6,6,6,6# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=6,6,6,6,6
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=7,7,7,7,7# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=7,7,7,7,7
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=8,8,8,8,8# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=8,8,8,8,8
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=9,9,9,9,9# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=9,9,9,9,9
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=10,10,10,10,10# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=10,10,10,10,10
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Se resta una vida
                            vidas-=1
                
                if contadorNivel>=6:
                    if jugador.rect.colliderect(alienv6.rect):
                        if vidas<=1:
                            mouse=False
                            jugador.velocidad=0
                            velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                            velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                            vidas-=1
                        else:
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde-100
                            posXverde7,posYverde7=posXverde+100,posYverde-100
                            posXverde8,posYverde8=posXverde+200,posYverde-100
                            posXverde9,posYverde9=posXverde+300,posYverde-100
                            posXverde10,posYverde10=posXverde+400,posYverde-100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Se resta una vida
                            vidas-=1
                
                if contadorNivel>=7:
                    if jugador.rect.colliderect(alienv7.rect):
                        if vidas<=1:
                            mouse=False
                            jugador.velocidad=0
                            velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                            velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                            vidas-=1
                        else:
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde-100
                            posXverde7,posYverde7=posXverde+100,posYverde-100
                            posXverde8,posYverde8=posXverde+200,posYverde-100
                            posXverde9,posYverde9=posXverde+300,posYverde-100
                            posXverde10,posYverde10=posXverde+400,posYverde-100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Se resta una vida
                            vidas-=1

                if contadorNivel>=8:
                    if jugador.rect.colliderect(alienv8.rect):
                        if vidas<=1:
                            mouse=False
                            jugador.velocidad=0
                            velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                            velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                            vidas-=1
                        else:
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde-100
                            posXverde7,posYverde7=posXverde+100,posYverde-100
                            posXverde8,posYverde8=posXverde+200,posYverde-100
                            posXverde9,posYverde9=posXverde+300,posYverde-100
                            posXverde10,posYverde10=posXverde+400,posYverde-100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Se resta una vida
                            vidas-=1

                if contadorNivel>=9:
                    if jugador.rect.colliderect(alienv9.rect):
                        if vidas<=1:
                            mouse=False
                            jugador.velocidad=0
                            velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                            velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                            vidas-=1
                        else:
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde-100
                            posXverde7,posYverde7=posXverde+100,posYverde-100
                            posXverde8,posYverde8=posXverde+200,posYverde-100
                            posXverde9,posYverde9=posXverde+300,posYverde-100
                            posXverde10,posYverde10=posXverde+400,posYverde-100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Se resta una vida
                            vidas-=1

                if contadorNivel>=10:
                    if jugador.rect.colliderect(alienv10.rect):
                        if vidas<=1:
                            mouse=False
                            jugador.velocidad=0
                            velocidad,velocidad2,velocidad3,velocidad4,velocidad5=0,0,0,0,0# velocidad enemigos en nivel1
                            velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=0,0,0,0,0
                            vidas-=1
                        else:
                            #*************************Reinicio****************
                            #Volver a poner jugar con el mouse
                            mouse=True
                            #Activar el modo juego
                            enJuego= True 
                            #Revivir a los aliens
                            muertealienv,muertealienv2,muertealienv3,muertealienv4,muertealienv5=False,False,False,False,False
                            muertealienv6,muertealienv7,muertealienv8,muertealienv9,muertealienv10=False,False,False,False,False
                            #Resetear las coordenadas de los aliens:
                            posXverde,posYverde=0,0
                            posXverde2,posYverde2=posXverde+100,posYverde
                            posXverde3,posYverde3=posXverde+200,posYverde
                            posXverde4,posYverde4=posXverde+300,posYverde
                            posXverde5,posYverde5=posXverde+400,posYverde
                            posXverde6,posYverde6=0,posYverde-100
                            posXverde7,posYverde7=posXverde+100,posYverde-100
                            posXverde8,posYverde8=posXverde+200,posYverde-100
                            posXverde9,posYverde9=posXverde+300,posYverde-100
                            posXverde10,posYverde10=posXverde+400,posYverde-100
                            #Reiniciar movimiento a la derecha:
                            derecha,derecha2,derecha3,derecha4,derecha5=True,True,True,True,True
                            derecha6,derecha7,derecha8,derecha9,derecha10=True,True,True,True,True
                            #Velocidad de acuerdo al nivel, y lista de enemigos
                            if contadorNivel==1:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=1,1,1,1,1# velocidad enemigos en nivel1
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=1,1,1,1,1
                                listaEnemigos=[1]

                            elif contadorNivel==2:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=2,2,2,2,2# velocidad enemigos en nivel2
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=2,2,2,2,2
                                listaEnemigos=[1,2]

                            elif contadorNivel==3:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=3,3,3,3,3# velocidad enemigos en nivel3
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=3,3,3,3,3
                                listaEnemigos=[1,2,3]
                            elif contadorNivel==4:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=4,4,4,4,4# velocidad enemigos en nivel4
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=4,4,4,4,4
                                listaEnemigos=[1,2,3,4]
                            if contadorNivel==5:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel5
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5]
                            if contadorNivel==6:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel6
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6]
                            if contadorNivel==7:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel7
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7]
                            if contadorNivel==8:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel8
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8]
                            if contadorNivel==9:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9]
                            if contadorNivel==10:
                                velocidad,velocidad2,velocidad3,velocidad4,velocidad5=5,5,5,5,5# velocidad enemigos en nivel9
                                velocidad6,velocidad7,velocidad8,velocidad9,velocidad10=5,5,5,5,5
                                listaEnemigos=[1,2,3,4,5,6,7,8,9,10]

                            #Resetear el tiempo de explosion del alien:
                            tiempoexplosionalienv,tiempoexplosionalienv2,tiempoexplosionalienv3,tiempoexplosionalienv4,tiempoexplosionalienv5=0,0,0,0,0
                            tiempoexplosionalienv6,tiempoexplosionalienv7,tiempoexplosionalienv8,tiempoexplosionalienv9,tiempoexplosionalienv10=0,0,0,0,0
                            #Se resta una vida
                            vidas-=1
                            
                if len(jugador.listaDisparo)>0:
                    for x in jugador.listaDisparo:
                
                        x.dibujar(ventana)
                        x.trayectoria()
                
                        if x.rect.top<-1000:
                            
                            jugador.listaDisparo.remove(x)
                        if alienv.rect.colliderect(x.rect):
                                if x in jugador.listaDisparo:
                                    jugador.listaDisparo.remove(x)
                                muertealienv=True
                                if len(listaEnemigos)>0:
                                    listaEnemigos.pop()
                        
                        if contadorNivel>=2:
                            if alienv2.rect.colliderect(x.rect):
                                    if x in jugador.listaDisparo:
                                        jugador.listaDisparo.remove(x) 
                                    muertealienv2=True 
                                    if len(listaEnemigos)>0:
                                        listaEnemigos.pop()
                        
                        if contadorNivel>=3:
                            if alienv3.rect.colliderect(x.rect):
                                    if x in jugador.listaDisparo:
                                        jugador.listaDisparo.remove(x) 
                                    muertealienv3=True 
                                    if len(listaEnemigos)>0:
                                        listaEnemigos.pop()
                        if contadorNivel>=4:
                            if alienv4.rect.colliderect(x.rect):
                                    jugador.listaDisparo.remove(x) 
                                    muertealienv4=True 
                                    if len(listaEnemigos)>0:
                                        listaEnemigos.pop()
                        
                        if contadorNivel>=5:
                            if alienv5.rect.colliderect(x.rect):
                                    jugador.listaDisparo.remove(x) 
                                    muertealienv5=True 
                                    if len(listaEnemigos)>0:
                                        listaEnemigos.pop()
                        
                        if contadorNivel>=6:
                            if alienv6.rect.colliderect(x.rect):
                                    jugador.listaDisparo.remove(x) 
                                    muertealienv6=True 
                                    if len(listaEnemigos)>0:
                                        listaEnemigos.pop()
                        
                        if contadorNivel>=7:
                            if alienv7.rect.colliderect(x.rect):
                                    if x in jugador.listaDisparo:
                                        jugador.listaDisparo.remove(x) 
                                    muertealienv7=True 
                                    if len(listaEnemigos)>0:
                                        listaEnemigos.pop()
                        
                        if contadorNivel>=8:
                            if alienv8.rect.colliderect(x.rect):
                                    if x in jugador.listaDisparo:
                                        jugador.listaDisparo.remove(x) 
                                    muertealienv8=True 
                                    if len(listaEnemigos)>0:
                                        listaEnemigos.pop()
                        
                        if contadorNivel>=9:
                            if alienv9.rect.colliderect(x.rect):
                                    if x in jugador.listaDisparo:
                                        jugador.listaDisparo.remove(x) 
                                    muertealienv9=True 
                                    if len(listaEnemigos)>0:
                                        listaEnemigos.pop()
                        
                        if contadorNivel>=10:
                            if alienv10.rect.colliderect(x.rect):
                                    if x in jugador.listaDisparo:
                                        jugador.listaDisparo.remove(x) 
                                    muertealienv10=True 
                                    if len(listaEnemigos)>0:
                                        listaEnemigos.pop()
                #Muestra nivel
                ventana.blit(textonivel,(200,alto-50))
                if vidas>=1:
                    #Muestra vidas
                    ventana.blit(textovidas,(50,alto-50))  
        if vidas<1:
            enJuego=False
            subirnivel=False
            inicio=False
            perder=True
            
        if len(listaEnemigos)<=0:
            subirnivel=True
            inicio=False
            enJuego=False
        if contadorNivel>=11:
            enJuego=False
            subirnivel=False
            inicio=False
            ganar=True


        pygame.display.update()


Juego() 
