import cv2
import numpy as np
import matplotlib as mapli
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid

def rgb(image : np.array) -> np.array:
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def gray(image : np.array) -> np.array:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def grid(images : list[np.array], rows : int, cols : int, size : int, colors : list[str] = None) -> None:
    fig = plt.figure(figsize=(size,size))
    grid = ImageGrid(fig, 111, nrows_ncols=(rows, cols), axes_pad=0.1)

    if colors is not None:
        counter = 0
        for ax, im in zip(grid, images):
            ax.imshow(im, cmap=colors[counter])
            counter = (counter + 1) % len(colors)
        plt.show()
    else:
        for ax, im in zip(grid, images):
            ax.imshow(im)
        plt.show()


mario = cv2.imread('./images/mario.png', cv2.IMREAD_UNCHANGED)
mario = rgb(mario)
sky = cv2.imread('./images/background.jpg')
_,apple_mask = cv2.threshold(mario[:,:,3], 0, 255, cv2.THRESH_BINARY)

grid([rgb(apple_mask)], 1, 1, 10)