from strategie import StratAvance,StratStop
from threading import Thread
import sys, termios, tty, os, time
 


class Controleur_droit_stop():
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
     
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
     
    button_delay = 0.2
    
    def __init__(self,rob, vit = 1000):
        self.robot = rob
        self.Go = None
        self.cnt = "o"
        self.dst = dst
        self.vitesse = vit
    
    def start(self):
        self.Go = Stop(self.robot());
        self.Go.start()
        self.cnt = "o"
        
    def step(self):
        self.Go.step()
        self.cnt = getch()
        
        if (self.cnt == "z"):
            time.sleep(0.2)
        
        if (self.cnt == "s"):
            time.sleep(0.2)

        if (self.cnt == "q"):
            time.sleep(0.2)
        
        if (self.cnt == "d"):
            time.sleep(0.2)
            
    def stop(self):
        if (cnt == "p"):
            self.Go = StratStop(self.robot)
            self.Go.start()
            return False
        return True
