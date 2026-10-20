void setup() {
  Serial.begin(9600);      // Inicia la comunicación serial
  pinMode(A0, INPUT);      // Configura A0 como entrada
}

void loop() {
  if (Serial.available() > 0) {         // Verifica si hay datos disponibles en el puerto serial
    char input = Serial.read();         // Lee el carácter enviado

    if (input == '1') {                 // Si el carácter es '1'
      int valorADC = analogRead(A0);    // Lee el valor analógico (0 - 1023)
      float voltaje = valorADC * (5.0 / 1023.0);  // Convierte a voltaje (0 - 5V)
      
      Serial.print("Voltaje en A0: ");
      Serial.print(voltaje, 3);         // Muestra el voltaje con 3 decimales
      Serial.println(" V");
    }
  }
}
