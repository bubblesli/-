import os
from shutil import copy
import random
 

def mkfile(file):
    if not os.path.exists(file):
        os.makedirs(file)


file = 'sn_data/sn'
sf_class = [cla for cla in os.listdir(file) if ".txt" not in cla]
mkfile('sn_data/train')
for cla in sf_class:
    mkfile('sn_data/train/'+cla)

mkfile('sn_data/val')
for cla in sf_class:
    mkfile('sn_data/val/'+cla)

split_rate = 0.1
for cla in sf_class:
    cla_path = file + '/' + cla + '/'
    images = os.listdir(cla_path)
    num = len(images)
    eval_index = random.sample(images, k=int(num*split_rate))
    for index, image in enumerate(images):
        if image in eval_index:
            image_path = cla_path + image
            new_path = 'sn_data/val/' + cla
            copy(image_path, new_path)
        else:
            image_path = cla_path + image
            new_path = 'sn_data/train/' + cla
            copy(image_path, new_path)
        print("\r[{}] processing [{}/{}]".format(cla, index+1, num), end="")  # processing bar
    print()

print("processing done!")
