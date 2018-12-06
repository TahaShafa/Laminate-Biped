#include <string.h>

//#include <OpenCM904.h>
//#include <DynamixelSDK.h>

/* Dynamixel Basic Position Control Example
 
 Turns left the dynamixel , then turn right for one second,
 repeatedly.
 
                   Compatibility
 CM900                  O
 OpenCM9.04             O
 
                  Dynamixel Compatibility
               AX    MX      RX    XL-320    Pro
 CM900          O      O      O        O      X
 OpenCM9.04     O      O      O        O      X
 **** OpenCM 485 EXP board is needed to use 4 pin Dynamixel and Pro Series ****
 
 created 16 Nov 2012
 by ROBOTIS CO,.LTD.
 */
/* Serial device defines for dxl bus */
#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04
#define DXL_BUS_SERIAL2 2  //Dynamixel on Serial2(USART2)  <-LN101,BT210
#define DXL_BUS_SERIAL3 3  //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
/* Dynamixel ID defines */
#define ID_NUM 1
/* Control table defines */
#define GOAL_POSITION 30

#define MA 511
#define MB 500
#define MC 575
#define MD 512
#define ME 507
#define MF 500

#define RANGE 30
#define DELAY 1000

Dynamixel Dxl(DXL_BUS_SERIAL1);


int m=0;
int ii=0;
int jj=0;
char inputbuffer[100]="";
int value=0;
int values[18];

void setup() {
  
  // Dynamixel 2.0 Baudrate -> 0: 9600, 1: 57600, 2: 115200, 3: 1Mbps 
  Dxl.begin(3);
  Dxl.jointMode(1); //jointMode() is to use position mode
  Dxl.jointMode(2); //jointMode() is to use position mode
  Dxl.jointMode(3); //jointMode() is to use position mode
  Dxl.writeWord(1, GOAL_POSITION, MA); //Compatible with all dynamixel serise
  Dxl.writeWord(2, GOAL_POSITION, MB); //Compatible with all dynamixel serise
  Dxl.writeWord(3, GOAL_POSITION, MC); //Compatible with all dynamixel serise
  Dxl.writeWord(4, GOAL_POSITION, MD); //Compatible with all dynamixel serise
  Dxl.writeWord(5, GOAL_POSITION, ME); //Compatible with all dynamixel serise
  Dxl.writeWord(6, GOAL_POSITION, MF); //Compatible with all dynamixel serise
}

void loop() {
  m = SerialUSB.available();
  while(m){
    SerialUSB.read(inputbuffer+ii,1);
    if(inputbuffer[ii]==','){
      values[jj] = atoi(inputbuffer);
      memset(inputbuffer,0,100);
      ii=0;
      jj++;
      break;
    }
    else if(inputbuffer[ii]=='\r'){
      values[jj] = atoi(inputbuffer);
      memset(inputbuffer,0,100);
      ii=0;
      jj=0;
      break;
    }
    else{
      ii++;
      m = SerialUSB.available();
    }
  }
  //SerialUSB.print("input:\r\n");
//  SerialUSB.print(inputbuffer);
//  SerialUSB.print("\r\n");
//    for(int kk=0;kk<10;kk++){
//    SerialUSB.print(values[kk]);
//    SerialUSB.print(",");
//  }
//  SerialUSB.print("\r\n");
  //  SerialUSB.println(value);
  Dxl.writeWord(1, GOAL_POSITION, MA+values[0]+66); //Compatible with all dynamixel serise
  Dxl.writeWord(2, GOAL_POSITION, MB+values[1]-68); //Compatible with all dynamixel serise
  Dxl.writeWord(3, GOAL_POSITION, MC+values[2]+140); //Compatible with all dynamixel serise
  Dxl.writeWord(4, GOAL_POSITION, MD+values[3]-78); //Compatible with all dynamixel serise
  Dxl.writeWord(5, GOAL_POSITION, ME+values[4]+0); //Compatible with all dynamixel serise
  Dxl.writeWord(6, GOAL_POSITION, MF+values[5]-222); //Compatible with all dynamixel serise
//  delay(10);

}


