import cadquery as cq
import math

def angle(
        length:float, 
        height:float
    ) -> float:
    '''
    Finds the hypotenuse of a right triangle
    Presumed length and height are part of a right triangle
    '''
    hyp = math.hypot(length, height)
    angle = length/hyp
    angle_radians = math.acos((angle))
    angle_deg = math.degrees(angle_radians)
    return angle_deg