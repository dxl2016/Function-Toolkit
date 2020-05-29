### Convolutional Neural Networks
### ConvNets, Deep convolutional models, image recognition/classfication, object detections
### Machine learning, deep learning, cv, nlp
### Two sources of knowledge: 1. labeled data (x,y) supervised learning 2. hand-engineered features/network architecture/other components
### Week 1:
  * cv: image classification, object detection, neural style transfer
  * RGB channels
  * conv filter/kernel, size is usually odd, better to have central pixel, 3*3, 5*5
  * problems: shrink output, missing information from the edges
  * padding: valid padding and same padding
  * strided conv
  * output size: (n+2p-f)/s + 1 running down to int
  * cross-correlation vs convolution
  * multiple layers: depth/channels = # of features
  * padding, flatten, fit into logistic/softmax regression, etc.
  * layers: conv, pool, fc
  * output size: (batch size, width, height, # of channels)
  * pooling: max poolig, average pooling; **max pooling usually uses no padding, no parameter back prop to learn through pooling, fix function**
  * ex. conv layer (each can be deep, multiple filters) + pooling + flatten + FC layer + softmax unit + output
  * usually count as layers if have weights (parameters)
  * activation sizes decrease, as # of parameters increase
  * why conv: 1. sharing parameters 2. sparsity of connections; avoid overfitting and better capture translations and variations
<br><br/>
  ### Week 2:
  * LeNet, AlexNet, VGG, etc.
  * ResNets: residual blocks, main paths vs short cuts/skip connections, help vanishing/exploding gradient problems
  * preserve layer dimensions/sizes, make adjustments using vectors Ws if necessary
  * inception network: bottleneck layer, channel concat, some side branches make predictions in the hiddlen units and prevent from overfitting, stack up multiple modules to become a network
  * transfer learning: ImageNets, pre-trained weights, freeze early layers
  * data augmentation: 
    1. mirroring, random cropping, rotation, shearing, local warping, etc.
    2. color shifting, distort color channels, PCA color augmentation
  * benchmarks (but not help product systems): 
    1. ensembling (average outputs not parameter weights, 3-15 networks)
    2. multi-crop at test time and average the outputs
  * architecture of networks in the lit, pre-trained + fine tune
<br><br/>
  ### Week 3:
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
