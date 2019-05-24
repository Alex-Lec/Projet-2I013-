class StratAvance:
    def __init__(self, robot, distance, vitesse):
        self.robot = robot
        self.dst = distance # Distance d'arret en cm
        self.vit = vitesse  # Vitesse de rotation des roues en degree par seconde
    
    def start(self):
        self.robot.set_motor_dps(1, self.vit) # Met la vitesse de la roue gauche à self.vit
        self.robot.set_motor_dps(2, self.vit) # Met la vitesse de la roue droite à self.vit
        
        # Met l'offset de la roue droite et gauche à zéro
        self.robot.offset_motor_encoder(1, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(2, self.robot.get_motor_position()[1])
    
    def step(self):
    
        pos1 = self.robot.get_motor_position()[0] 
        pos2 = self.robot.get_motor_position()[1]
        
        if (pos1 < pos2):# La roue droite a plus avancée que la roue gauche
            # On met donc la roue gauche à la vitesse self.vit plus la différence 
            # de rotation entre les deux roues.
            self.robot.set_motor_dps(1, self.vit + (pos2 - pos1))
        
        elif (pos1 > pos2):# La roue gauche a plus avancé que la roue droite
            self.robot.set_motor_dps(2, self.vit + (pos1 - pos2))
            
        else :
            self.robot.set_motor_dps(1, self.vit)
            self.robot.set_motor_dps(2, self.vit)
    
    def stop(self):
        # Stop si une des roues a effectuée une distance supérieur à self.dst
        angleg = (self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE)/360
        angled = (self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE)/360
            
        if(angleg > self.dst):
            return True
            
        if(angled > self.dst):
            return True
        
        return False
