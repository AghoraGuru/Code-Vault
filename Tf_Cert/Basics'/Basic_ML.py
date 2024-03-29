import tensorflow as tf

#loading dataset from tf datasets
mnist = tf.keras.datasets.mnist

#train test split
(x_train,y_train),(x_test,y_test) = mnist.load_data()

#normalizing data
x_train, x_test = x_train / 255.0, x_test / 255.0

#model building - Sequential model with 2 dense laters

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(128,activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10,activation='softmax')
    ]
)

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(
    x_train,y_train,epochs=5,verbose=2
)
model.evaluate(x_test,y_test,verbose=2)
