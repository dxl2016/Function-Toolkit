### Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization
### Week 1:
  * layers,
  * hiddlen units
  * learning rates
  * activation functions
  * train/dev/test: preferred train and dev have the same distribution
  
  * high bias or/and variance problems (given Bayes optimal error)
  * bigger network (bias) + more data (variance)
  1. regularization (reduce bias and avoid overfitting): L1 (sparse), L2 (weight decay GD)
  ex: high lambda: a lot of w close to 0, simpler/smaller NN or nearly linear activation functions, 
    leadning to less overfitting 
  2. droupout regularization: inverted dropout (last step: rescale to keep the same expectation values of activation functions)
  intuition: keep-prob>0, can't rely on any one feature, so have to spread out weights
  3. data augmentation: generate more data
  4. early stopping: give mid-size w
  
  * orthogonalization: two tasks (optimal cost function J + not overfitting)
  * normalizing inputs: use the same rescale to normalize mu and sigma on the training and test datasets
  * to easier and faster optimize and learn w
  * vanishing/exploding gradients (w)
  * weight initialization: ReLU activation functions - sqrt(2/n[l-1]), etc.
  
  * gradient check (two-sided epi)
  
### Week 2:
  
  
  
  
