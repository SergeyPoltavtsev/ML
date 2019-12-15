from fastai import *
from fastai.vision import *
import torch

# path = untar_data(URLs.MNIST)
# data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2, ds_tfms=get_transforms(), size=224, num_workers=4).normalize(imagenet_stats)
# learn = cnn_learner(data, models.resnet18, metrics=accuracy)

# learn.fit_one_cycle(1)

torch.cuda.is_available()
torch.cuda.empty_cache()

mnist = untar_data()