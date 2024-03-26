import os
import pygame
import time
from math import sin, radians, degrees, copysign
from pygame.math import Vector2


background = pygame.image.load('ProjectMenu.jpg')
backgroundCrash = pygame.image.load('backgroundProjectCrash.jpg')
parkingImage = pygame.image.load('backgroundProject.jpg')
parking1 = pygame.image.load('level2.jpg')
parking2 = pygame.image.load('level3.jpg')
parking3 = pygame.image.load('level4.jpg')
parking4 = pygame.image.load('level5.jpg')
parking5 = pygame.image.load('level6.jpg')
parking6 = pygame.image.load('end.jpg')




class Car:
    def __init__(self, x, y, angle=0.0, length=4, max_steering=30, max_acceleration=5.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 8
        self.brake_deceleration = 10
        self.free_deceleration = 2
        self.acceleration = 0.0
        self.steering = 0.0
        

    

    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt


class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car Parking")
        icon = pygame.image.load('grand-theft-auto.png')
        pygame.display.set_icon(icon)
        width = 1280
        height = 680
        self.screen = pygame.display.set_mode((width, height))
       # self.screen.blit(background, (0,-35))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    
    def run(self):
    
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "CarYellow.png")
        car_image = pygame.image.load(image_path)
        car = Car(4.5, 4.19)
        ppu = 32
        
        score_value = 0
            
        while not self.exit:
            
            dt = self.clock.get_time() / 600

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                if car.velocity.x < 0:
                    car.acceleration = car.brake_deceleration
                else:
                    car.acceleration += 1 * dt
            elif pressed[pygame.K_DOWN]:
                if car.velocity.x > 0:
                    car.acceleration = -car.brake_deceleration
                else:
                    car.acceleration -= 1 * dt
            elif pressed[pygame.K_SPACE]:
                if abs(car.velocity.x) > dt * car.brake_deceleration:
                    car.acceleration = -copysign(car.brake_deceleration, car.velocity.x)
                else:
                    car.acceleration = -car.velocity.x / dt
            else:
                if abs(car.velocity.x) > dt * car.free_deceleration:
                    car.acceleration = -copysign(car.free_deceleration, car.velocity.x)
                else:
                    if dt != 0:
                        car.acceleration = -car.velocity.x / dt
            car.acceleration = max(-car.max_acceleration, min(car.acceleration, car.max_acceleration))

            if pressed[pygame.K_RIGHT]:
                car.steering -= 30 * dt
            elif pressed[pygame.K_LEFT]:
                car.steering += 30 * dt
            else:
                car.steering = 0
            car.steering = max(-car.max_steering, min(car.steering, car.max_steering))
            
            #Score parking
            #parking 1
            if (score_value == 0 and car.position.x >25.55 and car.position.x < 27.1 and car.position.y > 1.65 and car.position.y < 2.15 and car.angle > -3.8 and car.angle < 3.8 and car.velocity == [0,0]):
                score_value = 1
                self.screen.blit(parking1, (0, 0))
                pygame.display.update()
                time.sleep(2)
            #parking 2
            if (score_value == 1 and car.position.x >36 and car.position.x < 37.6 and car.position.y > 6.2 and car.position.y < 6.7 and car.angle > -3.8 and car.angle < 3.8 and car.velocity == [0,0]):
                score_value = 2
                self.screen.blit(parking2, (0, 0))
                pygame.display.update()
                time.sleep(2)
            #parkign 3
            if (score_value == 2 and car.position.x >23.2 and car.position.x < 24.8 and car.position.y > 10.95 and car.position.y < 11.5 and car.angle > -3.8 and car.angle < 3.8 and car.velocity == [0,0]):
                score_value = 3
                self.screen.blit(parking3, (0, 0))
                pygame.display.update()
                time.sleep(2)
            #parking 4
            if (score_value == 3 and car.position.x >37.5 and car.position.x < 38.3 and car.position.y > 17.8 and car.position.y < 18.5 and car.angle > -93.8 and car.angle < -86.2 and car.velocity == [0,0]):
                score_value = 4
                self.screen.blit(parking4, (0, 0))
                pygame.display.update()
                time.sleep(2)
            #parking 5
            if (score_value == 4 and car.position.x >23.73 and car.position.x < 25.26 and car.position.y > 18.1 and car.position.y < 18.8 and car.angle > -183.8 and car.angle < -176.2 and car.velocity == [0,0]):
                score_value = 5
                self.screen.blit(parking5, (0, 0))
                pygame.display.update()
                time.sleep(2)
            #parking 6
            if (score_value == 5 and car.position.x >3 and car.position.x < 4.55 and car.position.y > 17.5 and car.position.y < 18.1 and car.angle > -183.8 and car.angle < -176.2 and car.velocity == [0,0]):
                score_value = 6
                self.screen.blit(parking6, (0, 0))
                pygame.display.update()
                time.sleep(3)
                game.main()
                self.exit = True
                
                
                
            
            
            #Crash respawn function
            def respawn():
                car.position = [2.5, 4.19]
                car.velocity.x = 0
                car.velocity.y = 0
                car.angle = 0
                self.screen.blit(backgroundCrash, (0, 0))
                pygame.display.update()
                time.sleep(3)
                
        
            
            #print(car.angle)
            #Crash respawn Edges + 1 
            if(car.position.x < 1 or car.position.y < 1 or car.position.x > 38.7 or car.position.y > 19.5 or (car.position.y < 3.16 and (car.position.x < 18.45 or car.position.x > 28.5))):
                respawn()
                score_value = 0
                
            #Crash respawn 2
            elif((car.position.x > 8.05 and car.position.x < 32.5) and (car.position.y > 5.44 and car.position.y < 7.95)):
                respawn()
                score_value = 0
                
            
            #Crash respawn 3.1
            elif(car.position.x < 20.05 and car.position.y > 9.85 and car.position.y < 12.45):
                respawn()
                score_value = 0
            
            #Crash respawn 3.2 green area
            elif((car.position.x > 25.9 and car.position.x < 36) and (car.position.y > 10.27 and car.position.y < 12.5)):
                respawn()
                score_value = 0
                
            #Crash respawn 4.1
            elif ((car.position.x > 6.05 and car.position.x < 20.7) and (car.position.y > 15.4)):
                respawn() 
                score_value = 0
                
            #Crash respawn 4.2
            elif ((car.position.x > 28.75 and car.position.x < 36.7 ) and (car.position.y > 16.2)):
                respawn() 
                score_value = 0
            
            # Logic
            car.update(dt)

            
            
            # Drawing
            self.screen.blit(parkingImage, (0, 0))
            rotated = pygame.transform.rotate(car_image, car.angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, car.position * ppu - (rect.width / 2, rect.height / 2))
            pygame.display.flip()
            self.clock.tick(self.ticks)
            pygame.display.update()
            


            
        pygame.quit()
    
    #Main Menu
    def main(self):
        while not self.exit:
            self.screen.blit(background, (0, -35))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    time.sleep(1)
                    game.run()
        pygame.quit()

game = Game()
game.main()