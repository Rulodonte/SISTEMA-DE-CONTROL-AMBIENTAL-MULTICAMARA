from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtChart import *
import sys
from PyQt5.QtGui import QIcon

from PyQt5 import QtChart
from Ecuaciones import *
from PyQt5.QtCore import QDate, Qt, QThread


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.Ecuacion = LlamaEcuaciones()
   
    def GraficaControl(self, DataFrame, CamaraSeleccionada):
        Xi = 0
        self.CurvaControl = QLineSeries()
        
        for Xi in range (24):
            listalineal = DataFrame.at[CamaraSeleccionada, "Parametros"]
            Yi = self.Ecuacion.EcuacionExperimental(listalineal, Xi)
            #Yi = round(Yi)
            self.CurvaControl.append(Xi, Yi)

        chart =  QChart()
               
        chart.addSeries(self.CurvaControl)        
        
        #chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Grafica control de temperatura")       
        
        ########
        axis_X = QtChart.QValueAxis()
        axis_X.setTickCount(24)
        axis_X.setTitleText("Horas (h)")
        axis_X.setRange(0, 23)
        axis_X.setLabelFormat('%.0f')
        
        chart.setAxisX(axis_X, self.CurvaControl)
        
        axis_Y = QtChart.QValueAxis()
        axis_Y.setTickCount(23)
        axis_Y.setTitleText("Temperatura (C)")
        axis_Y.setRange(0, 46)
        axis_Y.setLabelFormat('%.0f')
        
        chart.setAxisY(axis_Y, self.CurvaControl)
        #########
        
        chartview = QChartView(chart)

        return chartview
    
    def GraficaMonitor(self, FinalDataFrame):
        Cam1Series = QLineSeries()
        Cam2Series = QLineSeries()
        Cam3Series = QLineSeries()
        Cam4Series = QLineSeries()
        Cam5Series = QLineSeries()
        Cam6Series = QLineSeries()
        Cam7Series = QLineSeries()
        Cam8Series = QLineSeries()
        Cam9Series = QLineSeries()
        Cam10Series = QLineSeries()
        Cam11Series = QLineSeries()
        Cam12Series = QLineSeries()
        Cam13Series = QLineSeries()
        Cam14Series = QLineSeries()
        Cam15Series = QLineSeries()
        
        linea = 0
        vuelta = 0
       
        for camara in FinalDataFrame.index:  # Recorre todo el indice
            linea = linea + 1
            
            if linea == 1:
                Cam1Series.append(vuelta, FinalDataFrame.iloc[camara,3])
            if linea == 2:
                Cam2Series.append(vuelta, FinalDataFrame.iloc[camara,3])
            if linea == 3:
                Cam3Series.append(vuelta, FinalDataFrame.iloc[camara,3])
            if linea == 4:
                Cam4Series.append(vuelta, FinalDataFrame.iloc[camara,3])
            if linea == 5:
                Cam5Series.append(vuelta, FinalDataFrame.iloc[camara,3])
            if linea == 6:
                Cam6Series.append(vuelta, FinalDataFrame.iloc[camara,3])
            if linea == 7:
                Cam7Series.append(vuelta, FinalDataFrame.iloc[camara, 3])
            if linea == 8:
                Cam8Series.append(vuelta, FinalDataFrame.iloc[camara, 3])
            if linea == 9:
                Cam9Series.append(vuelta, FinalDataFrame.iloc[camara, 3])
            if linea == 10:
                Cam10Series.append(vuelta, FinalDataFrame.iloc[camara, 3])
            if linea == 11:
                Cam11Series.append(vuelta, FinalDataFrame.iloc[camara, 3])
            if linea == 12:
                Cam12Series.append(vuelta, FinalDataFrame.iloc[camara, 3])
            if linea == 13:
                Cam13Series.append(vuelta, FinalDataFrame.iloc[camara, 3])
            if linea == 14:
                Cam14Series.append(vuelta, FinalDataFrame.iloc[camara, 3])
            if linea == 15:
                Cam15Series.append(vuelta, FinalDataFrame.iloc[camara, 3])
                linea = 0
                vuelta = vuelta + 1
            
            chart =  QChart()
               
        chart.addSeries(Cam1Series)
        chart.addSeries(Cam2Series)
        chart.addSeries(Cam3Series)
        chart.addSeries(Cam4Series)
        chart.addSeries(Cam5Series)
        chart.addSeries(Cam6Series)
        chart.addSeries(Cam7Series)
        chart.addSeries(Cam8Series)
        chart.addSeries(Cam9Series)
        chart.addSeries(Cam10Series)
        chart.addSeries(Cam11Series)
        chart.addSeries(Cam12Series)
        chart.addSeries(Cam13Series)
        chart.addSeries(Cam14Series)
        chart.addSeries(Cam15Series)
       
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Temperatura y humedad de todas los compartimientos")
        
        ######## Cam1Series
        axis_X = QtChart.QValueAxis()
        axis_X.setTickCount(7)
        axis_X.setTitleText("Horas (h)")
        axis_X.setRange(0, 24)
        axis_X.setLabelFormat('%.0f') 
        
        chart.setAxisX(axis_X, Cam1Series)
        chart.setAxisX(axis_X, Cam2Series)
        chart.setAxisX(axis_X, Cam3Series)
        chart.setAxisX(axis_X, Cam4Series)
        chart.setAxisX(axis_X, Cam5Series)
        chart.setAxisX(axis_X, Cam6Series)
        chart.setAxisX(axis_X, Cam7Series)
        chart.setAxisX(axis_X, Cam8Series)
        chart.setAxisX(axis_X, Cam9Series)
        chart.setAxisX(axis_X, Cam10Series)
        chart.setAxisX(axis_X, Cam11Series)
        chart.setAxisX(axis_X, Cam12Series)
        chart.setAxisX(axis_X, Cam13Series)
        chart.setAxisX(axis_X, Cam14Series)
        chart.setAxisX(axis_X, Cam15Series)
        
        axis_Y = QtChart.QValueAxis()
        axis_Y.setTitleText("Temperatura (C)")
        axis_Y.setRange(0, 80)
        axis_Y.setLabelFormat('%.0f') 
        
        chart.setAxisY(axis_Y, Cam1Series)
        chart.setAxisY(axis_Y, Cam2Series)
        chart.setAxisY(axis_Y, Cam3Series)
        chart.setAxisY(axis_Y, Cam4Series)
        chart.setAxisY(axis_Y, Cam5Series)
        chart.setAxisY(axis_Y, Cam6Series)
        chart.setAxisY(axis_Y, Cam7Series)
        chart.setAxisY(axis_Y, Cam8Series)
        chart.setAxisY(axis_Y, Cam9Series)
        chart.setAxisY(axis_Y, Cam10Series)
        chart.setAxisY(axis_Y, Cam11Series)
        chart.setAxisY(axis_Y, Cam12Series)
        chart.setAxisY(axis_Y, Cam13Series)
        chart.setAxisY(axis_Y, Cam14Series)
        chart.setAxisY(axis_Y, Cam15Series)           
        #########
        
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)

        return chartview

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec_())