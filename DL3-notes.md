### Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization
### Search/tuning hyperparameter, speed up learning algorithm, optimization
### Week 1: recurrent neural networks
  * speech recognition, music generation, sentiment classification, DNA sequence analysis, machine translation, video activity recognition, name entity recognition
  * supervised learning, mapping x and y
  * NLP: dictionary representing words: size 30k, or 1M
  * a standard network does not share features learned across different positions of text, RNN reduces the number of parameters 
  * Forward propagation and backpropagation
  * RNN architectures: many-to-many (x and y in same/different [encoder-decoder] lengths) such as in machine translation, many-to-one (sentiment classification), one-to-one (standard generic NN), one-to-many (music generation)
  * attention architecture
  * language model and sequence generation
  * sampling novel sequences: character-level language model vs word-level language model
  * normal RNNs (relatively weak long-range dependencies), 
  * potential problems: vanishing gradients or exploding gradients
  * exploding gradients solution: gradient clipping: rescale some of the gradient vectors
  * vanishing gradients solution: GRU, LSTM (update, forget, and output gates)
  * Peephole connection
  * bidirectional RNN (BRNN) with GRU or LSTM (most common)
  * deep RNN (the number of layers is smaller than the one in deep CNN)




<br/><br/>
