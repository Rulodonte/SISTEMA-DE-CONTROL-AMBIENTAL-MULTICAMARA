#include <Ticker.h>
#include <Wire.h>
#include <ThreeWire.h> 

#include "DHT.h"                        /// LIBRERIAS PARA DHT22 
#include <RtcDS1302.h>                  ///  LIBRERIAS PARA RTC  
#include <Adafruit_PWMServoDriver.h>    ///  LIBRERIAS PARA SERVO   
#include <Separador.h>                  ///  LIBRERIAS PARA SEPARADOR POR COMAS

///////////   VARAIABLES PARA CADA LIBRERIA   ///////
/////////////////////////////////////////////////////

///////////////         DHT22       ////////////////

// Definimos el tipo de sensor  //

#define DHTTYPE DHT22      // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

//Variables definidas para los sensores de humedad y temperatura (DHT22)
// Definimos el nombre y direccion en el Arduimo MEGA

#define DHTPIN30 30  
#define DHTPIN31 31  
#define DHTPIN32 32  
#define DHTPIN33 33 
#define DHTPIN34 34 
#define DHTPIN35 35 
#define DHTPIN36 36 
#define DHTPIN37 37 
#define DHTPIN38 38 
#define DHTPIN39 39
#define DHTPIN40 40 
#define DHTPIN41 41 
#define DHTPIN42 42 
#define DHTPIN43 43 
#define DHTPIN44 44

#define HUMIFICAOR01 46
#define HUMIFICAOR02 47
#define HUMIFICAOR03 48
#define HUMIFICAOR04 49
#define HUMIFICAOR05 8
#define HUMIFICAOR06 9
#define HUMIFICAOR07 10
#define HUMIFICAOR08 11 
#define HUMIFICAOR09 22
#define HUMIFICAOR10 23
#define HUMIFICAOR11 24 
#define HUMIFICAOR12 25
#define HUMIFICAOR13 26
#define HUMIFICAOR14 27
#define HUMIFICAOR15 28

#define TODOENCERO 13

#define COMPRESOR 50

//////  RTC   /////
#define countof(a) (sizeof(a) / sizeof(a[0]))

///////////   INICIALIZACIONES PARA CADA LIBRERIA   ///////
//////////////////////////////////////////////////////////

//////  DHT22   /////

// Aqui estamos inicializando cada una de las variables 
// con su respectivo pin en arduino y el tipo de sensor

DHT dht1(DHTPIN30, DHTTYPE);
DHT dht2(DHTPIN31, DHTTYPE);
DHT dht3(DHTPIN32, DHTTYPE);
DHT dht4(DHTPIN33, DHTTYPE);
DHT dht5(DHTPIN34, DHTTYPE);
DHT dht6(DHTPIN35, DHTTYPE);
DHT dht7(DHTPIN36, DHTTYPE);
DHT dht8(DHTPIN37, DHTTYPE);
DHT dht9(DHTPIN38, DHTTYPE);
DHT dht10(DHTPIN39, DHTTYPE);
DHT dht11(DHTPIN40, DHTTYPE);
DHT dht12(DHTPIN41, DHTTYPE);
DHT dht13(DHTPIN42, DHTTYPE);
DHT dht14(DHTPIN43, DHTTYPE);
DHT dht15(DHTPIN44, DHTTYPE);

//////  RTC   /////
ThreeWire myWire(4,5,2); // IO, SCLK, CE
RtcDS1302<ThreeWire> Rtc(myWire);

Separador s;   //// Estamos haciendo una instancia

////////////////  VARIABLES GENERALES   ///////////

/// El el arreglo DatosSerialString[47] recive los datos que envia el software de control
/// los datos estan compuestos por 47 datos. Los primeros 45 corresponden al numeros de 
///camara (1-15), Nivel de calefaccion (0-255), ON/OFF de humificadores (0/1 respectivamente)
/// el 46 coresponde al DIMMER especial que se considero para el control de los extractores 
///(el cual no funciono) y el 47 controla el inicio y apagado del compresor del A/C todos estan
///separados por una coma (,).
/// EJEMPLO: 1,255,0,2,255,0,3,255,0,4,255,0,5,255,0,6,255,0,7,255,0,8,255,0,9,255,0,10,255,0,11,255,0,12,255,0,13,255,0,14,255,0,15,255,0,255,0
String DatosSerialString[47]; 

