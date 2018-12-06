/* Minimum_Source*/
#include <string.h>

int m=0;
int ii=0;
int jj=0;
char inputbuffer[100]="";
int value=0;
int values[10];

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  m = SerialUSB.available();
  if(m){
    SerialUSB.read(inputbuffer+ii,1);
    if(inputbuffer[ii]==','){
      values[jj] = atoi(inputbuffer);
      memset(inputbuffer,0,100);
      ii=0;
      jj++;
    }
    else if(inputbuffer[ii]=='\n'){
      values[jj] = atoi(inputbuffer);
      memset(inputbuffer,0,100);
      ii=0;
      jj=0;
    }
    else{
      ii++;
    }
  }
  SerialUSB.println("input:");
  SerialUSB.println(inputbuffer);
  for(int kk=0;kk<10;kk++){
    SerialUSB.print(values[kk]);
    SerialUSB.print(",");
  }
  SerialUSB.print("\n");
  //  SerialUSB.println(value);
  delay(1000);

}


