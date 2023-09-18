import sys
import glob
import serial
from PyQt5.QtWidgets import QDialog, QApplication
from PuertoSerial import *

class ConfigPuertoSerial(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.PuertoSeleccionado = ""
        self.BaudiosSeleccionado = ""
               
        self.CargarDatosPuertoSerial()
        
        self.ui.ComboBoxPuertoSerial.activated.connect(self.DatosPuertoSerial)
        self.ui.ComboBoxBaudios.activated.connect(self.DatosPuertoSerial)
                       
        self.show()
    
    def CargarDatosPuertoSerial(self):
        #Variable puerto
        Puertos = self.AdquirirDatosPuertoSerial()
        
        #Variable Baudios
        Baudios = ["4800", "9600", "14400", "19200", "28800", "38400", "57600", "115200"]
        self.ui.ComboBoxPuertoSerial.clear()
               
        #Agrega las variables a las opciones alejir (Puerto y baudios)
        self.ui.ComboBoxPuertoSerial.addItems(Puertos)
        self.ui.ComboBoxBaudios.addItems(Baudios)
        
        #Llama funcion para asignar las variables del puerto serial
        self.DatosPuertoSerial()
              
    def DatosPuertoSerial(self):
        #Asigna el valor para las vraiables Puerto y Baudios
        self.PuertoSeleccionado = self.ui.ComboBoxPuertoSerial.currentText()
        self.BaudiosSeleccionado = self.ui.ComboBoxBaudios.currentText()
    
    def AdquirirDatosPuertoSerial(self):
        """ Este codigo lo encontre en linea"""

        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        
        return result   

    def GetPuertoBaudios(self):
        return[self.PuertoSeleccionado, self.BaudiosSeleccionado]
    

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = ConfigPuertoSerial()
    w.show()
    sys.exit(app.exec_())