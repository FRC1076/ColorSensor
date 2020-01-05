import wpilib
import ctre



class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        Initializes all motors in the robot.
        """
        
        #Setup colour sensor
        self.colorSensor = wpilib.I2C(wpilib.I2C.Port.kOnboard, 0x52)
        

    def autonomousInit(self):
        pass #Do nothing for now in auton

    def autonomousPeriodic(self):
        print()

    def teleopInit(self):
        targetColor = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        self.timer = 0
 

    def teleopPeriodic(self):
        if self.timer % 50 == 0:
            self.logger.info("Red Value: %f",self.getRed())
        self.timer+=1

    def getRed(self):
        red1 = self.colorSensor.read(0x13, 1)
        return red1


#  main entry point
if __name__ == "__main__":
  wpilib.run(MyRobot)
