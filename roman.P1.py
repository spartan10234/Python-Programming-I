"""
Program: CS 115 Project 1
Author: Eduardo Roman
Description: Using input from the user, this program will calculate the (WCT) of a location using
temperature (T) and wind velocity (V). Also if the number of locations, decimal_precision, air temperature, and
velocity exceed their boundaries an error message appears and tells the user what they did wrong and closes the program.
reference for highest and lowest temperature: http://coolcosmos.ipac.caltech.edu
reference for speed of sound: GOOGLE search
"""
import sys
def main():
    print('==> Windchill Temperature (WTC) Weather Report Calculator <==')
    num_locations= int(input('Select the number of locations for the report: '))
    if num_locations<=0:
        print('Error:',num_locations, 'is not a valid input.')
        sys.exit(-1)
    decimal_precision = int(input('Select the decimal precision for the report [1--4]: '))
    if decimal_precision >4 or decimal_precision<=0:
        print('Error:', decimal_precision,'is not in the range 1--4.')
        sys.exit(-1)
    total=0
    a_total= 0
    w_total= 0
    highest_temp= 200
    lowest_temp= 200
    highest_w_vel= 0


    for i in range (1, num_locations+1):
        location_name= input('Enter name of ** Location '+ str(i) +' **:')
        temp_int = int(input('\tEnter air temperature [in deg F]: '))
        if temp_int > 136:
            print('Sorry that temperature is to high for the highest recorded temperature on Earth.')
            print('Try a lower temperature!')
            sys.exit(-1)

        if temp_int < -126:
            print('Sorry that temperature is to low for the lowest recorded temperature on Earth.')
            print('Try a higher temperature!')
            sys.exit(-1)

        vel_int= int(input('\tEnter wind velocity [in mph]: '))
        if vel_int<0:
            print('Error: there is no such thing as negative wind velocity, try a positive integer.')
        if vel_int> 761:
            print('That wind velocity is higher than (761 mph) the speed of sound!')
            print('Try a more realistic number!')
            sys.exit(-1)
        a_total += temp_int
        w_total+= vel_int
        wtc_equ = 35.74 + 0.6215 * temp_int - 35.75 * (vel_int ** 0.16) + 0.4275 * temp_int * (vel_int ** 0.16)
        final_precision= round(wtc_equ, decimal_precision)
        total += final_precision
        if final_precision<highest_temp:
            new_location=location_name
            highest_temp=final_precision
        if temp_int<lowest_temp:
            a_new_location=location_name
            lowest_temp=float(temp_int)
        if vel_int>highest_w_vel:
            b_new_location= location_name
            highest_w_vel= float(vel_int)
        print('WCT is', final_precision,'deg F.')
    print()
    print('***Summary***')

    print('WTC')
    avg_wtc= round(total/num_locations, decimal_precision)
    print('\tAvg recorded WCT:', avg_wtc,'deg F')
    print('\tLocation with lowest WTC:', new_location, '('+str(highest_temp)+' F)')

    print('Air Temperature')
    avg_temp= round(a_total/num_locations,decimal_precision)
    print('\tAVG Recorded air temperature:', avg_temp,'deg F')
    print('\tLocation with lowest air temperature:',a_new_location, '('+str(lowest_temp)+' F)')

    print('Wind Velocities')
    avg_w_temp= round(w_total/num_locations, decimal_precision)
    print('\tAVG recorded wind velocity:', avg_w_temp,'mph')
    print('\tLocation with highest wind velocity:',b_new_location, '('+str(highest_w_vel)+' mph)')









main()