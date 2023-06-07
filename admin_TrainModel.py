import tensorflow as tf
import os
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# Import categorialcrossentropy to use in model.compile()
training_folder = os.getcwd() + "/data/train/"
testing_folder = os.getcwd() + "/data/validation/"

# Prepare the dataset
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2)

train_generator = train_datagen.flow_from_directory(
    training_folder,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='training')

validation_generator = train_datagen.flow_from_directory(
    testing_folder,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='validation')

# Build the model
base_model = tf.keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
x = tf.keras.layers.Flatten()(base_model.output)
x = tf.keras.layers.Dense(256, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(4, activation='softmax')(x)
model = tf.keras.models.Model(base_model.input, x)
model.summary()

# Compile the model
model.compile(loss='categorical_crossentropy',
              optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
              metrics=[tf.keras.metrics.CategoricalCrossentropy()])

# Train the model
checkpoint = tf.keras.callbacks.ModelCheckpoint('best_model.h5', save_best_only=True, save_weights_only=True)
early_stop = tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
history = model.fit(train_generator, epochs=100, validation_data=validation_generator, callbacks=[checkpoint, early_stop])

# Save the model
model.save('model.h5')

# Plot the model accuracy and loss
val_loss = history.history['val_loss']
loss = history.history['loss']
val_cross = history.history['val_categorical_crossentropy']
plt.plot(val_loss, label='Validation Loss')
plt.plot(loss, label='Training Loss')
plt.plot(val_cross, label='Validation Categorical Crossentropy')
plt.plot()
plt.legend()
plt.savefig('model.png')
