from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, SHOT_COOLDOWN
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.player_shot_timer = 0  
# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle())
        self.triangle()
        self.linewidth = 2

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
         
        if self.player_shot_timer > 0:
            self.player_shot_timer -= dt
            if self.player_shot_timer <0:
                self.player_shot_timer = 0
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.player_shot_timer == 0:
                self.shoot()
                self.player_shot_timer = SHOT_COOLDOWN   #sets cooldown timing for bullets
                

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x,y):
        super().__init__(x, y, SHOT_RADIUS)
    

    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), self.position, self.radius,width = 2)

    def update(self, dt):
        self.position += self.velocity * dt