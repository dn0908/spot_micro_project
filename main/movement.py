#-------------------------------------
#          <front>
# (0 1 2)          (9 10 11)
# 
#
# (6 7 8)          (3 4 5)
#          <hind>
# motor configuration 
#-------------------------------------

# forward movement
class movement:
  def move_forward(self):

    servo0.angle = 55
    servo1.angle = 70
    servo2.angle = 70  
  
    servo3.angle = 55
    servo4.angle = 70
    servo5.angle = 70 

    servo1.angle = 90
    servo2.angle = 90 

    servo6.angle = 55
    servo7.angle = 70
    servo8.angle = 70  
    
    servo4.angle = 90
    servo5.angle = 90 
    
    servo9.angle = 55
    servo10.angle = 70
    servo11.angle = 70   

    servo7.angle = 90
    servo8.angle = 90  
    
    servo10.angle = 90
    servo11.angle = 90  
      
    time.sleep(10)
      
  
  def return_initial(self):
    servo0.angle = 90
    servo1.angle = 90
    servo2.angle = 90
    servo3.angle = 90
    servo4.angle = 90
    servo5.angle = 90
    servo6.angle = 90
    servo7.angle = 90
    servo8.angle = 90
    servo9.angle = 90
    servo10.angle = 90
    servo11.angle = 90
    print("spotty return to initial state!")  

  def sit(self):
    