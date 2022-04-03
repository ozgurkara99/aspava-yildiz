from pydoc import apropos
from PIL import Image
import matplotlib.pyplot as plt
import torch
import torchvision.transforms as T
import torchvision
import numpy as np

import cv2
import random
import warnings
import argparse
import os

def deneme(a):
    if a < 0:
        return True
    else:
        return False

<<<<<<< HEAD
argpar = argparse.ArgumentParser()
argpar.add_argument("--w", type=int, default=256)
argpar.add_argument("--h", type=int, default=256)
argpar.add_argument("--img_folder", type=str, default="python/images/")
argpar.add_argument("--dst_folder", type=str, default="python/images_real/")
args = argpar.parse_args()

warnings.filterwarnings('ignore')

# load model
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True).cuda()
# set to evaluation mode
model.eval()

DST_FOLDER = args.dst_folder 

if not os.path.exists(args.dst_folder):
  os.mkdir(args.dst_folder) 

# load COCO category names
COCO_CLASS_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]



def get_coloured_mask(mask):
  colours = [[0, 255, 0],[0, 0, 255],[255, 0, 0],[0, 255, 255],[255, 255, 0],[255, 0, 255],[80, 70, 180],[250, 80, 190],[245, 145, 50],[70, 150, 250],[50, 190, 190]]
  r = np.zeros_like(mask).astype(np.uint8)
  g = np.zeros_like(mask).astype(np.uint8)
  b = np.zeros_like(mask).astype(np.uint8)
  r[mask == 1], g[mask == 1], b[mask == 1] = colours[random.randrange(0,10)]
  coloured_mask = np.stack([r, g, b], axis=2)
  return coloured_mask



def get_prediction(img_path, confidence, width, height):
  img = Image.open(img_path)
  img_return = img.resize((width, height), Image.BILINEAR)
  transform = T.Compose([T.ToTensor()])
  img = transform(img_return).cuda()
  pred = model([img])
  pred_score = list(pred[0]['scores'].cpu().detach().numpy())
  pred_t = [pred_score.index(x) for x in pred_score if x>confidence][-1]
  pred_class = [COCO_CLASS_NAMES[i] for i in list(pred[0]['labels'].cpu().detach().numpy())]
  dog_index = pred_class.index("dog")
  masks = (pred[0]['masks']>0.5).squeeze().detach().cpu().numpy()
  
  masks = np.expand_dims(masks[dog_index], axis=0)
  
  pred_class = pred_class[:pred_t+1]
  return masks, pred_class, img_return.convert('RGB')




def segment_instance(img_path, width, height, confidence=0.5):
  masks, pred_cls, img = get_prediction(img_path, confidence, width, height)
  print(pred_cls)
  x = np.asarray(img)
  masks = masks.astype(int)
  masks = np.moveaxis(masks, [0, 1, 2], [2, 0, 1])
  masks = np.dstack([masks, masks, masks])

  result = np.multiply(masks,x).astype(np.uint8)
  img_path = img_path.replace("\\", "/")
  fp = os.path.join(DST_FOLDER, img_path.split("/")[-1])

  plt.imsave(fp, result)



from os import listdir
from os.path import isfile, join
from tqdm import tqdm


onlyfiles = [f for f in listdir(args.img_folder) if isfile(join(args.img_folder, f))]
onlyfiles_dst = [f for f in listdir(DST_FOLDER) if isfile(join(DST_FOLDER, f))]
onlyfiles = list(set(onlyfiles) - set(onlyfiles_dst))
for file in tqdm(onlyfiles):
  # try:
  file_p = os.path.join(args.img_folder, file)
  segment_instance(file_p, args.w, args.h, confidence=0.5)
  # except:
  #     pass
=======
def main():
    print("hello222333")
    print("ozgurdenemeasdasads")
    # exp2 = 
    a = [-1,-2,3,4,5]
    b = list(map(lambda x:x**2,a))
    c = list(filter(deneme, a))
    a 
    print(a,c)
    
    
if __name__ == "__main__":
    main()
>>>>>>> 9eac019d2b8717d7316329d5773318bbf6141728
