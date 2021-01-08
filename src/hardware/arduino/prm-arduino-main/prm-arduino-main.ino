// Author: Zhaoyuan "Maxwell" Cui
// Physics department, University of Arizona
// This is the central part of the arduino firmware

#include <Wire.h>
#include "prm-arduino.h"

bool connection=false;

String inputString = "";
bool stringComplete = false;

void setup()
{
  //Set Digital Pin 13 as output
  pinMode(13, OUTPUT);  
  
  // Open Serial communication
  Serial.begin(9600);
  delay(100);
  if(Serial.availableForWrite()>0)
  {
    // Send ready string out
    Serial.write("Device Ready..."); // Device Ready
    // Reserve 200 bytes for the inputString
    inputString.reserve(200);
    
  }
}

void loop()
{
  // Alwasy linsten to the serial input
  serialEvent();
  // If the string is complete the proceed
  if (stringComplete)
  {
    //Serial.write("test\n");
    task_select(inputString);
    //Serial.print(inputString);
    // clear the string:

    // Reset the string for the next operations
    inputString = "";
    stringComplete = false;
  }
}

// This function is to read the input string, no need to change.
void serialEvent() 
{
  while (Serial.available()) 
  {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') 
    {
      stringComplete = true;
    }
  }
}
