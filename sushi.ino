#include "Keyboard.h"
#include "Mouse.h"
char serialData;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Keyboard.begin();
  Keyboard.releaseAll();
}


void loop() {
  pinMode(2,INPUT_PULLUP);

  if (digitalRead(2) == LOW)
  {

      if(Serial.available() > 0)
      {
        
          serialData = Serial.read();
          //Serial.print(serialData);
          delay(1);
          Keyboard.write(serialData);
          Keyboard.releaseAll();
          
      }

  }
  

}
