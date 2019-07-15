#-*-coding:utf-8 -*-
# rocket_rand_game
# 2019.07.11

# The Rule
# 1) Your rocket starts at position 100m above the earth. Initial velocity is 0m/s.
# 2) Gravity pulls you down at acceleration 10m/s^2
# 3) You have 100 liters of fuel
# 4) You have thrusters that can be powered from 0 to 20. 1 thrust = 1 liter of fuel
# 5) Total acceleration = gravity + thrusters (minimum -10, maximum +10)

# Additional requirements:
# 1) Check the input (thrusters). If it is greater than 20 or less than 0, fix it. Thrust cannot be more than the available fuel.
# 2) If fuel is 0, the ship is in free-fall. Do not even ask for input!
# 3) When the lander reaches position 0m or less, the game is over. If the magnitude of final velocity is greater than 3m/s, the rocket has crashed! See my sample output below.
# P = position, V = velocity, F = fuel

position = 100
velocity = 0
gravity = -10
fuel = 100
thruster = 0        # it can be 0~20

#repeat ask
while 1:
    input_temp = input("Set thrusters(0-20): ")

    if (input_temp < 0):
        print("No thruster(0)!")
        thruster = 0
    elif (input_temp >= 20):
        print("Thrusters at max(20)!")
        thruster = 20
    else:
        thruster = input_temp

    #if input_temp > fuel, show the fuel by thruster. And calc the last fuel
    if (input_temp > fuel):
        print ("Out of fuel! Thrusters at {}".format(fuel))

        thruster = fuel
        #add count the val by fuel
        count = fuel
        #set the fuel value to '0'
        fuel = 0

        while 1:
            if(count == 0):
                break
            elif(count == 1):
                #DO NOT USED THE THURSTER VALUE
                #DO NOT CALC THE FUEL

                # calc acceleration
                acceleration = gravity
                # calc position
                position = position + velocity + acceleration * 0.5
                # calc velocity
                velocity = velocity + acceleration
                if velocity >= -3:
                    print("Landing successful!")
                    exit()
                else:
                    print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))
                    print ("Rocket crashed! Velocity was {} m/s".format(velocity))
                    exit()
            elif(count == 4):
                # DO NOT CALC THE FUEL

                # calc acceleration
                acceleration = gravity + thruster
                # calc position
                position = position + velocity + acceleration * 0.5
                # calc velocity
                velocity = velocity + acceleration
                print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))
                print("No fuel -- rockeet is in free-fall!")
                count = count - 1
            else:
                # DO NOT USED THE THURSTER VALUE
                # DO NOT CALC THE FUEL

                # calc acceleration
                acceleration = gravity
                # calc position
                position = position + velocity + acceleration * 0.5
                # calc velocity
                velocity = velocity + acceleration
                print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))
                print("No fuel -- rockeet is in free-fall!")
                count = count - 1

    # calc acceleration
    acceleration = gravity + thruster
    # calc position
    position = position + velocity + acceleration * 0.5
    # calc fuel
    fuel = fuel - thruster
    # calc velocity
    velocity = velocity + acceleration

    if position < 0:
        position = 0
        print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))
        print("Landing successful!")
        exit()
    else:
        print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))