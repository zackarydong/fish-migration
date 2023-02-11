import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import dataparse as dp
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


def build_grid(time):
    grid = [[None for _ in range(11)] for _ in range(8)]
    for i in range(0,8):
        for j in range(0,11):
            grid[7 - i][j] = dp.predictedtemp((j,i), time)
    return grid

fig = plt.figure(figsize=(7, 7))

ax = fig.add_subplot()

plt.xlabel("Longitude")
plt.ylabel("Latitude")



#starting in 1971 so 2019 is 576 months out, 1176 is 2069

def yearly():
    arr = []
    i = 576
    while i <= 1176:
        arr.append(build_grid(i))
        i += 12
    return arr

def monthly():
    arr = []
    for i in range(576, 709):
        arr.append(build_grid(i))
    return arr


arr = np.array(yearly())
print(np.nanmin(arr), np.nanmax(arr))

i = 0

im = plt.imshow(arr[0], extent = [12, 0 , 55, 63 ] , animated=True)

# dx = 7/72.; dy = 0/72. 
# offset = mpl.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)

# apply offset transform to all x ticklabels.
# for label in ax.xaxis.get_majorticklabels():
#     label.set_transform(label.get_transform() + offset)

cb = fig.colorbar(im)
im.set_clim(8.5, 15)
plt.title(f'Sea Surface Temperatures in 2019, January')

def updatefig(*args):
    global i
    if (i<133):
        i += 1
    else:
        i=0
    # vmin = np.nanmin(arr[i])
    # vmax = np.nanmax(arr[i])

    im.set_array(arr[i])
    im.set_clim(8.5, 15)
    plt.title(f'Sea Surface Temperatures in {2019 + i}, January')
    
    #norm = mpl.colors.Normalize(vmin = np.min(arr[i]), vmax = np.max(arr[i]))
    # if i > 12:
    #     if i % 12 == 0:
    #         plt.title(f'Sea Surface Temperatures in {int(i/13) + 2019}, Month: 12')
    #     else:
    #         plt.title(f'Sea Surface Temperatures in {int(i/12) + 2019}, Month: {i%12}')
    # else:
    #     plt.title(f'Sea Surface Temperatures in 2019, Month: {i}')


    #cb = plt.colorbar(mpl.cm.ScalarMappable(norm = norm))
    return im,

anim = animation.FuncAnimation(fig, updatefig,  blit=True)
plt.show()