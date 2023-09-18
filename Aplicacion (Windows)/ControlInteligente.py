from simple_pid import PID

##63, 0.06, 0.05 este es el que funciono mejor con la primera evaluacion de algoritmos genetiocpos

class LlamaControl:
    def __init__(self, camara):
        self.camara = camara                                      
        
        self.PIDtemp = PID(229, 1.5, 0.01)
        self.SetTemp = 0.0
        self.PIDtemp.output_limits = (0, 255)
        self.PIDtemp.sample_time = 0.001
        #self.PIDtemp.proportional_on_measurement = True
        
        
        self.PIDhume = PID(60, 75, 0)
        self.SetHume= 0.0
        self.PIDhume.output_limits = (0, 1)
        self.PIDhume.sample_time =0.5      
    
    def ControlTemperatura(self, control, Sensor, Objetivo):               
        
        if control == "PID":
            if self.SetTemp != Objetivo:
                self.SetTemp = Objetivo
                self.ActualizarPIDTempObje(self.SetTemp)       
                     
            NivelCalefaccion = self.PIDtemp(Sensor)           
                     
        if control == "FUZZY":
            NivelCalefaccion = 666            
                    
        if control == "ANN":
            NivelCalefaccion = 777            
                            
        return NivelCalefaccion    
    
    def ActualizarPIDTempObje(self, Objetivo):
        self.PIDtemp.setpoint = Objetivo
        #print("Actualizamos")
    
    def ActualizarPIDHumeObje(self, Objetivo):
        self.PIDhume.setpoint = Objetivo
        #print("Actualizamos")
    
    def ActualizarParametrosPID(self, Kp, Ki, Kd):
        print(Kp)
        print(Ki)
        print(Kd)
        self.PIDtemp.tunings = (Kp, Ki, Kd)
        
      
    def ControlHumedad(self, control, Sensor, Objetivo):               
        if control == "PID":
            if self.SetHume != Objetivo:
                self.SetHume = Objetivo
                self.ActualizarPIDHumeObje(self.SetHume)
                     
            NivelHumedad = self.PIDhume(Sensor)           
                     
        if control == "FUZZY":
            NivelHumedad = 666            
                    
        if control == "ANN":
            NivelHumedad = 777            
                            
        return NivelHumedad
    