/// El arreglo DatosSerialInt[47] tambien conttiene 47 espacios, en esto se guardan los datos ya transformados a una
/// veriable INT, esto conla finalidad de que pueda ser usada para el control de los equipos.
/// Aqui si se ocupa el cero, empezamos como 0 osea que son del 0 al 46 espacios.
int DatosSerialInt[47]; 

/// La matriz  DataFrameSerialInt[15][3] guarda los datos de las 15 camras (Numero de camara, Nivel del dimmer y estado del humificador)
/// [0][0] = Numero de camara
/// [0][1] = Nivek de dimmer
/// [0][2] = Estado del humificador (ON/OFF, 0/1 respectivamente)
int DataFrameSerialInt[16][3];  

/// La matriz DataFrameSensores[16][12] guarda los datos de los 15 sensores (DHT22)
/// columna 0 = Temeratura y columna 1 =  Humedad
/// los datos empeizan en la fila 1 y terminan en la 16
float DataFrameSensores[16][12]; /// la localidad 0 no se ocupa, por eso los ciclos for empiezan en 1

int EstadoCompresor = 0;   
int Contador = 0;

void setup() 
  {
    Serial.begin(9600);

    pinMode(HUMIFICAOR01, OUTPUT);
    pinMode(HUMIFICAOR02, OUTPUT);
    pinMode(HUMIFICAOR03, OUTPUT);
    pinMode(HUMIFICAOR04, OUTPUT);
    pinMode(HUMIFICAOR05, OUTPUT);
    pinMode(HUMIFICAOR06, OUTPUT);
    pinMode(HUMIFICAOR07, OUTPUT);
    pinMode(HUMIFICAOR08, OUTPUT);
    pinMode(HUMIFICAOR09, OUTPUT);
    pinMode(HUMIFICAOR10, OUTPUT);
    pinMode(HUMIFICAOR11, OUTPUT);
    pinMode(HUMIFICAOR12, OUTPUT);
    pinMode(HUMIFICAOR13, OUTPUT);
    pinMode(HUMIFICAOR14, OUTPUT);
    pinMode(HUMIFICAOR15, OUTPUT);

    pinMode(TODOENCERO, OUTPUT);

    pinMode(COMPRESOR, OUTPUT);
  
    dht1.begin();
    dht2.begin();
    dht3.begin();
    dht4.begin();
    dht5.begin();
    dht6.begin();
    dht7.begin();
    dht8.begin();
    dht9.begin();
    dht10.begin();
    dht11.begin();
    dht12.begin();
    dht13.begin();
    dht14.begin();
    dht15.begin();

    Rtc.Begin();

    Wire.begin(); // join i2c bus (address optional for master)

    for (int i = 0; i <= 15; i++) 
                    {
                      DataFrameSerialInt[i][0] = i+1;
                      DataFrameSerialInt[i][1] = 0;
                      DataFrameSerialInt[i][2] = 0;                      
                    }

 
               digitalWrite(HUMIFICAOR01, HIGH);
               digitalWrite(HUMIFICAOR02, HIGH);
               digitalWrite(HUMIFICAOR03, HIGH);
               digitalWrite(HUMIFICAOR04, HIGH);
               digitalWrite(HUMIFICAOR05, HIGH);
               digitalWrite(HUMIFICAOR06, HIGH);
               digitalWrite(HUMIFICAOR07, HIGH);
               digitalWrite(HUMIFICAOR08, HIGH);
               digitalWrite(HUMIFICAOR09, HIGH);
               digitalWrite(HUMIFICAOR10, HIGH);
               digitalWrite(HUMIFICAOR11, HIGH);
               digitalWrite(HUMIFICAOR12, HIGH);
               digitalWrite(HUMIFICAOR13, HIGH);
               digitalWrite(HUMIFICAOR14, HIGH);
               digitalWrite(HUMIFICAOR15, HIGH);

               digitalWrite(COMPRESOR, HIGH);
               digitalWrite(TODOENCERO, HIGH);

               for (int i = 0; i <= 14; i++) 
                  {
                    Calefaccion(DataFrameSerialInt[i][0],DataFrameSerialInt[i][1]);
                  }
                               
               //Serial.println("TODO APAGADO"); 
 
  }   /////////  Fin void setup


