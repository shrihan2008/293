"""my_controlleraqre controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
robot=Robot()
# create the Robot instance.
RPCm=robot.getDevice("RPC")
RPFm=robot.getDevice("RPF")
RMCm=robot.getDevice("RMC")
RMFm=robot.getDevice("RMF")
RACm=robot.getDevice("RAC")
RAFm=robot.getDevice("RAF")


LPCm=robot.getDevice("LPC")
LPFm=robot.getDevice("LPF")
LMCm=robot.getDevice("LMC")
LMFm=robot.getDevice("LMF")
LACm=robot.getDevice("LAC")
LAFm=robot.getDevice("LAF")