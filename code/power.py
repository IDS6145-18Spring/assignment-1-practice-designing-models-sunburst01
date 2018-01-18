class Power():
    batterylevel = 100

    def Recharge(self,  batterylevel):
      self.batterylevel = batterylevel+1
      
    def Discharge(self, batterylevel):
      self.batterylevel = batterylevel -1
      
    def Neutral(self, batterylevel):
      self.batterylevel = batterylevel +0