void loop() 
  {
    //// Este "if" se ejecuta si llega informacion al puerto serial
    if (Serial.available()) 
      {
        String StringVariableTemporal;
        int IntVariableTemporal;
        String incomingString = Serial.readString();

        
        /// Este ciclo "for" extrae los datos separados por coma (,) de la variable incomingString
        /// usando la funcion s.separa y los mete en el arreglo DatosSerialInt[47]
        for (int i = 0; i <= 46; i++)
          {
              DatosSerialString[i] = s.separa(incomingString, ',', i);
              StringVariableTemporal = DatosSerialString[i];
              IntVariableTemporal = StringVariableTemporal.toInt();
              DatosSerialInt[i] = IntVariableTemporal;
          }

        /// En este ciclo se toman los datos de DatosSerialInt[47] y se acomodan en la matriz DataFrameSerialInt[j][k]
        /// [0][0] = Numero de camara
        /// [0][1] = Nivek de dimmer
        /// [0][2] = Estado del humificador (ON/OFF, 0/1 respectivamente)
        int k = 0;
        int j = 0;
        
        for (int i = 0; i <= 44; i++) /// Aqui el conteo es hasta 44, porque solo estamos extrayendo el hasta el dato 45 (0-45).
          {              
            if (k <= 2)
              {                
                DataFrameSerialInt[j][k] =  DatosSerialInt[i]; 
                
                if (k == 2)
                   {
                      k = 0;
                      j = j + 1;                     
                   }
                else
                  {
                     k = k + 1;
                  }
               }
            }
      
       /// Este ciclo "for" toma las lecturas de todos los sensores DHT22
       /// pero las toma desde la fial 1 del arreglo, columna 0 = a temepratura y columna 1 igual a humedad
       /// los datos se guardan en el DataFrameSensores[i][j]    
       for (int i = 1; i <= 15; i++) 
          {
            DataFrameSensores[i][0] = Sensores(i,0);
            DataFrameSensores[i][1] = Sensores(i,1);
          }                
       
       /// Este ciclo "for" extrae y ordena los datos de los sensores (DHT22) para ser enviados a travez
       /// del puerto COM (Serial) seleccionado.
       for (int i = 1; i <= 15; i++) 
          {
            
            for (int j = 0; j <= 1; j++)
              { 
                
                Serial.print(DataFrameSensores[i][j]);
                if (j < 1)
                  {
                    Serial.print(",");
                  }
              }
               if (i <= 14)
                  {
                    Serial.print(";");
                  }
           }                                                                       
       
       /// Este ciclo envia los datos numero de camara y nivel del dimmer (0-255)
       /// a la funcion de Calefaccion
       for (int i = 0; i <= 14; i++) 
          {
            Calefaccion(DataFrameSerialInt[i][0],DataFrameSerialInt[i][1]);
           }
       
       /// Esta lina de codigo envia el 16 a la fuancion de calefaccion como el canal a controla del dimmer
       /// y extraemos es valor de dimmer que esta en la posicion 45 pero que
       /// corresponde al dato 46 de lo sdatos enviados por el software de control
       Calefaccion(16, DatosSerialInt[45]);  

       /// Esta linea de codigo establece el estado del compresion en la variable EstadoCompresor
       /// esta variable se encuentra en la posicion 47 de los datos enviados por el software
       /// control
       EstadoCompresor = DatosSerialInt[46];
       
      /////////////////////////////////////////////////////////////////////////////////////////////
      ///////////////////  Esta seccion se realiza el control del copresor del A/C   //////////////
      /////////////////////////////////////////////////////////////////////////////////////////////

       if (EstadoCompresor == 1)
         {
            digitalWrite(COMPRESOR, LOW);
         }

        if (EstadoCompresor == 0)
         {
            digitalWrite(COMPRESOR, HIGH);
         }
               

      /////////////////////////////////////////////////////////////////////////////////////////////
      ///////////////////  Esta seccion se realiza el control de los humificadores   /////////////
      /////////////////////////////////////////////////////////////////////////////////////////////
     
       if (DataFrameSerialInt[0][2] == 1)
         {
            digitalWrite(HUMIFICAOR01, LOW);
         }

       if (DataFrameSerialInt[0][2] == 0)
         {
            digitalWrite(HUMIFICAOR01, HIGH);
         }

       /////////////////////////////////////////////////////////////////////////////
       if (DataFrameSerialInt[1][2] == 1)
         {
            digitalWrite(HUMIFICAOR02, LOW);
         }

       if (DataFrameSerialInt[1][2] == 0)
         {
            digitalWrite(HUMIFICAOR02, HIGH);
         }

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[2][2] == 1)
         {
            digitalWrite(HUMIFICAOR03, LOW);
         }

       if (DataFrameSerialInt[2][2] == 0)
         {
            digitalWrite(HUMIFICAOR03, HIGH);
         }

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[3][2] == 1)
         {
            digitalWrite(HUMIFICAOR04, LOW);
         }

       if (DataFrameSerialInt[3][2] == 0)
         {
            digitalWrite(HUMIFICAOR04, HIGH);
         }        

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[4][2] == 1)
         {
            digitalWrite(HUMIFICAOR05, LOW);
         }

       if (DataFrameSerialInt[4][2] == 0)
         {
            digitalWrite(HUMIFICAOR05, HIGH);
         }       

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[5][2] == 1)
         {
            digitalWrite(HUMIFICAOR06, LOW);
         }

       if (DataFrameSerialInt[5][2] == 0)
         {
            digitalWrite(HUMIFICAOR06, HIGH);
         }       

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[6][2] == 1)
         {
            digitalWrite(HUMIFICAOR07, LOW);
         }

       if (DataFrameSerialInt[6][2] == 0)
         {
            digitalWrite(HUMIFICAOR07, HIGH);
         }

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[7][2] == 1)
         {
            digitalWrite(HUMIFICAOR08, LOW);
         }

       if (DataFrameSerialInt[7][2] == 0)
         {
            digitalWrite(HUMIFICAOR08, HIGH);
         } 

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[8][2] == 1)
         {
            digitalWrite(HUMIFICAOR09, LOW);
         }

       if (DataFrameSerialInt[8][2] == 0)
         {
            digitalWrite(HUMIFICAOR09, HIGH);
         } 

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[9][2] == 1)
         {
            digitalWrite(HUMIFICAOR10, LOW);
         }

       if (DataFrameSerialInt[9][2] == 0)
         {
            digitalWrite(HUMIFICAOR10, HIGH);
         } 

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[10][2] == 1)
         {
            digitalWrite(HUMIFICAOR11, LOW);
         }

       if (DataFrameSerialInt[10][2] == 0)
         {
            digitalWrite(HUMIFICAOR11, HIGH);
         } 

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[11][2] == 1)
         {
            digitalWrite(HUMIFICAOR12, LOW);
         }

       if (DataFrameSerialInt[11][2] == 0)
         {
            digitalWrite(HUMIFICAOR12, HIGH);
         }

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[12][2] == 1)
         {
            digitalWrite(HUMIFICAOR13, LOW);
         }

       if (DataFrameSerialInt[12][2] == 0)
         {
            digitalWrite(HUMIFICAOR13, HIGH);
         }
       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[13][2] == 1)
         {
            digitalWrite(HUMIFICAOR14, LOW);
         }

       if (DataFrameSerialInt[13][2] == 0)
         {
            digitalWrite(HUMIFICAOR14, HIGH);
         }

       /////////////////////////////////////////////////////////////////////////////       
       if (DataFrameSerialInt[14][2] == 1)
         {
            digitalWrite(HUMIFICAOR15, LOW);
         }

       if (DataFrameSerialInt[14][2] == 0)
         {
            digitalWrite(HUMIFICAOR15, HIGH);
         }
        
       digitalWrite(TODOENCERO, LOW);
       Contador = 0;
       
      }///////// fin if aviable puerto serial con datos



 
    //// Este "if" se ejecuta si no llega informacion al puerto serial
    if (Serial.available() == 0)
      {
        Contador = Contador + 1;
                
        if (Contador == 1000)
            {
               
              for (int i = 0; i <= 15; i++) 
                    {
                      DataFrameSerialInt[i][0] = i+1;
                      DataFrameSerialInt[i][1] = 0;
                      DataFrameSerialInt[i][2] = 0;                      
                    }
 
               digitalWrite(HUMIFICAOR01, HIGH);
               digitalWrite(HUMIFICAOR02, HIGH);
               digitalWrite(HUMIFICAOR03, HIGH);
               digitalWrite(HUMIFICAOR04, HIGH);
               digitalWrite(HUMIFICAOR05, HIGH);
               digitalWrite(HUMIFICAOR06, HIGH);
               digitalWrite(HUMIFICAOR07, HIGH);
               digitalWrite(HUMIFICAOR08, HIGH);
               digitalWrite(HUMIFICAOR09, HIGH);
               digitalWrite(HUMIFICAOR10, HIGH);
               digitalWrite(HUMIFICAOR11, HIGH);
               digitalWrite(HUMIFICAOR12, HIGH);
               digitalWrite(HUMIFICAOR13, HIGH);
               digitalWrite(HUMIFICAOR14, HIGH);
               digitalWrite(HUMIFICAOR15, HIGH);

               digitalWrite(COMPRESOR, HIGH);
               digitalWrite(TODOENCERO, HIGH);

               for (int i = 0; i <= 15; i++) 
                  {
                    Calefaccion(DataFrameSerialInt[i][0],DataFrameSerialInt[i][1]);
                  }
                               
               Contador = 0; 
                                          
            }
            
        delay(10);        
      }///////// fin if aviable puerto serial sin datos
 
      
      
  }  //////////// fin void principal


