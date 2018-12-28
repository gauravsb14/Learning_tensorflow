#1. import tensorflow Module
import tensorflow as tf

# 2. load the data :
#     - data can be loaded using different methods
# in this program wehave not used any real time data

# 3. creating placeholders for X  and y
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# 4. Network parameter :
m_curr = tf.Variable([0.0],tf.float32)
b_curr = tf.Variable([0.0],tf.float32)

# create network model:
model = m_curr * x + b_curr

# calculating loss
squared_err = tf.square(model - y)
loss = tf.reduce_sum(squared_err)

# optimization - best value of coefficient
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# global variable initializer
init = tf.global_variables_initializer()

# training under session
sess = tf.Session()
sess.run(init)
for i in range(1000):
    sess.run(train,feed_dict={x:[1,2,3,4,5],y:[5,7,9,11,13]})
print(sess.run([m_curr,b_curr]))

# Predicting value
pr = sess.run(model,feed_dict={x:[4,5,6]})
print("prediction is {}".format(pr))