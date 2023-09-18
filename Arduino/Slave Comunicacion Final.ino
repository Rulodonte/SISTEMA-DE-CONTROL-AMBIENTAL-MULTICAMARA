
#include <Wire.h>

#include <GyverDimmer.h>
DimmerBresMulti<17> dim1;   // especificar el número de atenuadores


void setup() 
  {
    Wire.begin(8);                // join i2c bus with address #8
    Wire.onReceive(receiveEvent); // register event
    Serial.begin(9600);           // start serial for output
    
    //pinMode(13, OUTPUT);    // sets the digital pin 13 as output
    
    // crear una interrupción general en el detector cero
    attachInterrupt(0, isr, RISING);  // D2 == 0
    
    
    // conectar pines
   
    dim1.attach(1, 30);    // canal 1, pin 30
    dim1.attach(2, 32);    // canal 2, pin 32
    dim1.attach(3, 34);    // canal 3, pin 35
    dim1.attach(4, 36);    // canal 4, pin 36
    dim1.attach(5, 38);    // canal 5, pin 38
    dim1.attach(6, 40);    // canal 6, pin 40
    dim1.attach(7, 42);    // canal 7, pin 42
    dim1.attach(8, 44);    // canal 8, pin 44
    dim1.attach(9, 3);     // canal 9, pin 3
    dim1.attach(10, 4);    // canal 10, pin 4
    dim1.attach(11, 5);    // canal 11, pin 5
    dim1.attach(12, 6);    // canal 12, pin 6
    dim1.attach(13, 7);    // canal 13, pin 7
    dim1.attach(14, 8);    // canal 14, pin 8
    dim1.attach(15, 9);    // canal 15, pin 9
    dim1.attach(16, 10);    // canal 16, pin 9

    //dim.attach(12, 6);  // canal 12, pin 6*/
   
  }

void isr() 
  {
    dim1.tick(); // activar un tic en la interrupción del detector cero
  }


void loop() 
  {
    
    delay(100);
  }

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) 
  {
    
    int camara = 0;
    int nivel = 0;
   
    // Si hay dos bytes disponibles
    if (Wire.available() == 2)
      {
        // Leemos el primero que será el pin
        camara = Wire.read();
        //Serial.print("Camara ");
        //Serial.print(camara);
      }
    // Si hay un byte disponible
    if (Wire.available() == 1)
      {
        nivel = Wire.read();
        //Serial.print(" Nivel: ");
        //Serial.println(nivel);
      }
   
        // Activamos/desactivamos salida del dimmer
      
        dim1.write(camara, nivel);        // canal 0 (rango 0-255)
        
        delay(100);
    
  }
