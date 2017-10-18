import tensorflow as tf
hello=tf.constant('Hello!')
sess=tf.Session()
print(sess.run(hello))
a=tf.add(3,5)
print(a)