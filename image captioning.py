import numpy as np
import pandas as pd
import os
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input # type: ignore
from tensorflow.keras.preprocessing.image import load_img, img_to_array # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding # type: ignore
from tensorflow.keras.models import Model # type: ignore

# Load pre-trained VGG16 model without top layers
vgg_model = VGG16(include_top=False, weights='imagenet')

# Freeze the weights
for layer in vgg_model.layers:
    layer.trainable = False

# Function to extract features from an image using VGG16
def extract_features(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    features = vgg_model.predict(img)
    return features

# Load captions
def load_captions(filename):
    captions = pd.read_csv(filename, header=None)
    captions.columns = ['image', 'caption']
    return captions

# Tokenize captions
def tokenize_captions(captions):
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(captions['caption'])
    return tokenizer

# Define captioning model
def captioning_model(vocab_size, max_length):
    inputs1 = Input(shape=(7, 7, 512))
    fe1 = tf.keras.layers.GlobalMaxPooling2D()(inputs1)
    fe2 = Dense(256, activation='relu')(fe1)
    inputs2 = Input(shape=(max_length,))
    se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
    se2 = LSTM(256)(se1)
    decoder1 = Dense(256, activation='relu')(fe2)
    decoder2 = Dense(256, activation='relu')(se2)
    decoder3 = Dense(256, activation='relu')(decoder1)
    decoder4 = Dense(256, activation='relu')(decoder2)
    decoder5 = tf.keras.layers.Add()([decoder3, decoder4])
    outputs = Dense(vocab_size, activation='softmax')(decoder5)
    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

# Generate caption given an image
def generate_caption(model, tokenizer, photo, max_length):
    in_text = 'startseq'
    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = word_for_id(yhat, tokenizer)
        if word is None:
            break
        # Check if the word is 'endseq' or if it has been repeated
        if word == 'endseq' or word in in_text:
            break
        in_text += ' ' + word
    return in_text


# Map an integer to a word
def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

# Define paths
image_folder = 'image captioning\Images'
captions_path = 'image captioning\captions.txt'

# Load captions
captions_df = pd.read_csv(captions_path, header=None, delimiter=',', names=['image', 'caption'])
captions_dict = dict(zip(captions_df['image'], captions_df['caption']))

# Extract features for each image in the folder
image_files = os.listdir(image_folder)
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    photo = extract_features(image_path)
    
    # Get caption for the current image from captions.txt
    caption = captions_dict.get(image_file)
    
    # Print the image file name along with the caption from captions.txt
    print(f"Image: {image_file}, Caption: {caption}")