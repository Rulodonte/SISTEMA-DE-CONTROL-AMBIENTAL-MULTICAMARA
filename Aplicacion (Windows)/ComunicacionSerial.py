import serial        
import time
from datetime import date
import pandas as pd
import numpy as np
from DataFrameTemporal import *

class Comunicacion:
    def __init__(self, Puerto, Baudios):
        self.Puerto = Puerto
        self.Baudios = int(Baudios)
        self.SerialArduino = None

        self.TemporalDataFrame = TemporalDataframe()
        
    def ArduinoConect(self):
        self.SerialArduino = serial.Serial(self.Puerto, self.Baudios, timeout=1.0)   
        time.sleep(3)
    
    def ArduinoDesconect(self):
        self.SerialArduino.close()
        time.sleep(3)
           
    def ArduinoData(self, FinalString):        
        enviar = FinalString 
        GetData = str(enviar)
        self.SerialArduino.write(GetData.encode('ascii'))
        DataRaw = self.SerialArduino.readline().decode('ascii') 
        DataRaw = self.SerialArduino.readline().decode('ascii').strip() 
        SplitData = DataRaw.split(';')

        #print(SplitData)        
        return SplitData

    def ArduinoProcesarData(self, DataFrame, Extractores, Compresor):
        FinalString = ""
        InicialString = ""
                
        for camara in range(15):          
            InicialString = str(DataFrame.at[camara, "Compartimiento"]) + "," +  str(DataFrame.at[camara, "Dimmer"]) + "," + str(DataFrame.at[camara, "Humificador"]) 
            
            if camara < 14:
                InicialString = InicialString + ","

            FinalString = FinalString + InicialString
           
        FinalString = FinalString + "," +  Extractores + "," + Compresor 
        
        #print(FinalString)                
        SplitData = self.ArduinoData(FinalString)
        print(SplitData)

        DataOfList = len(SplitData)
       
        VarFecha = date.today()
        VarTiempo = time.strftime("%H:%M:%S")                
        VarHora = time.strftime("%H")
        
        if DataOfList == 15:
            for index in range(len(SplitData)):
                DatosCamara = SplitData[index]
                data =  DatosCamara.split(",")
                
                if data[0] == "nan" or data[1] == "nan":
                    temp = 0.0
                    hume = 0.0 
                else:
                    temp = float(data[0])  
                    hume = float(data[1])
                    
                DataFrame.at[index, "Fecha"] = VarFecha
                DataFrame.at[index, "Hora"] = VarTiempo
                
                DataFrame.at[index, "Temperatura"] = temp
                DataFrame.at[index, "Humedad"] = hume

            return DataFrame                                

        if DataOfList != 15:
            print("entro correccion")
            time.sleep(2)
            self.ArduinoDesconect()
            self.ArduinoConect()
            return self.TemporalDataFrame.dfError