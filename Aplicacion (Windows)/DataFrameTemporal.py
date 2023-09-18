import pandas as pd

class TemporalDataframe:
    def __init__(self):        
        self.colnames = ["Compartimiento",
                         "Fecha", 
                         "Hora",
                         "Temperatura", 
                         "Humedad", 
                         "Humificador", 
                         "Dimmer", 
                         "Set Curva", 
                         "Tipo Control",
                         "Temperatura_Objetivo",
                         "Humedad_Relativa_Objetivo", 
                         "Parametros"]

        #este es para evaluar
        self.df = pd.DataFrame([["1","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  32.00, 60.0, [0, 32,   7, 32,   9, 32,   14, 32,   17, 32,   23, 32,]],
                                ["2","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  34.00, 60.0, [0, 34,   7, 34,   9, 34,   14, 34,   17, 34,   23, 34,]],
                                ["3","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  36.00, 60.0, [0, 36,   7, 36,   9, 36,   14, 36,   17, 36,   23, 36,]],
                                ["4","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  38.00, 60.0, [0, 38,   7, 38,   9, 38,   14, 38,   17, 38,   23, 38,]],
                                ["5","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  40.00, 60.0, [0, 40,   7, 40,   9, 40,   14, 40,   17, 40,   23, 40,]],
                                ["6","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  32.00, 60.0, [0, 32,   7, 32,   9, 32,   14, 32,   22, 32,   23, 32,]],
                                ["7","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  34.00, 60.0, [0, 34,   7, 34,   9, 34,   14, 34,   17, 34,   23, 34,]],
                                ["8","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  36.00, 60.0, [0, 36,   7, 36,   9, 36,   14, 36,   17, 36,   23, 36,]],
                                ["9","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  38.00, 60.0, [0, 38,   7, 38,   9, 38,   14, 38,   17, 38,   23, 38,]],
                                ["10","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 40.00, 60.0, [0, 40,  7, 40,   9, 40,   14, 40,   17, 40,   23, 40,]],
                                ["11","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 32.00, 60.0, [0, 32,  7, 32,   9, 32,   14, 32,   17, 32,   23, 32,]],
                                ["12","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 34.00, 60.0, [0, 34,  7, 34,   9, 34,   14, 34,   17, 34,   23, 34,]],
                                ["13","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 36.00, 60.0, [0, 36,  7, 36,   9, 36,   16, 36,   17, 36,   23, 36,]],
                                ["14","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 38.00, 60.0, [0, 38,  7, 38,   9, 38,   14, 38,   17, 38,   23, 38,]],
                                ["15","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 40.00, 60.0, [0, 40,  7, 40,   9, 40,   14, 40,   17, 40,   23, 40,]]], columns = self.colnames)
        
        self.dfError = pd.DataFrame([["1","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  32.00, 60.0, [0, 32,   7, 32,   9, 32,   14, 32,   17, 32,   23, 32,]],
                                     ["2","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  34.00, 60.0, [0, 34,   7, 34,   9, 34,   14, 34,   17, 34,   23, 34,]],
                                     ["3","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  36.00, 60.0, [0, 36,   7, 36,   9, 36,   14, 36,   17, 36,   23, 36,]],
                                     ["4","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  38.00, 60.0, [0, 38,   7, 38,   9, 38,   14, 38,   17, 38,   23, 38,]],
                                     ["5","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  40.00, 60.0, [0, 40,   7, 40,   9, 40,   14, 40,   17, 40,   23, 40,]],
                                     ["6","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  32.00, 60.0, [0, 32,   7, 32,   9, 32,   14, 32,   22, 32,   23, 32,]],
                                     ["7","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  34.00, 60.0, [0, 34,   7, 34,   9, 34,   14, 34,   17, 34,   23, 34,]],
                                     ["8","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  36.00, 60.0, [0, 36,   7, 36,   9, 36,   14, 36,   17, 36,   23, 36,]],
                                     ["9","07/12/2021","11:19",  0.00, 0.00, 0, 0, "Const", "PID",  38.00, 60.0, [0, 38,   7, 38,   9, 38,   14, 38,   17, 38,   23, 38,]],
                                     ["10","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 40.00, 60.0, [0, 40,  7, 40,   9, 40,   14, 40,   17, 40,   23, 40,]],
                                     ["11","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 32.00, 60.0, [0, 32,  7, 32,   9, 32,   14, 32,   17, 32,   23, 32,]],
                                     ["12","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 34.00, 60.0, [0, 34,  7, 34,   9, 34,   14, 34,   17, 34,   23, 34,]],
                                     ["13","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 36.00, 60.0, [0, 36,  7, 36,   9, 36,   16, 36,   17, 36,   23, 36,]],
                                     ["14","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 38.00, 60.0, [0, 38,  7, 38,   9, 38,   14, 38,   17, 38,   23, 38,]],
                                     ["15","07/12/2021","11:19", 0.00, 0.00, 0, 0, "Const", "PID", 40.00, 60.0, [0, 40,  7, 40,   9, 40,   14, 40,   17, 40,   23, 40,]]], columns = self.colnames)
        
        """self.df = pd.DataFrame([["1","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  22.00, 60.0, [0, 22,   7, 22,   9, 22,   14, 22,   17, 22,   23, 22,]],
                                ["2","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  27.00, 60.0, [0, 27,   7, 27,   9, 27,   14, 27,   17, 27,   23, 27,]],
                                ["3","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  32.00, 60.0, [0, 32,   7, 32,   9, 32,   14, 32,   17, 32,   23, 32,]],
                                ["4","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  37.00, 60.0, [0, 37,   7, 37,   9, 37,   14, 37,   17, 37,   23, 37,]],
                                ["5","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  40.00, 60.0, [0, 40,   7, 40,   9, 40,   14, 40,   17, 40,   23, 40,]],
                                ["6","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  22.00, 60.0, [0, 22,   7, 22,   9, 22,   14, 22,   22, 37,   23, 22,]],
                                ["7","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  27.00, 60.0, [0, 27,   7, 27,   9, 27,   14, 27,   17, 27,   23, 27,]],
                                ["8","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  32.00, 60.0, [0, 32,   7, 32,   9, 32,   14, 32,   17, 32,   23, 32,]],
                                ["9","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  37.00, 60.0, [0, 37,   7, 37,   9, 37,   14, 37,   17, 37,   23, 37,]],
                                ["10","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 40.00, 60.0, [0, 40,  7, 40,   9, 40,   14, 40,   17, 40,   23, 40,]],
                                ["11","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 22.00, 60.0, [0, 22,  7, 22,   9, 22,   14, 22,   17, 22,   23, 22,]],
                                ["12","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 27.00, 60.0, [0, 27,  7, 27,   9, 27,   14, 27,   17, 27,   23, 27,]],
                                ["13","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 32.00, 60.0, [0, 32,  7, 32,   9, 32,   14, 32,   17, 32,   23, 32,]],
                                ["14","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 37.00, 60.0, [0, 37,  7, 37,   9, 37,   14, 37,   17, 37,   23, 37,]],
                                ["15","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 40.00, 60.0, [0, 40,  7, 40,   9, 40,   14, 40,   17, 40,   23, 40,]]], columns = self.colnames)
        
        
        ## Este es para porn a punto de inicio 20 garods
        self.df = pd.DataFrame([["1","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["2","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["3","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["4","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["5","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["6","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["7","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["8","07/12/2021","11:19",  0.00, 0.00, 0, 225, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["9","07/12/2021","11:19",  0.00, 0.00, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["10","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["11","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["12","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["13","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["14","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                ["15","07/12/2021","11:19", 0.00, 0.00, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]]], columns = self.colnames)
        
        self.dfError = pd.DataFrame([["1","07/12/2021", "11:19",  666, 666, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["2","07/12/2021", "11:19",  666, 666, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["3","07/12/2021", "11:19",  666, 666, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["4","07/12/2021", "11:19",  666, 666, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["5","07/12/2021", "11:19",  666, 666, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["6","07/12/2021", "11:19",  666, 666, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["7","07/12/2021", "11:19",  666, 666, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["8","07/12/2021", "11:19",  666, 666, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["9","07/12/2021", "11:19",  666, 666, 0, 255, "Const", "PID",  20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["10","07/12/2021","11:19",  666, 666, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["11","07/12/2021","11:19",  666, 666, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["12","07/12/2021","11:19",  666, 666, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["13","07/12/2021","11:19",  666, 666, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["14","07/12/2021","11:19",  666, 666, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]],
                                     ["15","07/12/2021","11:19",  666, 666, 0, 255, "Const", "PID", 20.00, 0.0, [0, 20,   7, 20,   9, 20,   14, 20,   17, 20,   23, 20,]]], columns = self.colnames)"""