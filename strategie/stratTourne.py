class StratTourne:
    def __init__(self, robot, angle, vitesse):
        """
        Tourne d'un angle 0 à la vitesse v;
        Tourne dans le sens trigo. 
        Un angle < 0 fait tourner dans le sens anti-trigo.
        step() permet de redresser le robot si celui-ci tente 
        
        """
        self.robot = robot
        self.angle = angle # Angle que l'on veut faire effectuer au robot 
        if(self.angle<0):
            vitesse = -vitesse
        self.vit = vitesse # Vitesse de rotation des roues en degree par seconde
        
    def start(self):
        self.robot.set_motor_dps(1, self.vit)  # Met la vitesse de la roue gauche à self.vit
        self.robot.set_motor_dps(2, -self.vit) # Met la vitesse de la roue droite à self.vit
        
        # Met l'offset de la roue droite et gauche à zéro
        self.robot.offset_motor_encoder(1, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(2, self.robot.get_motor_position()[1])

    def step(self):
        pos1 = self.robot.get_motor_position()[0] 
        pos2 = self.robot.get_motor_position()[1]
    
        if (pos1 < -pos2):# La roue droite a plus avancée que la roue gauche
            # On met donc la roue gauche à la vitesse self.vit plus la différence 
            # de rotation entre les deux roues.
            self.robot.set_motor_dps(1,  self.vit +  (pos1 + pos2))
        
        elif (pos1 > -pos2):# La roue gauche a plus avancée que la roue droite
            self.robot.set_motor_dps(2, -self.vit + -(pos2 + pos1))
            
        else :
            self.robot.set_motor_dps(1, self.vit)
            self.robot.set_motor_dps(2, -self.vit)
    
    def stop(self):
        # Stop si les deux roues ont effectuées un angle supérieur à self.angle
    
        angleg = (self.robot.get_motor_position()[0]*self.robot.WHEEL_CIRCUMFERENCE) /(self.robot.WHEEL_BASE_CIRCUMFERENCE)
        angled = (self.robot.get_motor_position()[1]*self.robot.WHEEL_CIRCUMFERENCE) /(self.robot.WHEEL_BASE_CIRCUMFERENCE)
        
        if((angleg >= self.angle) and (angled <= -self.angle)):
            print(angled, angleg)
            return True
        
        return False
