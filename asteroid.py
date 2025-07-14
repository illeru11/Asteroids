import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), self.position, self.radius,width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            spawn_angle = random.uniform(20,50)
            #new1_angle = self.velocity.rotate(spawn_angle)
            #new2_angle = self.velocity.rotate(-spawn_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            new1 = self.spawn(self.radius,self.position,self.velocity.rotate(spawn_angle))
            new2 = self.spawn(self.radius,self.position,self.velocity.rotate(-spawn_angle))

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity