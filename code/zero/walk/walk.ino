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

#define MA_POSITION 511
#define MB_POSITION 449
#define MC_POSITION 513

Dynamixel Dxl(DXL_BUS_SERIAL1);
int position1=0;
int position2=0;
int position3=0;

void setup() {
  
  // Dynamixel 2.0 Baudrate -> 0: 9600, 1: 57600, 2: 115200, 3: 1Mbps 
  Dxl.begin(3);
  Dxl.jointMode(1); //jointMode() is to use position mode
  Dxl.jointMode(2); //jointMode() is to use position mode
  Dxl.jointMode(3); //jointMode() is to use position mode
}

void loop() {  
  //Turn dynamixel ID 1 to position 0  
  //Dxl.writeWord(ID_NUM, GOAL_POSITION, 0); //Compatible with all dynamixel serise
  // Wait for 1 second (1000 milliseconds)

  position1=Dxl.readWord(1, GOAL_POSITION); //Compatible with all dynamixel serise
  position2=Dxl.readWord(2, GOAL_POSITION); //Compatible with all dynamixel serise
  position3=Dxl.readWord(3, GOAL_POSITION); //Compatible with all dynamixel serise
  SerialUSB.println("SERVO 1:");//SerialUSB.print("\r\n");  
  SerialUSB.println(position1);//SerialUSB.print("\r\n");  
  SerialUSB.println("SERVO 2:");//SerialUSB.print("\r\n");  
  SerialUSB.println(position2);//SerialUSB.print("\r\n");  
  SerialUSB.println("SERVO 3:");//SerialUSB.print("\r\n");  
  SerialUSB.println(position3);//SerialUSB.print("\r\n");  
  //Dxl.writeWord(1, GOAL_POSITION, MA); //Compatible with all dynamixel serise
//  Dxl.writeWord(2, GOAL_POSITION, MB); //Compatible with all dynamixel serise
//  Dxl.writeWord(3, GOAL_POSITION, MC); //Compatible with all dynamixel serise
  delay(500);
}


