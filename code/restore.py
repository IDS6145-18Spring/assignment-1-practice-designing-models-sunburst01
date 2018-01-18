class Restore():
  damages = 75
  
    
  def Paint(self, damages):
    self.damages = damages - 5.5
    
  def Repair(self, damages):
    self.damages = damages - 10.5
    
  def Replace(self, damages):
      if self.damages > 100:
        return True
