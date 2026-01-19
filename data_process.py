# import the necessary packages
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from skimage import feature
from imutils import paths
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

import cv2
import os
import pickle

basepath= os.path.normpath('E:/100% Signature_Recognition/100% Signature_Recognition/')

def fd_hu_moments(image):
    #For Shape of signature Image
    feature = cv2.HuMoments(cv2.moments(image)).flatten()
    return feature

def quantify_image(image):
    #For Speed and pressure of signature image

    # compute the histogram of oriented gradients feature vector for
    # the input image
    features = feature.hog(image, orientations=9,
        pixels_per_cell=(10, 10), cells_per_block=(2, 2),
        transform_sqrt=True, block_norm="L1")

    # return the feature vector
    return features

def load_split(path):
    # grab the list of images in the input directory, then initialize
    # the list of data (i.e., images) and class labels
    path=trainingPath
    imagePaths = list(paths.list_images(path))
    data = []
    labels = []

    # loop over the image paths
    for imagePath in imagePaths:
        # extract the class label from the filename
        label = imagePath.split(os.path.sep)[-2]
#        print(imagePath)
        # load the input image, convert it to grayscale, and resize
        # it to 200x200 pixels, ignoring aspect ratio
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (200, 200))

        # threshold the image such that the drawing appears as white
        # on a black background
        image = cv2.threshold(image, 0, 255,
            cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        # quantify the image
        features1 = quantify_image(image)
        features2 = fd_hu_moments(image)
        global_feature = np.hstack([features1,features2])

        # update the data and labels lists, respectively
        data.append(global_feature)
        
        labels.append(label)

    # return the data and labels
    return (np.array(data), np.array(labels))


trainingPath = os.path.sep.join([basepath, "dataset1/training"])
testingPath = os.path.sep.join([basepath, "dataset1/testing"])


## loading the training and testing data
#print("[INFO] loading data...")
(trainX, trainY) = load_split(trainingPath)
(testX, testY) = load_split(testingPath)

# encode the labels as integers
le = LabelEncoder()
trainY = le.fit_transform(trainY)
testY = le.transform(testY)

# initialize our trials dictionary
trials = {}


######CNN Model ################################################
def CNN_Model():
   
    from keras.models import Sequential
    from keras.layers.convolutional import Conv2D
    from keras.layers.convolutional import MaxPooling2D
    from keras.layers.core import Activation
    from keras.layers.core import Flatten
    from keras.layers.core import Dense
    from keras.optimizers import Adam
    from sklearn.preprocessing import LabelBinarizer
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report
    from PIL import Image
    import numpy as np
    import os
    # construct the argument parser and parse the arguments
#    basepath= os.path.normpath('D:\Alka_python_2019_20\Alka_python_2019_20\Handwriting Signature Recognition\Dataset\dataset1')
    
    imagePaths=[]
    
    for path in os.listdir(basepath + '\\dataset2\\real'):
        full_path = os.path.join(basepath + '\\dataset2\\real', path)
        imagePaths.append(full_path)
    
    for path in os.listdir(basepath + '\\dataset2\\forge'):
        full_path = os.path.join(basepath + '\\dataset2\\forge', path)
        imagePaths.append(full_path)
        
    data = []
    labels = []
    
    # loop over our input images
    for imagePath in imagePaths:
    	# load the input image from disk, resize it to 32x32 pixels, scale
    	# the pixel intensities to the range [0, 1], and then update our
    	# images list
    	image = Image.open(imagePath)
    	image = np.array(image.resize((32, 32))) / 255.0
    	data.append(image)
    	# extract the class label from the file path and update the
    	# labels list
    	label = imagePath.split(os.path.sep)[-2]
    	labels.append(label)
        
    # encode the labels, converting them from strings to integers
    lb = LabelBinarizer()
    labels = lb.fit_transform(labels)
    

    # perform a training and testing split, using 75% of the data for
    # training and 25% for evaluation
    (trainX, testX, trainY, testY) = train_test_split(np.array(data),
    	np.array(labels), test_size=0.25)
    from keras.utils import to_categorical
    trainY = to_categorical(trainY)
    testY = to_categorical(testY)
    
    # define our Convolutional Neural Network architecture
    model = Sequential()
    model.add(Conv2D(8, (3, 3), padding="same", input_shape=(32, 32, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(16, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(32, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(2))
    model.add(Activation("softmax"))
    
    # train the model using the Adam optimizer
    print("[INFO] training network...")
    opt = Adam(lr=1e-3, decay=1e-3 / 50)
    model.compile(loss="categorical_crossentropy", optimizer=opt,
    	metrics=["accuracy"])
    
    H = model.fit(trainX, trainY, validation_data=(testX, testY),
    	epochs=400, batch_size=32)
    
#    basepath= os.path.normpath('D:/Signature_Recognition/dataset')
    
    model.save(basepath + '\CNN_model.h5')
    
    scores = model.evaluate(testX, testY, verbose=0)
    A="Test Set Accuracy: %.2f%%" % (scores[1]*100)
    print("Test Set Accuracy: %.2f%%" % (scores[1]*100))
#    
    scores1 = model.evaluate(trainX, trainY, verbose=0)
    A1="Train Set Accuracy: %.2f%%" % (scores1[1]*100)
#    print(A1)
    C="CNN Model Saved as <<  CNN_model.h5  >>"
    
    D =A+'\n' +  A1 +'\n'+ C
#    D =A+ '\n'+ C
    
    import numpy as np
    
    pred = model.predict(testX)

    predicted = np.argmax(pred, axis=1)
    report = classification_report(np.argmax(testY, axis=1), predicted)
    print(report)

    from plt_graph import plot_model_history
    plot_model_history(H)
    
    
    
    return D  
    