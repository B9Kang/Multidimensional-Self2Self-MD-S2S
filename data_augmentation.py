import torch 
import numpy as np
import torchvision.transforms.functional as F
import random

def random_shift_rotate(image, max_translate=(0.1, 0.1)):
    w = 256
    h = 256
    max_t_w, max_t_h = max_translate
    max_angle = random.randint(-10, 10)

    trans_coef = np.random.rand() * 2 - 1
    w_t = int(trans_coef * max_t_w * w)
    h_t = int(trans_coef * max_t_h * h)
    image = F.affine(image, translate=(w_t, h_t), shear=0, angle=max_angle, scale=1)

    return image


def data_augmentation(img, flip_v, flip_h,device):
    axis = []
    if flip_v:
        axis.append(2)
    if flip_h:
        axis.append(3)
    if len(axis):
        # img = random_shift_rotate(img)
        img = torch.flip(img, axis)
        
    return img


