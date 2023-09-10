from tupy import *


class Bolha(Image): 
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade 
        self.file = "bolha.png"
        self.pedra = None

    def update(self):
        if self._collides_with(self.pedra):
             self.destroy()
        self.y -= self.velocidade 
        if self.y < -20:
            self.y = 520
        elif self.y > 520:
            self.y = -20
        


    def destroy(self):
        inspector.destroy_object(self)
        objects.remove_object(self)
        window.update_object_pane()


        
    def _collides_with(self, other) -> bool:
        return super()._collides_with(other)



class Crianca(Image):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.file =  'crianca.png'
        self.move = False
        self.pedra = Pedra(self)

    def update(self):
        if keyboard.is_key_just_down('Up'):
            self.y -= 20
        if keyboard.is_key_just_down('Down'):
            self.y += 20
        if keyboard.is_key_just_down('Right'):
            self.x += 20
        if keyboard.is_key_just_down('Left'):
            self.x -= 20
        

    def lancar(self):
      if self.pedra is not None:
        self.pedra.update()      

class Pedra(Image):
    def __init__(self, crianca):
        self.x = crianca.x 
        self.y = crianca.y
        self.crianca = crianca
        self.file = 'pedra.png'
        self.move = False


    def update(self):
        if self.move is False and self.x != self.crianca.x:
            self.x = self.crianca.x
        if self.move is False and self.y != self.crianca.y:
            self.y = self.crianca.y
        if self.x  > 820:
            self.x = self.crianca.x
            self.move =  False
        if keyboard.is_key_just_down('space'):
            if self.move is False:
                self.move = True
            else:
                self.x += 20




if __name__ == '__main__':
    crianca =Crianca(500, 40)

    bolha1 = Bolha(710, 40, 10)
    bolha2 = Bolha(720, 30, 10)
    bolha3 = Bolha(730, 40, 15)
    
    crianca.lancar()
    bolha1.update()
    bolha2.update()
    bolha3.update()
    crianca.update()

    

    run(globals())

