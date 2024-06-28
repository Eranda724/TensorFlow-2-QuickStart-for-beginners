# -*- coding: utf-8 -*-
"""TensorFlow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dZJnqGUn0U5fory-IwxqsjfZqMxaHqaw
"""

import tensorflow as tf
print(tf.__version__)

minst = tf.keras.datasets.mnist #collection of hand written digits dataset

(x_train, y_train), (x_test, y_test) = minst.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  #Normalize the values train and test datasets

#pixel values define in range 0 to 255 , 0 = black 1=white. Scale 0 to 1

#train model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), #flatning the input, convrets array 2d(28*28) to 1d
    tf.keras.layers.Dense(128, activation='relu'), #connect every neurone in previous layer
    tf.keras.layers.Dropout(0.2), #to avoid overfitting , 0.2 means 20% fron input unit , which  0 while update unit
    tf.keras.layers.Dense(10) #activate softmax func to train to obtain probility
])

#define loss func
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
#return scaler for its loss logic examles

loss_fn

#loss_fn(y_train[:1], predictions).numpy() #calculate loss of first line of the example actual sample

model.compile(optimizer='adam', #optimization algo
              loss=loss_fn, #loss function
              metrics=['accuracy']) #metrics to monitor during training and testing

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)