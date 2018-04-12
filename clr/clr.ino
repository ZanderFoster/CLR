/* Computer Light Reaction
 * Made By: Zander Foster
 * Date: 04/11/2018 11:00
 * ===========================
 * 
 * Comamnd layout as followed
 * 
 * mode/red/green/blue/delay/
 * 
 * Modes:
 * 0 = fade
 * 
 * RGB:
 * 0-255
 * 
 * Delay:
 * seconds 1,2,3...
 * 
 * ===========================
 */
 

unsigned long serialdata;
int inbyte;

//transistor base pins
const int r = 3; 
const int g = 5;
const int b = 6;


//output rgb values
int rv = 0;
int gv = 0;
int bv = 0;

//input rgb values
int ri = 0;
int gi = 0;
int bi = 0;

//Delay after complete in seconds
int changeDelay = 0;

//Fade Speed
long fadeDelay = 500;

void setup()
{
  Serial.begin(115200);
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(b, OUTPUT);
}

void loop()
{
  getSerial();
  switch(serialdata)
  {
    case 0:
    {
      Serial.print("Fade:Start");

      //get rgb values to change to
      getSerial();
      ri = serialdata;
      getSerial();
      gi = serialdata;
      getSerial();
      bi = serialdata;
      getSerial();
      changeDelay = serialdata * 1000;
      
      while((rv != ri) || (gv != gi) || (bv != bi)){

        //change red value
        if(rv == ri){
          rv = ri;
        }
        else if(rv < ri){
          rv++;
        }
        else{
          rv--;
        }

        //change green value
        if(gv == gi){
          gv = gi;
        }
        else if(gv < gi){
        gv++;
        }
        else{
          gv--;
        }
  
        //change blue value
        if(bv == bi){
          bv = bi;
        }
        else if(bv < bi){
          bv++;
        }
        else{
          bv--;
        }
        
        delayMicroseconds(fadeDelay);
        analogWrite(r, rv);
        analogWrite(g, gv);
        analogWrite(b, bv);
      }

      delay(changeDelay);
      Serial.print("|| Delay: ");
      Serial.print(changeDelay / 1000);
      Serial.print("S || Finished");
      Serial.print("\n");
      break;
   }
  }
}

long getSerial()
{
  serialdata = 0;
  while (inbyte != '/')
  {
    inbyte = Serial.read(); 
    if (inbyte > 0 && inbyte != '/')
    {
     
      serialdata = serialdata * 10 + inbyte - '0';
    }
  }
  inbyte = 0;
  return serialdata;
}

