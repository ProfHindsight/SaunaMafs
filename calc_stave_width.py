import math

def calc_stave_widths():
    with open("stave_widths.txt", "r") as f:
        lines = f.readlines()
        normal = []
        special = []
        selected = "normal"
        for line in lines:
            if "NORMAL" in line:
                selected = "normal"
            elif "SPECIAL" in line:
                selected = "special"
            else:
                if selected == "normal":
                    normal.append(line)
                else:
                    special.append(line)
        
        # Calculate the average width of the normal staves
        normal_widths = [float(x) for x in normal]
        normal_avg = sum(normal_widths) / len(normal_widths)
        
        # Multiply the average width by 44 to get total circumference
        total_circumference = normal_avg * 44
        
        # Add the two special staves
        special_widths = [float(x) for x in special]
        total_circumference += sum(special_widths)
        
        # Print the total circumference
        print(f"Total circumference: {total_circumference}")
        # Print the average width of the normal staves
        print(f"Average width of normal staves: {normal_avg}")
        print(f"Average width of special staves: {sum(special_widths) / len(special_widths)}")
        # Print standard deviation of normal staves
        normal_std = (sum([(x - normal_avg) ** 2 for x in normal_widths]) / len(normal_widths)) ** 0.5
        print(f"Standard deviation of normal staves: {normal_std}")
        return {"special": special_widths, "average": normal_avg}
    
def calc_46_sided_polygon_diameter(board_gap:float=0):
    # Angle of each side of the polygon
    angle = 2*math.pi / 46
    # Using the average width of all staves, use tangent to calculate radius
    radius = (calc_stave_widths()["average"] + board_gap) / (2 * math.tan(angle / 2))
    # Diameter is twice the radius
    diameter = 2 * radius
    print(f"Diameter of 46-sided polygon: {diameter}")

def split_board_length():
    # Board width is 5.160 inches
    # Diameter of circle is 73.875 inches
    # Height of each board is a = sqrt(c^2 - b^2) 
    # where c is the radius of the circle and b is the board width
    # There should be 8 total boards
    a = []
    for i in range(0, 8):
        a.append(2*math.sqrt((73.875/2)**2 - (i*5.125)**2))
        print(f"Board {i + 1} height: {a[i]}")
        
    # A1 - 73 and 7/8
    # B1 - 73.16
    # C1 - 70.97
    # B2 - 67.17
    # A2 - 61.45
    # C2 - 53.21
    # D1 - 40.93
    # C3 - 17.59
    A1 = a[0]
    B1 = a[1]
    C1 = a[2]
    B2 = a[3]
    A2 = a[4]
    C2 = a[5]
    D1 = a[6]
    C3 = a[7]
    
    A1_proportion = A1 / (A1 + A2)
    B1_proportion = B1 / (B1 + B2)
    C1_proportion = C1 / (C1 + C2 + C3)
    D1_proportion = D1 / (D1 + D1 + D1)
    print(f"A1 proportion: {A1_proportion}")
    print(f"B1 proportion: {B1_proportion}")
    print(f"C1 proportion: {C1_proportion}")
    print(f"D1 proportion: {D1_proportion}")
    
    print(f"A sum: {A1 + A2}")
    print(f"B sum: {B1 + B2}")
    print(f"C sum: {C1 + C2 + C3}")
    print(f"D sum: {D1 + D1 + D1}")
    
    BOARD_LENGTH = 144.5
    
    # Multiply proportion by 144 inches to get the length of the board
    print(f"A1   length: {A1_proportion * BOARD_LENGTH}")
    print(f"B1   length: {B1_proportion * BOARD_LENGTH}")
    print(f"C1   length: {C1_proportion * BOARD_LENGTH}")
    print(f"B2   length: {(1 - B1_proportion) * BOARD_LENGTH}")
    print(f"A2   length: {(1 - A1_proportion) * BOARD_LENGTH}")
    print(f"C2&3 length: {(1 - C1_proportion) * BOARD_LENGTH}")
    print(f"C2   length: {C2 / (C1 + C2 + C3) * BOARD_LENGTH}")
    print(f"C3   length: {C3 / (C1 + C2 + C3) * BOARD_LENGTH}")
    print(f"D1   length: {D1_proportion * BOARD_LENGTH}")
    print(f"D2&3 length: {(1 - D1_proportion) * BOARD_LENGTH}")
    print(f"D2   length: {D1 / (D1 + D1 + D1) * BOARD_LENGTH}")
    
    
if __name__ == "__main__":
    # calc_46_sided_polygon_diameter()
    # calc_46_sided_polygon_diameter(0.005)
    split_board_length()
    