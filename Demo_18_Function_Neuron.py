from pyrosim import PYROSIM
import math


ARM_LENGTH = 0.5

ARM_RADIUS = ARM_LENGTH / 10.0

sim = PYROSIM(playPaused = True , evalTime = 1000, dt=.05)

sim.Send_Cylinder(objectID = 0 , x=0, y=0, z=ARM_LENGTH/2.0 + ARM_RADIUS, r1=0, r2=0, r3=1, length=ARM_LENGTH, radius=ARM_RADIUS)

sim.Send_Cylinder(objectID = 1 , x=0, y=ARM_LENGTH/2.0, z=ARM_LENGTH + ARM_RADIUS, r1=0, r2=1, r3=0, length=ARM_LENGTH, radius=ARM_RADIUS)

sim.Send_Joint(jointID = 0, firstObjectID=0, secondObjectID=1, x=0, y=0, z=ARM_LENGTH + ARM_RADIUS, n1=1, n2=0, n3=0, lo=-3.14159/4.0, hi=+3.14159/4.0)

sim.Send_Function_Neuron(neuronID=0, function=math.sin)

sim.Send_Motor_Neuron(neuronID=1 , jointID=0 )

sim.Send_Synapse(sourceNeuronID = 0 , targetNeuronID = 1 , weight = 1.0 )

sim.Start()

#print sim.pipe.communicate()[0]
# sim.Collect_Sensor_Data()
