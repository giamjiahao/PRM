#ifndef PRM_ARDUINO_H
#define PRM_ARDUINO_H

#include <Wire.h>

String task_select(String input)
{
  if(input=="h\n")
  {
    digitalWrite(13, HIGH);
    Serial.print("voltage high");
  }
  
  else if(input=="l\n")
  {
    digitalWrite(13, LOW);
    Serial.print("voltage low");
  }
  
  else
  {
    Serial.print("Not accepted commands");
  }
}

#endif
