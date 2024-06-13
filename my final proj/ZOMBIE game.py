import pygame, simpleGE





class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.position = (50, 400)
        self.inAir = True
            
    def process(self):
        if self.inAir:
            self.addForce(.24, 270)
            self.correction = (0, 0)
            
        if self.y > 450:
            self.inAir = False
            self.y = 450
            self.dy = 0          
        
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += 5
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= 5   
        if self.scene.isKeyPressed(pygame.K_UP):
            
            if not self.inAir:
                self.addForce(7, 90)
                self.inAir = True
        self.inAir = True

        for platform in self.scene.platforms:
            if self.collidesWith(platform):                
                self.x += self.correction[0]
                self.y += self.correction[1]
                        
                        
                        
        for WALLR in self.scene.rightWall:
            if self.collidesWith(WALLR):                
                if self.dy > 0:
                        self.right = WALLR.left
                        self.dy = 0
                        self.inAir = False
        
        for WALLLE in self.scene.leftwall:
            if self.collidesWith(WALLLE):                
                if self.dy > 0:
                        self.left = WALLLE.right
                        self.dy = 0
                        self.inAir = False

class Platform(simpleGE.Sprite):
    def __init__(self, scene, position):
        super().__init__(scene)
        self.position = (position)
        self.colorRect("darkblue", (50, 50))
       
    def update(self):
        super().update()
        if self.mouseDown:
            self.position = pygame.mouse.get_pos()

class WALLR(simpleGE.Sprite):
    
    def __init__(self, scene, position):
        super().__init__(scene)
        self.position = (position)
        self.colorRect("pink", (10, 50))
       
    def update(self):
        super().update()
        if self.mouseDown:
            self.position = pygame.mouse.get_pos()


class WALLLE(simpleGE.Sprite):
    
    def __init__(self, scene, position):
        super().__init__(scene)
        self.position = (position)
        self.colorRect("forestgreen", (10, 50))
       
    def update(self):
        super().update()
        if self.mouseDown:
            self.position = pygame.mouse.get_pos()



#class objecttive:
                
                
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
       
        self.setCaption("arrows to move and jump. drag platforms around")
        
        self.charlie = Charlie(self)
        
        self.platforms = self.platforms = [Platform(self, (350, 350)), 
                                           Platform(self, (150, 450))]
     
        self.rightWall = self.rightWall = [WALLR(self, (317,350))]
        self.leftwall = self.leftWall = [WALLLE(self, (200,50))]
        
        self.sprites = [ self.platforms , self.rightWall, self.leftWall ,self.charlie ]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    