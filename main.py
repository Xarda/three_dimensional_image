import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from PIL import Image, ImageOps
from mpl_toolkits.mplot3d import Axes3D
from utils import get_default_image, resize_img


def plot_img_in_three_dimensions(img=None, img_out_path=None, color=True, scaling_factor=1):
    if img == None:
        img = get_default_image()

    img_gray = ImageOps.grayscale(img)  
    
    img = np.asarray(img)
    img_gray = np.asarray(img_gray)

    print("Base-image shape:", img.shape, "Gray-image shape:", img_gray.shape)
    assert img.shape[:2] == img_gray.shape

    h, w = img.shape[:2]
    print("Number of pixels:", h * w)

    img_gray_flat = img_gray.ravel()
    
    pixel_positions = np.array(list(product(range(h), range(w)))) * scaling_factor

    # assert matching vector sizes
    assert img_gray_flat.shape[0] == pixel_positions.shape[0]

    fig = plt.figure(figsize=(15, 15*(h/w)))
    ax = plt.axes(projection='3d')
    ax.set_title('3d image')
    ax.view_init(elev=90., azim=0)
    ax.grid(False)
    # rescaling plot axes to match image aspect ratio
    ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1*(h/w), 1, 1, 1]))

    ax.scatter(
        xs=pixel_positions[:,0], 
        ys=pixel_positions[:,1], 
        zs=img_gray_flat, 
        s=0.1, 
        c=img.reshape((h*w, img.shape[2])) / 255.0 if color else img_gray_flat,
        cmap='color' if color else 'gray',
        alpha=0.5
    )
    
    if img_out_path:
        fig.savefig(str.split(img_out_path, ".")[0] + "_3d_img.png")

    plt.show()


if __name__ == "__main__":

    # set your own image path or name here
    # otherwise you can use one of sample images:
    # zebra.jpg - forest_and_sea.jpg - moon.jpg - door.jpg
    img_path = "imgs/"
    img_name = "zebra.jpg"#"forest_and_sea.jpg"#"moon.jpg"#"door.jpg"

    img = Image.open(img_path + img_name)
    
    # if the input image is too big, it may be a 
    # good idea to shrink the image in order
    # to improve performance
    if any(dimension > 500 for dimension in img.size):
        img = resize_img(img, target_width=500)

    # when passing no image, a default image will be created and plotted
    plot_img_in_three_dimensions(img, img_out_path=img_path + img_name)
