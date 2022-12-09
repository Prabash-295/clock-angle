import math
def Clock_Angle(h,m):

        if (h < 0 or m < 0 or h > 24 or m > 60):
            print('Wrong input')
         
        if (h == 12):
            h = 0
        if (m == 60):
            m =0
            h += 1;
        if(h>12):
                   h = h-12;
        
        hour_angle = 0.5 * (h * 60 + m)
        hour_angle=math.ceil(hour_angle)
        minute_angle = 6 * m
        angle = abs(hour_angle - minute_angle)   
        angle = min(360 - angle, angle)
        return angle


a=input("Time:")
if (":" not in a):

    print("Please enter in a valid format")
b=a.split(":")
h,m=int(b[0]),int(b[1])
print('Angle B/W CLock needle: {}°'.format( Clock_Angle(h,m)))