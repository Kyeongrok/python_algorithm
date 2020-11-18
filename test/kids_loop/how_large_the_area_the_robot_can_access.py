import numpy as np
import matplotlib.pyplot as plt
def make_a_coords(extent):
    x_s = np.arange(-extent, extent+1, 1)
    y_s = np.arange(-extent, extent+1, 1)

    ### Loop through each point and check if safe
    coords = []
    for y in y_s:
        x_coords = []
        for x in x_s:
            coords_digits_sum = sum([int(i) for i in str(abs(x))]) + sum([int(i) for i in str(abs(y))])
            if coords_digits_sum <= 23:
                safe = True
            else:
                safe = False
            x_coords.append(safe)
        coords.append(x_coords)
    return coords


extent = 750
coords = make_a_coords(extent)

print(coords)

# ### Initialize the origin as `really_safe` point
# coords[extent][extent] = 'really_safe' # Origin
#
# ### Iteratively check if a safe point is beside a `really_safe` point
# changing = True
# while changing == True:
#     changing = False
#     # Skip the first and last rows and columns because these are just paddings for looking up/down/left/right
#     for y,x_coords in enumerate(coords[1:-1], start=1):
#         for x,is_safe in enumerate(x_coords[1:-1], start=1):
#             if is_safe == 'really_safe':
#                 continue
#             ### look up, down, left, right of the point being checked
#             elif is_safe and ('really_safe' in [coords[y-1][x], coords[y+1][x], coords[y][x-1], coords[y][x+1]]):
#                 coords[y][x] = 'really_safe'
#                 changing = True
#
# ### Count the number of "really safe" points only
# really_safe_points = [[1 if safety == 'really_safe' else 0 for safety in x_coords[1:-1]] for x_coords in coords[1:-1]]
# plt.imshow(really_safe_points)
# plt.gca().invert_yaxis()
#
# ### Exclude first and last rows and columns in total area calculation since those were not iterated over
# plt.title(f"Accessible area: {sum([sum(i) for i in really_safe_points])}. Total area: {((extent-1)*2)**2}")
# plt.show()