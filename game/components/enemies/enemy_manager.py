
from game.components.enemies.enemy import  Enemy, Enemy_2,Enemy_3
from game.utils.constants import  SCREEN_HEIGHT


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] =[]
    
    
    def update(self):
        if not self.enemies: #cosas vacias seran falsas # []{} 0 "" y de lo contratri sera verdadero 
            self.enemies.append(Enemy())
            self.enemies.append(Enemy_2())
            self.enemies.append(Enemy_3())
            
        
        for enemy in self.enemies:
            enemy.update(self.enemies)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)