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

#define RANGE 30
#define DELAY 1000

Dynamixel Dxl(DXL_BUS_SERIAL1);

void setup() {
  
  // Dynamixel 2.0 Baudrate -> 0: 9600, 1: 57600, 2: 115200, 3: 1Mbps 
  Dxl.begin(3);
  Dxl.jointMode(1); //jointMode() is to use position mode
  Dxl.jointMode(2); //jointMode() is to use position mode
  Dxl.jointMode(3); //jointMode() is to use position mode
  Dxl.writeWord(1, GOAL_POSITION, MA); //Compatible with all dynamixel serise
  Dxl.writeWord(2, GOAL_POSITION, MB); //Compatible with all dynamixel serise
  Dxl.writeWord(3, GOAL_POSITION, MC); //Compatible with all dynamixel serise
}

void loop() {  
//  Dxl.writeWord(3, GOAL_POSITION, MC+RANGE); //Compatible with all dynamixel serise
//  Dxl.writeWord(3, GOAL_POSITION, MC-RANGE); //Compatible with all dynamixel serise
  Dxl.writeWord(1, GOAL_POSITION, MA-RANGE); //Compatible with all dynamixel serise
  delay(DELAY);
  Dxl.writeWord(2, GOAL_POSITION, MB-RANGE); //Compatible with all dynamixel serise
  delay(DELAY);
  Dxl.writeWord(3, GOAL_POSITION, MC+RANGE); //Compatible with all dynamixel serise
  delay(DELAY);
  Dxl.writeWord(1, GOAL_POSITION, MA+RANGE); //Compatible with all dynamixel serise
  delay(DELAY);
  Dxl.writeWord(2, GOAL_POSITION, MB+RANGE); //Compatible with all dynamixel serise
  delay(DELAY);
  Dxl.writeWord(3, GOAL_POSITION, MC-RANGE); //Compatible with all dynamixel serise
  delay(DELAY);
}


