import math
def garden2():
    print("Calculate Garden requirements\n")
    print("--------------------------------")
    len=float(input("Enter lenght of side of garden (feet):"))
    l=len/4
    s=float(input("Enter spacing between plants (feet):"))
    d_garden=float(input("Enter depth of garden soil (feet):"))
    d_fill=float(input("Enter depth of fill (feet):"))
    each_semi_area=(math.pi*(l**2))/2
    i_each_semi_area=math.trunc(each_semi_area)
    each_semi_plant=each_semi_area/s**2
    i_each_semi_plant=math.trunc(each_semi_plant)
    circle_plant=i_each_semi_plant*2
    total_semi_area=each_semi_area*6
    total_semi_plant=i_each_semi_plant*6
    print(f"Plants for each semicircle garden:{i_each_semi_plant}")
    print(f"Plants for the circlegarden:{circle_plant}")
    print(f"Total:{total_semi_plant}")
    soil_semicircle_garden=(i_each_semi_area*d_garden)/27
    r_soil_semicircle_garden=round(soil_semicircle_garden,1)
    print(f"Soil for  each semicircle garden: {r_soil_semicircle_garden} cubic yards")
    soil_circle_garden=r_soil_semicircle_garden*2
    total_garden_soil=round(r_soil_semicircle_garden*6,1)
    print(f"Soil for the circle garden:{soil_circle_garden} cubic yards")
    print(f"Total soil for the garden: {total_garden_soil} cubic yards")
    except_area=(((len**2)-total_semi_area)*d_fill)/27
    r_except_area=round(except_area,1)
    print(f"Total fill for the  garden:{r_except_area} cubic yards")

garden2()