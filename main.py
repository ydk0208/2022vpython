"""
v = 0
kp = 0.2
target = 100
"""

motors = []
motors.append([0,10,0.2,100])   #v,a,kp,target
motors.append([0,10,0.2,40])

def motorP():
  for motor in motors:
    p = motor[2]*(motor[3]-motor[0])
    if p >= motor[1]:
      motor[0] = motor[0]+motor[1]
    elif p <= -motor[1]:
      motor[0] = motor[0]-motor[1]
    else:
      motor[0] = motor[0]+p

for i in range(20):
  print(motors[0][0],motors[1][0])
  motorP()
  rate(10)
