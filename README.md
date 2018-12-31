# Learning_tensorflow
Simple predictive model and weights and bias optimization using tensorflow methods

Prerequisit:
- Tensorflow installed.
- basic understanding of tensors, tensorflow graph, session 
- understanding of Placeholder variables and constant.
Note in this demo i have used predefined gradient descent method direcltly. hence basic understanding is required(atleast process knowledge).

Explaination:

     1. import tensorflow as tf
- is python way of importing tensorflow module which is installed on our machine. 
- one thing to notice here that we are using alias tf for tensorflow import, hence we will be using tf instead of tensorflow.

      2. Load the data : 
- is to load the data set how ever in this demo i have taken very simple X and Y value.

      3.  x = tf.placeholder(tf.float32)
          y = tf.placeholder(tf.float32)
- We will be creating placeholder for X and Y as values will be passed later during execution of graph
      
      4. m_curr = tf.Variable([0.0],tf.float32)
          b_curr = tf.Variable([0.0],tf.float32)
- we are  creating m and b values with 0 initialization. note that i have used Variable because the value will change later.

      5. ypred = m_curr * x + b_curr
- we are defining relation between x and y using above equation. 

      6. squared_err = tf.square(ypred - y)
        loss = tf.reduce_sum(squared_err)
- is used to calculate the error in our model because of m and b value that we have put randomly.
- our job is to minimize the error as much as possible.

      7. optimizer = tf.train.GradientDescentOptimizer(0.01)
        train = optimizer.minimize(loss)
- here  i am using gradientDescentoptimizer() available with tensorflow.train package.
- if you wish to see the code for gradient descent(known as backpropogation - neural network reference) in python check here : https://github.com/gauravsb14/GradientDescentInPython
      
      8. sess = tf.Session()
        sess.run(init)
        for i in range(1000):
          sess.run(train,feed_dict={x:[1,2,3,4,5],y:[5,7,9,11,13]})
- at last we are training model by creating session and passing x and y value and adjusting m and b value.

      9. pr = sess.run(ypred,feed_dict={x:[4,5,6]})
          print("prediction is {}".format(pr))
- here we are predicting y value for given x value 
      



