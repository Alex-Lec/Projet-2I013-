from .stratAvance import StratAvance

class StratAvanceplus(StratAvance):
    """
    Cette Stratégie permet de ralentir progressivement le robot vers la distance self.dst
    Afin de s'approcher le plus précisement possible de la distance voulu sans la dépasser
    """
    def __init__(self, robot, distance, vitesse):
        StratAvance.__init__(self,robot,distance,vitesse)
        self.ralenti = 0 # étape de la stratégie
    
    def step(self):
        angleg = (self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE)/360
        angled = (self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE)/360
        
        super().step()
        
        #Si on arrive au 4/5 de la distance à parcourir on divise la vitesse du robot par 2
        if(self.ralenti == 0 and (angleg >= self.dst*(4/5) or angled >= self.dst*(4/5))):
            self.robot.set_motor_dps(1, (self.vit/2))
            self.robot.set_motor_dps(2, (self.vit/2))
            self.vit = (self.vit/2)
            self.ralenti = 1 # changement d'étape
            
        #Si on arrive au 5/6 de la distance à parcourir on divise encore la vitesse par 2
        if(self.ralenti == 1 and (angleg >= self.dst*(5/6) or angled >= self.dst*(5/6))):
            self.robot.set_motor_dps(1, (self.vit/2))
            self.robot.set_motor_dps(2, (self.vit/2))
            self.vit = (self.vit/2)
            self.ralenti = 2 # Changement d'étape
        
