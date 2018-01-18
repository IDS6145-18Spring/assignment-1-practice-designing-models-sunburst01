class Power():
    batterylevel = 100

    def Recharge(self,  batterylevel):
      self.batterylevel = batterylevel+1
      
    def Discharge(self, batterylevel):
      self.batterylevel = batterylevel -1
      
    def Neutral(self, batterylevel):
      self.batterylevel = batterylevel +0
      
class Surveillance():
  crime = True
  
  if True:
    def Alert(self, crime):
      return "Alert";
    
    def Speak(self, crime):
      return "Speak";
      
    def Stun(self, crime):
      return "Stun";
      
class Pollution():
  airQualityLevels = 50
  
  def PurifyAir(self, airQualityLevels):
    self.airQualityLevels = airQualityLevels - 10;
    
  def Tree(self,airQualityLevels):
   self.airQualityLevels = airQualityLevels - 10;
   
class Restore():
  damages = 75
  
    
  def Paint(self, damages):
    self.damages = damages - 5.5
    
  def Repair(self, damages):
    self.damages = damages - 10.5
    
  def Replace(self, damages):
      if self.damages > 100:
        return True

def main():
 
