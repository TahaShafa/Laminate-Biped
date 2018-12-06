/*SerialUSB_Serial2_Converter
 
 This example is convert from serial2 to USB.
 CM-900, OpenCM9.04 has a port(J9) connected directly to Serial2.
 If some data is coming from Serial2, it is sent to serialUSB.
 On the contrary, all data coming from serialUSB is sent to Serial2.
 
 
 You can connect the below products to J9 Connector in CM-900, OpenCM9.04
 [BT-110A] or [BT-110A Set]
 http://www.robotis-shop-kr.com/goods_detail.php?goodsIdx=875
 [ZIG-110A Set]
 http://www.robotis-shop-kr.com/goods_detail.php?goodsIdx=405
 [LN-101] USART communication and download tool in CM-100
 http://www.robotis-shop-kr.com/goods_detail.php?goodsIdx=348
 
 You can also find all information about ROBOTIS products
 http://support.robotis.com/
 
                   Compatibility
 CM900                  O
 OpenCM9.04             O

 created 16 Nov 2012
 by ROBOTIS CO,.LTD.
 */

#include <string.h>

char inputbuffer[100]="";
char interpbuffer[100]="";
char outputbuffer[100]="";
int value=0;
int ii;
int jj; 
int l; 
int m; 

void setup(){
}

void loop(){
//  if(SerialUSB.available()){
//    SerialUSB.print((char)SerialUSB.read()); //send data coming from Serial2 to USB(PC)
//  }
  m = SerialUSB.available();

  if(m){
    SerialUSB.read(inputbuffer+ii,m);
    for(jj=ii;jj<ii+m;jj++){
      if(inputbuffer[jj]=='\n'){
        value = atoi(inputbuffer);
        //strncpy(interpbuffer,inputbuffer,jj);
        memset(inputbuffer,0,100);
        ii=0;
      }}
    ii+=m;
    }
//  l = strlen(inputbuffer);
//      interpbuffer[ii+1]=0;
//      inputbuffer[0]=0;
//    }
//  }
  
//  m = strlen(interpbuffer);
/*
*/
//  strcpy(outputbuffer,interpbuffer);
  SerialUSB.println("input:");
  SerialUSB.println(inputbuffer);
  SerialUSB.println("value:");
  SerialUSB.println(value);
  delay(1000);
}
