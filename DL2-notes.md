### Convolutional Neural Networks
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
  * pooling: max poolig, average pooling; max pooling usually uses no padding, no parameter back prop to learn through pooling, fix function
  * ex. conv layer + pooling + flatten + FC layer + softmax unit + output
  * activation sizes decrease, as # of parameters increase
  * why conv: 1. sharing parameters 2. sparsity of connections
  <br><br/>
  ### Week 2:
  
  
  
