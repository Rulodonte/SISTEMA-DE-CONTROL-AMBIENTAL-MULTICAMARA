import os
import time 
from datetime import date
from enum import Flag
import sys
import statistics
from PyQt5 import QtChart
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QDialog, QApplication
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import QDate, Qt, QThread

import plotly.express as px

from datetime import date
import pandas as pd
import openpyxl
import numpy as np
import threading

from sympy import arg, true

from ComunicacionSerial import *
from InterfaseUsuario import *
from ConfigPuertoSerial import *
from DataFrameTemporal import *
from Ecuaciones import *
from ControlInteligente import *
from Graficas import *

class Main(QMainWindow,QtCore.QThread):
    def __init__(self):
        self.Puerto = "None"
        self.Baudios = "0000"
        self.FlagThread = None
        self.CamaraSeleccionada = 0

        self.Compresor = "0"
        self.Extractores = "0"

        self.VarFecha = date.today()       
        self.VarTiempo = time.strftime("%H-%M-%S")                
              
        self.NombreArchivo = "Salida con Fecha" + " " + str(self.VarFecha.year) + "-" + str(self.VarFecha.month) + "-" +  str(self.VarFecha.day) + " " + "Hora" + " " + self.VarTiempo + ".xlsx" 
        

        self.ComunicacionSerialArduino = Comunicacion(self.Puerto, self.Baudios)
        self.TemporalDataFrame = TemporalDataframe()
        self.FinalDataFrame = pd.DataFrame()
        self.Ecuacion = LlamaEcuaciones()

        self.Cam1 = LlamaControl(0)
        self.Cam2 = LlamaControl(1)
        self.Cam3 = LlamaControl(2)
        self.Cam4 = LlamaControl(3)
        self.Cam5 = LlamaControl(4)
        self.Cam6 = LlamaControl(5)
        self.Cam7 = LlamaControl(6)
        self.Cam8 = LlamaControl(7)
        self.Cam9 = LlamaControl(8)
        self.Cam10 = LlamaControl(9)
        self.Cam11 = LlamaControl(10)
        self.Cam12 = LlamaControl(11)
        self.Cam13 = LlamaControl(12)
        self.Cam14 = LlamaControl(13)
        self.Cam15 = LlamaControl(14) 

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btn_Stop.setEnabled(False)
        self.ui.Btn_Monitor.setEnabled(False)
        self.ui.Btn_Graficas.setEnabled(False)
        self.ui.Btn_Control.setEnabled(False)
        self.ui.Btn_BaseDeDatos.setEnabled(False)
        
        self.ui.Btn_Play.clicked.connect(self.Conectar)
        self.ui.Btn_Stop.clicked.connect(self.Desconectar)
        self.ui.Btn_Monitor.clicked.connect(self.MostrarMenuMonitor)
        self.ui.Btn_Graficas.clicked.connect(self.MostrarMenuGrafica)
        self.ui.Btn_Control.clicked.connect(self.MostrarMenuControl)
        
        self.ui.Btn_GraficarMonitor.clicked.connect(self.GraficaGeneralMonitor)
                
        self.ui.CamaraComboBox.activated.connect(self.SeleccionarCamara)

        self.ui.RadioButtonConst.clicked.connect(lambda:self.CargarTipoCurva("Const"))
        self.ui.RadioButtonExp.clicked.connect(lambda:self.CargarTipoCurva("Exp"))

        self.ui.SliderTemp.valueChanged.connect(self.SliderConstante)

        self.ui.SliderAX.valueChanged.connect(self.SliderExp)
        self.ui.SliderAY.valueChanged.connect(self.SliderExp)
        self.ui.SliderBX.valueChanged.connect(self.SliderExp)
        self.ui.SliderBY.valueChanged.connect(self.SliderExp)
        self.ui.SliderCX.valueChanged.connect(self.SliderExp)
        self.ui.SliderCY.valueChanged.connect(self.SliderExp)
        self.ui.SliderDX.valueChanged.connect(self.SliderExp)
        self.ui.SliderDY.valueChanged.connect(self.SliderExp)
        self.ui.SliderEX.valueChanged.connect(self.SliderExp)
        self.ui.SliderEY.valueChanged.connect(self.SliderExp)
        self.ui.SliderFX.valueChanged.connect(self.SliderExp)
        self.ui.SliderFY.valueChanged.connect(self.SliderExp)

        self.ui.SliderHumedad.valueChanged.connect(self.SliderHumedadRelativa)
        
        self.SeleccionarCamara()

        self.show()
    
    def MostrarMenuMonitor(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.StackedMonitor)
    
    def MostrarMenuGrafica(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.StackedGraficas)
            
    def MostrarMenuControl(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.StackedControl)

    def Conectar(self):
        #Adquirimos los valores para Puerto Serial(COM1, COM2, etc) y Baudios
        DatosPuertoSerial = ConfigPuertoSerial()  
        DatosPuertoSerial.exec()
        Puerto = DatosPuertoSerial.PuertoSeleccionado
        Baudios = DatosPuertoSerial.BaudiosSeleccionado
        
        #Asigan los valores para Puerto y Baudios en
        self.ComunicacionSerialArduino.Puerto = Puerto
        self.ComunicacionSerialArduino.Baudios = Baudios  

        #Conecta Ardiuno con aplicacion Windows
        self.ComunicacionSerialArduino.ArduinoConect()

        #Habilitamos todos los botones de control nesesarios 
        # e inhabilitamos el boton de conectar
        self.ui.Btn_Play.setEnabled(False)
        self.ui.Btn_Stop.setEnabled(True)
        self.ui.Btn_Monitor.setEnabled(True)
        self.ui.Btn_Graficas.setEnabled(True)
        self.ui.Btn_Control.setEnabled(True)
        self.ui.Btn_BaseDeDatos.setEnabled(True)
        
        self.EstadoThreads("ON", "Solicitud")
        
    def Desconectar(self):
        self.EstadoThreads("OFF", "Solicitud")               
                                      
        #Desconecta puerto serial
        self.ComunicacionSerialArduino.ArduinoDesconect()

        
        #Deshabilita todos los botones y habilita el boton conectar
        self.ui.Btn_Stop.setEnabled(False)
        self.ui.Btn_Play.setEnabled(True)
        self.ui.Btn_Stop.setEnabled(False)
        self.ui.Btn_Monitor.setEnabled(False)
        self.ui.Btn_Graficas.setEnabled(False)
        self.ui.Btn_Control.setEnabled(False)
        self.ui.Btn_BaseDeDatos.setEnabled(False)
        
        #Regresa todos loa valores de las cámaras a modo inicial
        self.ui.Btn_Camara1.setText("Cámara: " + "1" +"\n" )
        self.ui.Btn_Camara2.setText("Cámara: " + "2" +"\n" )
        self.ui.Btn_Camara3.setText("Cámara: " + "3" +"\n" )
        self.ui.Btn_Camara4.setText("Cámara: " + "4" +"\n" )
        self.ui.Btn_Camara5.setText("Cámara: " + "5" +"\n" )
        self.ui.Btn_Camara6.setText("Cámara: " + "6" +"\n" )
        self.ui.Btn_Camara7.setText("Cámara: " + "7" +"\n" )
        self.ui.Btn_Camara8.setText("Cámara: " + "8" +"\n" )
        self.ui.Btn_Camara9.setText("Cámara: " + "9" +"\n" )
        self.ui.Btn_Camara10.setText("Cámara: " + "10" +"\n" )
        self.ui.Btn_Camara11.setText("Cámara: " + "11" +"\n" )
        self.ui.Btn_Camara12.setText("Cámara: " + "12" +"\n" )
        self.ui.Btn_Camara13.setText("Cámara: " + "13" +"\n" )
        self.ui.Btn_Camara14.setText("Cámara: " + "14" +"\n" )
        self.ui.Btn_Camara15.setText("Cámara: " + "15" +"\n" )        
    
    def EstadoThreads(self, Estado, Solicitud):                
        if  Estado == "ON" and Solicitud == "Solicitud":
            self.FlagThread = False
            self.Threads()           
        
        if  Estado == "OFF" and Solicitud == "Solicitud":
            self.FlagThread = True 
        
        if  Estado == "Estado" and Solicitud == "Solicitud":
            return self.FlagThread
    
    def Threads(self):              # Inicia todos los Thread
        self.DetenerThread = threading.Event()        
        
        self.ThreadObtenerDatosArduino = threading.Thread(target = self.ObtenerDatosArduino)               
        self.ThreadObtenerDatosArduino.start()   # Iniciamos la ejecución del thread

        time.sleep(3)

        self.ThreadGrabarDataFrameExcel = threading.Thread(target = self.GrabarDataFrameExcel)               
        self.ThreadGrabarDataFrameExcel.start()   # Iniciamos la ejecución del thread,

        self.ThreadDatosMiniMonitorIndividual = threading.Thread(target = self.DatosMiniMonitorIndividual)               
        self.ThreadDatosMiniMonitorIndividual.start()   # Iniciamos la ejecución del thread,

        self.ThreadControlAmbiental = threading.Thread(target = self.ControlAmbiental)               
        self.ThreadControlAmbiental.start()   # Iniciamos la ejecución del thread,

        self.ThreadControlCompresor = threading.Thread(target = self.ControlCompresor)               
        self.ThreadControlCompresor.start()

    def ObtenerDatosArduino(self):  # Obtiene los datos del Arduino y los pone en un DataFrame Temporal
        lecturas = 0
        while True: 
            lecturas  = lecturas + 1         
            estado = self.EstadoThreads("Estado", "Solicitud")
            if  estado == True:               
                self.DetenerThread.set()
                break
            else:
                self.TemporalDataFrame.df = self.ComunicacionSerialArduino.ArduinoProcesarData(self.TemporalDataFrame.df, self.Extractores , self.Compresor)
                                   
            self.DatosMonitorGeneral()

            ##os.system("cls")
            print("Numero de lectura", lecturas)
            print(self.TemporalDataFrame.df)
            time.sleep(1)               
            
    def GrabarDataFrameExcel(self): # Guarda los datos en un excel
        while True:
            estado = self.EstadoThreads("Estado", "Solicitud")
            if  estado == True:               
                self.DetenerThread.set()
                break
            else:            
                self.FinalDataFrame = pd.concat([self.FinalDataFrame, self.TemporalDataFrame.df])
                self.FinalDataFrame.to_excel(self.NombreArchivo, 'Datos Camara')      
                time.sleep(60)           

    def DatosMonitorGeneral(self):  # Muestra humedad y temperattura de las 15 cámaras       
        self.ui.Btn_Camara1.setText("Cámara: " + "1" +"\n" + str(self.TemporalDataFrame.df.at[0, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[0, "Humedad"]) + " %")
        self.ui.Btn_Camara2.setText("Cámara: " + "2" +"\n" + str(self.TemporalDataFrame.df.at[1, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[1, "Humedad"]) + " %")
        self.ui.Btn_Camara3.setText("Cámara: " + "3" +"\n" + str(self.TemporalDataFrame.df.at[2, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[2, "Humedad"]) + " %")
        self.ui.Btn_Camara4.setText("Cámara: " + "4" +"\n" + str(self.TemporalDataFrame.df.at[3, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[3, "Humedad"]) + " %")
        self.ui.Btn_Camara5.setText("Cámara: " + "5" +"\n" + str(self.TemporalDataFrame.df.at[4, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[4, "Humedad"]) + " %")
        self.ui.Btn_Camara6.setText("Cámara: " + "6" +"\n" + str(self.TemporalDataFrame.df.at[5, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[5, "Humedad"]) + " %")
        self.ui.Btn_Camara7.setText("Cámara: " + "7" +"\n" + str(self.TemporalDataFrame.df.at[6, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[6, "Humedad"]) + " %")
        self.ui.Btn_Camara8.setText("Cámara: " + "8" +"\n" + str(self.TemporalDataFrame.df.at[7, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[7, "Humedad"]) + " %")
        self.ui.Btn_Camara9.setText("Cámara: " + "9" +"\n" + str(self.TemporalDataFrame.df.at[8, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[8, "Humedad"]) + " %")
        self.ui.Btn_Camara10.setText("Cámara: " + "10" +"\n" + str(self.TemporalDataFrame.df.at[9, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[9, "Humedad"]) + " %")
        self.ui.Btn_Camara11.setText("Cámara: " + "11" +"\n" + str(self.TemporalDataFrame.df.at[10, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[10, "Humedad"]) + " %")
        self.ui.Btn_Camara12.setText("Cámara: " + "12" +"\n" + str(self.TemporalDataFrame.df.at[11, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[11, "Humedad"]) + " %")
        self.ui.Btn_Camara13.setText("Cámara: " + "13" +"\n" + str(self.TemporalDataFrame.df.at[12, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[12, "Humedad"]) + " %")
        self.ui.Btn_Camara14.setText("Cámara: " + "14" +"\n" + str(self.TemporalDataFrame.df.at[13, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[13, "Humedad"]) + " %")
        self.ui.Btn_Camara15.setText("Cámara: " + "15" +"\n" + str(self.TemporalDataFrame.df.at[14, "Temperatura"]) + " °C" + "\n"+ str(self.TemporalDataFrame.df.at[14, "Humedad"]) + " %")
    
    def DatosMiniMonitorIndividual(self):
         while True:
            estado = self.EstadoThreads("Estado", "Solicitud")
            if  estado == True:               
                self.DetenerThread.set()
                break
            else:    
                self.ui.LabelTemp.setText(str(self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Temperatura"]) + " °C")
                self.ui.LabelHume.setText(str(self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Humedad"]) + " %")
                self.ui.LabelCale.setText(str(self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Dimmer"]) + " PWM")
                
                if self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Humificador"] == 1:
                    self.ui.LabelVenti.setText("ON")
                else:
                    self.ui.LabelVenti.setText("OFF")

                time.sleep(0.1) 
    
    def SeleccionarCamara(self):
        Camara = self.ui.CamaraComboBox.currentIndex()
        self.CamaraSeleccionada = int(Camara)
        
        self.ActualizaAmbianteCamara()
        self.GraficaControl()
    
    def CargarTipoCurva(self, Curva):
        if Curva == "Const":
            self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Set Curva"] = "Const"                      
            self.ui.RadioButtonConst.setChecked(True)
            self.ActualizaAmbianteCamara()
                                                                      
        if Curva == "Exp":
            self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Set Curva"] = "Exp"           
            self.ui.RadioButtonExp.setChecked(True)
            self.ActualizaAmbianteCamara()

    def SliderConstante(self):
        DataList = self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Parametros"]
        valor = self.ui.SliderTemp.value()
        DataList[1] = valor
        DataList[3] = valor
        DataList[5] = valor
        DataList[7] = valor
        DataList[9] = valor
        DataList[11] = valor
        self.ui.label_32.setText("Temperatura: " + str(DataList[1]) + " °C")
        self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Parametros"]  = DataList
        
        VarHora = time.strftime("%H")        
        
        listalineal = self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Parametros"]                
        Yi = self.Ecuacion.EcuacionExperimental(listalineal, int(VarHora))
        #Yi = round(Yi)
        self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Temperatura_Objetivo"] =  Yi
        
        self.GraficaControl()
    
    def SliderExp(self):
        DataList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # mejor pasar el list como argumento
        
        self.ui.SliderAX.setRange(0, 0)             
        DataList[0] = self.ui.SliderAX.value()
        DataList[1] = self.ui.SliderAY.value()
        self.ui.label_9.setText("Hora: " + str(DataList[0]))
        self.ui.label_10.setText("Temperatura: " + str(DataList[1]))
        
        self.ui.SliderBX.setRange(DataList[0] + 1, 19)        
        DataList[2] = self.ui.SliderBX.value()
        DataList[3] = self.ui.SliderBY.value()
        self.ui.label_11.setText("Hora: " + str(DataList[2]))
        self.ui.label_12.setText("Temperatura: " + str(DataList[3]))
        
        self.ui.SliderCX.setRange(DataList[2] + 1, 20)
        DataList[4] = self.ui.SliderCX.value()
        DataList[5] = self.ui.SliderCY.value()
        self.ui.label_14.setText("Hora: " + str(DataList[4]))
        self.ui.label_15.setText("Temperatura: " + str(DataList[5]))
        
        self.ui.SliderDX.setRange(DataList[4] + 1, 21)
        DataList[6] = self.ui.SliderDX.value()
        DataList[7] = self.ui.SliderDY.value()
        self.ui.label_17.setText("Hora: " + str(DataList[6]))
        self.ui.label_18.setText("Temperatura: " + str(DataList[7]))
        
        self.ui.SliderEX.setRange(DataList[6] + 1, 22)
        DataList[8] = self.ui.SliderEX.value()
        DataList[9] = self.ui.SliderEY.value()
        self.ui.label_20.setText("Hora: " + str(DataList[8]))
        self.ui.label_21.setText("Temperatura: " + str(DataList[9]))
        
        self.ui.SliderFX.setRange(23, 23)
        DataList[10] = self.ui.SliderFX.value()
        DataList[11] = self.ui.SliderFY.value()
        self.ui.label_23.setText("Hora: " + str(DataList[10]))
        self.ui.label_24.setText("Temperatura: " + str(DataList[11]))        
                
        self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Parametros"] = DataList
        
        VarHora = time.strftime("%H")        
        
        listalineal = self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Parametros"]                
        Yi = self.Ecuacion.EcuacionExperimental(listalineal, int(VarHora))
        self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Temperatura_Objetivo"] =  Yi
        
        self.GraficaControl()
    
    def SliderHumedadRelativa(self):        
        HumedadRelativa = self.ui.SliderHumedad.value()
        self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Humedad_Relativa_Objetivo"]  = HumedadRelativa
        self.ui.label_27.setText("Humedad relativa: " + str(HumedadRelativa) + " %")       
        
    def ActualizaAmbianteCamara(self):
        HumedadRelativa = self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Humedad_Relativa_Objetivo"]
        self.ui.SliderHumedad.setValue(int(HumedadRelativa))
        self.ui.label_27.setText("Humedad relativa: " + str(HumedadRelativa) + " %")
      
                
        if  self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Set Curva"] == "Const":

            self.ui.frame_28.setDisabled(False)
            self.ui.frame_15.setDisabled(True)

            Datalist = self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Parametros"]
            self.ui.RadioButtonConst.setChecked(True)
            self.ui.SliderTemp.setValue(Datalist[1])

        if self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Set Curva"] == "Exp":
            self.ui.frame_28.setDisabled(True)
            self.ui.frame_15.setDisabled(False) 
            
            Datalist = self.TemporalDataFrame.df.at[self.CamaraSeleccionada, "Parametros"]
            self.ui.RadioButtonExp.setChecked(True)
                       
            self.ui.SliderAX.setValue(Datalist[0])
            self.ui.SliderAY.setValue(Datalist[1])
            
            self.ui.SliderBX.setValue(Datalist[2])
            self.ui.SliderBY.setValue(Datalist[3])
            
            self.ui.SliderCX.setValue(Datalist[4])
            self.ui.SliderCY.setValue(Datalist[5])
            
            self.ui.SliderDX.setValue(Datalist[6])
            self.ui.SliderDY.setValue(Datalist[7])
            
            self.ui.SliderEX.setValue(Datalist[8])
            self.ui.SliderEY.setValue(Datalist[9])
            
            self.ui.SliderFX.setValue(Datalist[10])
            self.ui.SliderFY.setValue(Datalist[11])        

    def GraficaControl(self):
        for i in reversed(range(self.ui.LayoutControl.count())): 
            self.ui.LayoutControl.itemAt(i).widget().setParent(None)

        MostrarGraficas = Window()
        chartview = MostrarGraficas.GraficaControl(self.TemporalDataFrame.df,self.CamaraSeleccionada)
        self.ui.LayoutControl.addWidget(chartview)
    
    def GraficaGeneralMonitor(self):
        self.ui.layoutgrafica.itemAt(0).widget().deleteLater()  # borra qwidget frafica
        MostrarGraficas = Window()
        chartview = MostrarGraficas.GraficaMonitor(self.FinalDataFrame)
        self.ui.layoutgrafica.addWidget(chartview)        
            
    def ControlCompresor(self):
        self.Compresor = "0"
        IndiceTempMin = []
        Temperaturas = []
        #time.sleep(1200)
        while True:
            estado = self.EstadoThreads("Estado", "Solicitud")
            if  estado == True:               
                self.DetenerThread.set()
                break
            else:
                listTempObjetivo = [self.TemporalDataFrame.df.at[0, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[1, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[2, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[3, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[4, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[5, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[6, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[7, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[8, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[9, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[10, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[11, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[12, "Temperatura_Objetivo"],
                                    self.TemporalDataFrame.df.at[13, "Temperatura_Objetivo"],                            
                                    self.TemporalDataFrame.df.at[14, "Temperatura_Objetivo"]]
                
                TempMinObjetivo = min(listTempObjetivo)                         
                count = 0
                
                for x in listTempObjetivo:    
                    if x == TempMinObjetivo:
                        IndiceTempMin.append(count)
                    count = count + 1 

                for x in IndiceTempMin:
                    Temperaturas.append = self.TemporalDataFrame.df.at[x, "Temperatura"]

                ActualTempMin = min(Temperaturas)

                if ActualTempMin >= TempMinObjetivo: 
                    self.Compresor = "1"
                                    
                if ActualTempMin <= (TempMinObjetivo-0.2):
                    self.Compresor = "0"
                               
            time.sleep(1)
 
    def ControlAmbiental(self):
         while True:
            estado = self.EstadoThreads("Estado", "Solicitud")
            if  estado == True:               
                self.DetenerThread.set()
                break
            else:                              
                PWM0 = self.Cam1.ControlTemperatura(self.TemporalDataFrame.df.at[0, "Tipo Control"], self.TemporalDataFrame.df.at[0, "Temperatura"], self.TemporalDataFrame.df.at[0, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[0, "Dimmer"] = int(PWM0)               
                                                
                PWM1 = self.Cam2.ControlTemperatura(self.TemporalDataFrame.df.at[1, "Tipo Control"], self.TemporalDataFrame.df.at[1, "Temperatura"], self.TemporalDataFrame.df.at[1, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[1, "Dimmer"] = int(PWM1)

                PWM2 = self.Cam3.ControlTemperatura(self.TemporalDataFrame.df.at[2, "Tipo Control"], self.TemporalDataFrame.df.at[2, "Temperatura"], self.TemporalDataFrame.df.at[2, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[2, "Dimmer"] = int(PWM2)

                PWM3 = self.Cam4.ControlTemperatura(self.TemporalDataFrame.df.at[3, "Tipo Control"], self.TemporalDataFrame.df.at[3, "Temperatura"], self.TemporalDataFrame.df.at[3, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[3, "Dimmer"] = int(PWM3)
                               
                PWM4 = self.Cam5.ControlTemperatura(self.TemporalDataFrame.df.at[4, "Tipo Control"], self.TemporalDataFrame.df.at[4, "Temperatura"], self.TemporalDataFrame.df.at[4, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[4, "Dimmer"] = int(PWM4)
                               
                PWM5 = self.Cam6.ControlTemperatura(self.TemporalDataFrame.df.at[5, "Tipo Control"], self.TemporalDataFrame.df.at[5, "Temperatura"], self.TemporalDataFrame.df.at[5, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[5, "Dimmer"] = int(PWM5)

                PWM6 = self.Cam7.ControlTemperatura(self.TemporalDataFrame.df.at[6, "Tipo Control"], self.TemporalDataFrame.df.at[6, "Temperatura"], self.TemporalDataFrame.df.at[6, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[6, "Dimmer"] = int(PWM6)

                PWM7 = self.Cam8.ControlTemperatura(self.TemporalDataFrame.df.at[7, "Tipo Control"], self.TemporalDataFrame.df.at[7, "Temperatura"], self.TemporalDataFrame.df.at[7, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[7, "Dimmer"] = int(PWM7)
                
                PWM8 = self.Cam9.ControlTemperatura(self.TemporalDataFrame.df.at[8, "Tipo Control"], self.TemporalDataFrame.df.at[8, "Temperatura"], self.TemporalDataFrame.df.at[8, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[8, "Dimmer"] = int(PWM8)
                
                PWM9 = self.Cam10.ControlTemperatura(self.TemporalDataFrame.df.at[9, "Tipo Control"], self.TemporalDataFrame.df.at[9, "Temperatura"], self.TemporalDataFrame.df.at[9, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[9, "Dimmer"] = int(PWM9)

                PWM10 = self.Cam11.ControlTemperatura(self.TemporalDataFrame.df.at[10, "Tipo Control"], self.TemporalDataFrame.df.at[10, "Temperatura"], self.TemporalDataFrame.df.at[10, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[10, "Dimmer"] = int(PWM10)
                
                PWM11 = self.Cam12.ControlTemperatura(self.TemporalDataFrame.df.at[11, "Tipo Control"], self.TemporalDataFrame.df.at[11, "Temperatura"], self.TemporalDataFrame.df.at[11, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[11, "Dimmer"] = int(PWM11)
                
                PWM12 = self.Cam13.ControlTemperatura(self.TemporalDataFrame.df.at[12, "Tipo Control"], self.TemporalDataFrame.df.at[12, "Temperatura"], self.TemporalDataFrame.df.at[12, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[12, "Dimmer"] = int(PWM12)
                
                PWM13 = self.Cam14.ControlTemperatura(self.TemporalDataFrame.df.at[13, "Tipo Control"], self.TemporalDataFrame.df.at[13, "Temperatura"], self.TemporalDataFrame.df.at[13, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[13, "Dimmer"] = int(PWM13)
                
                PWM14 = self.Cam15.ControlTemperatura(self.TemporalDataFrame.df.at[14, "Tipo Control"], self.TemporalDataFrame.df.at[14, "Temperatura"], self.TemporalDataFrame.df.at[14, "Temperatura_Objetivo"])
                self.TemporalDataFrame.df.at[14, "Dimmer"] = int(PWM14)

                ###################################                    HUMEDAD                #####################################
                ###################################################################################################################

                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[0, "Humedad"] >= self.TemporalDataFrame.df.at[0, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[0, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[0, "Humificador"] = int(1)
                else:
                    HumeCAM1 = self.Cam1.ControlHumedad(self.TemporalDataFrame.df.at[0, "Tipo Control"], self.TemporalDataFrame.df.at[0, "Humedad"], self.TemporalDataFrame.df.at[0, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[0, "Humificador"] = int(HumeCAM1)
                #####################################
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[1, "Humedad"] >= self.TemporalDataFrame.df.at[1, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[1, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[1, "Humificador"] = int(1)
                else:
                    HumeCAM2 = self.Cam2.ControlHumedad(self.TemporalDataFrame.df.at[1, "Tipo Control"], self.TemporalDataFrame.df.at[1, "Humedad"], self.TemporalDataFrame.df.at[1, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[1, "Humificador"] = int(HumeCAM2)
                #####################################
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[2, "Humedad"] >= self.TemporalDataFrame.df.at[2, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[2, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[2, "Humificador"] = int(1)
                else:
                    HumeCAM3 = self.Cam3.ControlHumedad(self.TemporalDataFrame.df.at[2, "Tipo Control"], self.TemporalDataFrame.df.at[2, "Humedad"], self.TemporalDataFrame.df.at[2, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[2, "Humificador"] = int(HumeCAM3)
                #####################################
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[3, "Humedad"] >= self.TemporalDataFrame.df.at[3, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[3, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[3, "Humificador"] = int(1)
                else:
                    HumeCAM4 = self.Cam4.ControlHumedad(self.TemporalDataFrame.df.at[3, "Tipo Control"], self.TemporalDataFrame.df.at[3, "Humedad"], self.TemporalDataFrame.df.at[3, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[3, "Humificador"] = int(HumeCAM4)
                #####################################
                
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[4, "Humedad"] >= self.TemporalDataFrame.df.at[4, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[4, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[4, "Humificador"] = int(1)
                else:
                    HumeCAM5 = self.Cam5.ControlHumedad(self.TemporalDataFrame.df.at[4, "Tipo Control"], self.TemporalDataFrame.df.at[4, "Humedad"], self.TemporalDataFrame.df.at[4, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[4, "Humificador"] = int(HumeCAM5)
                #####################################


                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[5, "Humedad"] >= self.TemporalDataFrame.df.at[5, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[5, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[5, "Humificador"] = int(1)
                else:
                    HumeCAM6 = self.Cam6.ControlHumedad(self.TemporalDataFrame.df.at[5, "Tipo Control"], self.TemporalDataFrame.df.at[5, "Humedad"], self.TemporalDataFrame.df.at[5, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[5, "Humificador"] = int(HumeCAM6)
                #####################################

                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[6, "Humedad"] >= self.TemporalDataFrame.df.at[6, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[6, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[6, "Humificador"] = int(1)
                else:
                    HumeCAM7 = self.Cam7.ControlHumedad(self.TemporalDataFrame.df.at[6, "Tipo Control"], self.TemporalDataFrame.df.at[6, "Humedad"], self.TemporalDataFrame.df.at[6, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[6, "Humificador"] = int(HumeCAM7)
                #####################################

                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[7, "Humedad"] >= self.TemporalDataFrame.df.at[7, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[7, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[7, "Humificador"] = int(1)
                else:
                    HumeCAM8 = self.Cam8.ControlHumedad(self.TemporalDataFrame.df.at[7, "Tipo Control"], self.TemporalDataFrame.df.at[7, "Humedad"], self.TemporalDataFrame.df.at[7, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[7, "Humificador"] = int(HumeCAM8)
                #####################################

                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[8, "Humedad"] >= self.TemporalDataFrame.df.at[8, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[8, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[8, "Humificador"] = int(1)
                else:
                    HumeCAM9 = self.Cam9.ControlHumedad(self.TemporalDataFrame.df.at[8, "Tipo Control"], self.TemporalDataFrame.df.at[8, "Humedad"], self.TemporalDataFrame.df.at[8, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[8, "Humificador"] = int(HumeCAM9)
                #####################################
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[9, "Humedad"] >= self.TemporalDataFrame.df.at[9, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[9, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[9, "Humificador"] = int(1)
                else:
                    HumeCAM10 = self.Cam10.ControlHumedad(self.TemporalDataFrame.df.at[9, "Tipo Control"], self.TemporalDataFrame.df.at[9, "Humedad"], self.TemporalDataFrame.df.at[9, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[9, "Humificador"] = int(HumeCAM10)
                #####################################
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[10, "Humedad"] >= self.TemporalDataFrame.df.at[10, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[10, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[10, "Humificador"] = int(1)
                else:
                    HumeCAM11 = self.Cam11.ControlHumedad(self.TemporalDataFrame.df.at[10, "Tipo Control"], self.TemporalDataFrame.df.at[10, "Humedad"], self.TemporalDataFrame.df.at[10, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[10, "Humificador"] = int(HumeCAM11)
                #####################################
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[11, "Humedad"] >= self.TemporalDataFrame.df.at[11, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[11, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[11, "Humificador"] = int(1)
                else:
                    HumeCAM12 = self.Cam12.ControlHumedad(self.TemporalDataFrame.df.at[11, "Tipo Control"], self.TemporalDataFrame.df.at[11, "Humedad"], self.TemporalDataFrame.df.at[11, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[11, "Humificador"] = int(HumeCAM12)
                #####################################
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[12, "Humedad"] >= self.TemporalDataFrame.df.at[12, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[12, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[12, "Humificador"] = int(1)
                else:
                    HumeCAM13 = self.Cam13.ControlHumedad(self.TemporalDataFrame.df.at[12, "Tipo Control"], self.TemporalDataFrame.df.at[12, "Humedad"], self.TemporalDataFrame.df.at[12, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[12, "Humificador"] = int(HumeCAM13)
                #####################################
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[13, "Humedad"] >= self.TemporalDataFrame.df.at[13, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[13, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[13, "Humificador"] = int(1)
                else:
                    HumeCAM14 = self.Cam14.ControlHumedad(self.TemporalDataFrame.df.at[13, "Tipo Control"], self.TemporalDataFrame.df.at[13, "Humedad"], self.TemporalDataFrame.df.at[13, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[13, "Humificador"] = int(HumeCAM14)
                #####################################
                
                if  self.Compresor == "1": 
                    if self.TemporalDataFrame.df.at[14, "Humedad"] >= self.TemporalDataFrame.df.at[14, "Humedad_Relativa_Objetivo"] + 5:
                        self.TemporalDataFrame.df.at[14, "Humificador"] = int(0)
                    else:
                        self.TemporalDataFrame.df.at[14, "Humificador"] = int(1)
                else:
                    HumeCAM15 = self.Cam15.ControlHumedad(self.TemporalDataFrame.df.at[14, "Tipo Control"], self.TemporalDataFrame.df.at[14, "Humedad"], self.TemporalDataFrame.df.at[14, "Humedad_Relativa_Objetivo"])
                    self.TemporalDataFrame.df.at[14, "Humificador"] = int(HumeCAM15)
                
                time.sleep(0.001)  #en milis segundos por que parece que eso influye


##############################################################################################################################################################################################        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())