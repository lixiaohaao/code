import torch
import tensorflow as tf
import keras

print(tf.test.is_gpu_available())
print(tf.__version__)

print(torch.cuda.is_available())
print(torch.__version__)