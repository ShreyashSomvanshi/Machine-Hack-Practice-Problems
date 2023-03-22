'''
Consider a cylinder of radius as R and height as H. Calculate the cylinder's volume, surface area, 
and lateral surface area in a list in the form of a list as [surface area, volume, lateral surface area].
Assume the value of pi as 3.14.
The formula for the surface area of a cylinder: 2πr² + 2πrh
The formula for the volume of a cylinder: πr²h
The formula for the lateral surface area of a cylinder: 2πrh

Example 1:
Input:
R = 2
H = 2
Output: [50.24, 25.12, 25.12]

Example 2:
Input:
R = 10
H = 10
Output: [1256.0, 3140.0, 628.0]
'''

# Solution:

def cylinder(R,H):
  # A cylinder's volume is π r² h, and its surface area is 2π r h + 2π r²
  # perimeter = 2 * π * r
  # lateral surface = perimeter * height

  volume = 3.14*R*R*H
  Surf_Area = (2*3.14*R*H) + (2*3.14*R*R)
  perim = 2*3.14*R
  lateral_surf_area = perim * H
  
  return [Surf_Area, volume, lateral_surf_area]
  
print(cylinder(R,H))