//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////

float Calefaccion (int NumCamara, int ValDimmer)
    {
       byte myPins[2];
      
       myPins[0] = NumCamara ;
       myPins[1] = ValDimmer;
                   
       Wire.beginTransmission(8);       // transmit to device #8
      
       Wire.write(myPins, 2);           // sends one byte
     
       Wire.endTransmission();         // stop transmitting

      
       return myPins[1];     
    }


float Sensores (int NumCamara, int tipo)
    {    
      float DataFrameSensores[16][2] = { 
        { 0,0 },
        { dht1.readTemperature(), dht1.readHumidity() },
        { dht2.readTemperature(), dht2.readHumidity() },
        { dht3.readTemperature(), dht3.readHumidity() },
        { dht4.readTemperature(), dht4.readHumidity() },
        { dht5.readTemperature(), dht5.readHumidity() },
        { dht6.readTemperature(), dht6.readHumidity() },
        { dht7.readTemperature(), dht7.readHumidity() },
        { dht8.readTemperature(), dht8.readHumidity() },
        { dht9.readTemperature(), dht9.readHumidity() },
        { dht10.readTemperature(), dht10.readHumidity() },
        { dht11.readTemperature(), dht11.readHumidity() },
        { dht12.readTemperature(), dht12.readHumidity() },
        { dht13.readTemperature(), dht13.readHumidity() },
        { dht14.readTemperature(), dht14.readHumidity() },
        { dht15.readTemperature(), dht15.readHumidity() }
          };
    
          
     return  DataFrameSensores[NumCamara][tipo];
     
    }   /////////////////////////////////////////////////////////   fin sensores

/*void printDate(const RtcDateTime& dt)
  {
      char datestring[20];
  
      snprintf_P(datestring, countof(datestring), PSTR("%02u/%02u/%04u"), dt.Month(), dt.Day(), dt.Year());
      Serial.print(datestring);
  }

void printHora(const RtcDateTime& dt)
  {
      char datestring[20];
  
      snprintf_P(datestring, countof(datestring), PSTR("%02u:%02u:%02u"), dt.Hour(), dt.Minute(), dt.Second());
      Serial.print(datestring);
  }*/

  
