
/*
LECTURA DE DOS POTENCIOMETROS
Este programa realiza la lectura de la posición
de dos potenciómetros (uno lineal y uno
logarítmico por medio de dos de los canales
analógicos disponibles en Arduino Uno
*/

// Pines de entrada
int inputPot1 = A0; // Pin de lectura Potenciometro 1 - Lineal
//int inputPot2 = A1; // Pin de lectura Potenciometro 2 - Logaritmico
// Variables
int valuePot1 = 0; // Almacena posicion Potenciometro 1
int valueR1 = 0; // Almacena posicion Potenciometro 2
int valueR2 = 0; // Almacena posicion Potenciometro 2
int valueR3 = 0; // Almacena posicion Potenciometro 2

void setup(){
Serial.begin(9600); // Configura comunicacion serial a 9600 Baudios
}

void loop(){

// Lectura analogica y conversión a digital
valuePot1 = analogRead(inputPot1); // Lee Potenciometro 1


// Envio de datos por puerto serie

Serial.print(": ");
Serial.print(valuePot1);// Envia posicion de Pot1
delay(1500);
Serial.print("\t Rotatorio: ");
Serial.println(valuePot2); // Envia posicion de Pot2
delay(1500);
}
