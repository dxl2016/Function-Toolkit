### Convolutional Neural Networks
### ConvNets, deep convolutional models, image recognition/classification, object detections
### Machine learning, deep learning, cv, nlp
### Two sources of knowledge: 1. labeled data (x,y) supervised learning 2. hand-engineered features/network architecture/other components
### Week 1: Foundations of Convolutional Neural Networks
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
  * pooling: max pooling, average pooling; **max pooling usually uses no padding, no parameter back prop to learn through pooling, fix function**
  * ex. conv layer (each can be deep, multiple filters) + pooling + flatten + FC layer + softmax unit + output
  * usually count as layers if have weights (parameters)
  * activation sizes decrease, as # of parameters increase
  * why conv: 1. sharing parameters 2. sparsity of connections; avoid overfitting and better capture translations and variations
<br><br/>
  ### Week 2: Deep convolutional models: case studies
  * LeNet, AlexNet, VGG, etc.
  * ResNets: residual blocks, main paths vs short cuts/skip connections, help vanishing/exploding gradient problems
  * preserve layer dimensions/sizes, make adjustments using vectors Ws if necessary
  * inception network: bottleneck layer, channel concat, some side branches make predictions in the hidden units and prevent from overfitting, stack up multiple modules to become a network
  * transfer learning: ImageNets, pre-trained weights, freeze early layers
  * data augmentation: 
    1. mirroring, random cropping, rotation, shearing, local warping, etc.
    2. color shifting, distort color channels, PCA color augmentation
  * benchmarks (but not help product systems): 
    1. ensembling (average outputs not parameter weights, 3-15 networks)
    2. multi-crop at test time and average the outputs
  * architecture of networks in the lit, pre-trained + fine tune
<br><br/>
### Week 3: Object detection
  * object localization: 1 object vs multiple objects (of different categories)
  * define label y (a vector): (bounding box) bx, by, bH, bW, (class) c, **0<bx, by<1, bH and bW can be > 1 (outside the grid cell)**
  * ex: landmark detection
  * object detection: **sliding windows detection**
  * sharing computation, **convolution implementation of sliding windows**
  * bounding box predictions: **YOLO algorithm, output volumes are n_sub_bgrid * n_sub_bgrid * label_y_dim, only look up midpoint coordinates of the objects** ex, FC layer 400 to (1, 1, 400) 
  * intersection over union (>=0.5, >=0.6, >=0.7)
  * non-max suppression: ensure one detection per object, discard pc<0.5, pick the one box with the max pc as a prediction, filter out boxes with IoU>=0.5
  * anchor boxes, (grid cell, anchor box) pair, look at the highest IoU, **n_sub_bgrid * n_sub_bgrid * label_y_dim * anchor_box_num**, better at detecting specialized objects, can use k-mean to automatically select anchor box sizes, ex. (19 * 19 * 5 anchor boxes * 8 label dim)
  * region proposals: R-CNN, segmentation algorithm to narrow down num of blobs
<br><br/>
### Week 4: Special applications: face recognition & neural style transfer
  * an application: face recognition, live detection, supervised learning
  * face verification vs face recognition
  * one-shot learning
  * encoding image representation/similarity: Siamese network, DeepFace
  * triplet loss (Anchor, Positive, Negative), add margin alpha, FaceNet
  * face verification and binary classification, similarity function (ex. chi-sq) and logistic regression
  * pre-compute image encodings, save computation costs
  * neural style transfer
  * deep ConvNets learning
  * neural style transfer cost function: use GD to min J(G) (C: content, S: style, G: generated), J(G) = alpha * J(C, G) + beta * J(S, G)
  * content cost function: too shallow < layer l < too deep, use pre-trained ConvNet (ex. VGG network)
  * measure similarity: J(C, G) = norm(a[l][C] - a[l][G]), element-wise sum-of-sq differences
  * style cost function: define style as correlation between activations across channels (# of channels is a lot in deep learning),nH, nW, nC, correlation gives high-level texture components yes/no occur in a part of image
  * style matrix (gram matrix G): a[i,j,k][l]; style matrix G[l] in shape of nC * nC
  * G[l][k,k'] = sum of sum of a[i,j,k][l] * a[i,j,k'][l] (non-normalized cross-covariance), apply for both S and G
  * J(S, G) = norm(G[l][S] - G[l][G]), usually adjusted by 1/(2nH * nW * nC)^2, can also apply a multiplier lambda for each layer
  * 1D and 3D generalization: ConvNets, but RNN, LSTM, etc are specific for sequence data
  * 3D applications: CT scans, movies, etc.
  
  
  
  
  
  
  
  
  
  
  
