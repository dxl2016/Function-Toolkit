### Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization
### Search/tuning hyperparameter, speed up learning algorithm, optimization
### Week 1:
  * layers
  * hiddlen units
  * learning rates
  * activation functions
  * mini-batch sizes
  * learning rate decay
  * train/dev/test: preferred train and dev have the same distribution
<br/><br/>
  * high bias or/and variance problems (given Bayes optimal error)
  * bigger network (bias) + more data (variance)
    1. regularization (reduce bias and avoid overfitting): L1 (sparse), L2 (weight decay GD)
    ex: high lambda: a lot of w close to 0, simpler/smaller NN or nearly linear activation functions, 
      leadning to less overfitting 
    2. droupout regularization: inverted dropout (last step: rescale to keep the same expectation values of activation functions)
    intuition: keep-prob>0, can't rely on any one feature, so have to spread out weights
    3. data augmentation: generate more data
    4. early stopping: give mid-size w
<br/><br/>  
  * orthogonalization: two tasks (optimal cost function J + not overfitting)
  * normalizing inputs: use the same rescale to normalize mu and sigma on the training and test datasets
  * to easier and faster optimize and learn w
  * vanishing/exploding gradients (w)
  * weight initialization: ReLU activation functions - sqrt(2/n[l-1]), etc.
<br/><br/>
  * gradient check (two-sided epi)
<br/><br/>
### Week 2:
  * mini-batch gradient descent vs batch: vectorization
  * 1-epoch: 1 pass through training set
  * if mini-batch size = 1: SGD
  * smaller dataset (<= 2000)
  * typical mini-batch sizes (2^6, 2^7, 2^8, 2^9, 2^10)
  * mini-batch fit in CPU/GPU memory
  * epi = 1-beta, (1epi)^(1/epi) = 1/e
  * EWMA, bias correction, use for GD with momentum and learning rate, default beta = 0.9
  * RMSprop, add epi=10^-8 for squared root stability in the denominator
  * Adam (adapt momentum estimation) optimization algorithm, alpha needs to be tuned, beta1 = 0.9 (dw), beta2 = 0.999 (dw2), epi = 10^-8
  * learning rate decay alpha, formulas or manual decay
  * the problem of local optima, saddle points
  * problem of plateaus, can make learning rate slow
<br/><br/>
### Week 3:
  * alpha is of the most importance
  * try random values, do not use a grid
  * use an appropriate scale to pick hyperparameters, random exponent, not random linearly
  * batch normalization: can we normalize a/z values as to tune w and b faster?
  * for each mini-batch: x (w1, b1) --> z1 (batch norm beta1 and gamma1) --> z~1 --> a1 = g(z~1) (w2, b2) --> z2 (batch norm beta2 and gamma2) --> z~2 --> a2 ... [beta is not the one for momentum]
  * z[l] = w[l]a[l-1], calculate z[l]norm, z~[l] = gamma * z[l]norm + beta[l] is to increase non-linearity of the sigmoid fucntion
  * work with momentum, RMSprop, and Adam to back-prop update parameters
  * reduce variance shifting around and stablize earlier layers, and make latter layers easier to learn
  * this has a slight regularization effect, each mini-batch is scaled by the mean/variance computed on just that mini-batch
  * a larger mini-batch will reduce that regularization effect
  * batch norm at a test time: use EWMA or running mean/variance of the entire training set
  * softmax regression and classifier
  * sigmoid vs relu vs tanh
  * tf
  
  
  
