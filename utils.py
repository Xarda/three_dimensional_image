import numpy as np
from PIL import Image

def get_default_image_I():
    # create default image I
    img = np.zeros((300, 300, 3)).astype(np.uint8)
    img[0:100,   0:100,   :] = 255
    img[0:100,   200:300, :] = 255
    img[100:200, 100:200, :] = 255
    img[200:300, 200:300, :] = 255
    img[200:300, 0:100,   :] = 255
    return Image.fromarray(img)

def get_default_image_II():
    # create default image II
    img = np.zeros((300, 300, 3)).astype(np.uint8)
    img[:,:,0] = np.identity(300, np.uint8) * 255
    img[:,:,1] = np.identity(300, np.uint8) * 100
    img[:,:,2] = np.identity(300, np.uint8) * 255
    img[140:160,:,:] = 255
    img[90:95,:,:2] = 255
    img[205:210,:,1:] = 255
    return Image.fromarray(img)

def get_default_image_III():
    # create default image III
    img = np.zeros((300, 400, 3)).astype(np.uint8)
    img[0:100,   0:100,   :2] = 255
    img[0:100,   200:300, :] = 255
    img[100:200, 100:200, 1:] = 255
    img[100:200, 300:400, 0] = 255
    img[200:300, 200:300, 1] = 255
    img[200:300, 0:100,   2] = 255
    return Image.fromarray(img)

def get_default_image(function_number=None):
    if function_number == None: 
        function_number = np.random.randint(3)
    
    if function_number == 0: return get_default_image_I()
    elif function_number == 1: return get_default_image_II()
    else: return get_default_image_III()

def resize_img(img, target_width=500):
    new_height = int((float(img.size[1]) * float((target_width / float(img.size[0])))))
    return img.resize((target_width, new_height), Image.ANTIALIAS)