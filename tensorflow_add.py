import tensorflow as tf 

hello_op = tf.constant('Hello,tensorflow!')
a = tf.constant(10)
b = tf.constant(20)
c = tf.Variable(tf.zeros([3]))
compute_op = tf.add(a,b)
print(c.value)

with tf.Session() as sess:
	print(sess.run(hello_op))
	print(sess.run(compute_op))
