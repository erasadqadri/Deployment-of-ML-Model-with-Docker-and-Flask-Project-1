# Deployment of Machine Learning Model (Bank Note Authentication) With Docker and Flask using Python:

• Flask is a small and lightweight Python web framework that provides useful tools and features that make creating web applications in Python.

• Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages.

|Language Used: | Python             |
|---------------|--------------------|

|IDE 1 Used:    | Jupyter Notebook |
|---------------|--------------------|

|IDE 2 Used:    | PyCharm          |
|---------------|--------------------|

## Get the Dataset:

Dataset Link: https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data

Data were extracted from images that were taken from genuine and forged banknote like specimens. For digitization, an industrial camera was used for print inspection. The final images have 400x400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 600 dpi were gained. Wavelet Transform tool were used to extract features from images. Dataset was retrieved from UCI Repositories.

Extracted Features = Variance, Skewness, Curtosis, Entropy and Class

Where;

class 0 => Fake / Inauthentic

class 1 => Authentic

## Import the Dataset:

The name of the dataset, I have used for this project is 'BankNoteAuthentication.csv'.

Dataset contains five columns -> Variance, Skewness, Curtosis, Entropy and Class. The shape of our dataset is (1373, 5).

In BankNoteAuthentication.csv, first four columns i.e. Variance, Skewness, Curtosis, Entropy are independent variables whereas fifth column Class is dependent variable.

## Importing the Libraries:

Importing following essential libraries

• Pandas

• Numpy

• Matplotlib

• Scikit-Learn

• Scipy

• Pickle

• Flask

## Matrix of Dependent and Independent Variables:

In Python, you have to create two matrices for independent variables and dependent variable.

Hence for BankNoteAuthentication.csv, create one matrix for four independent variables and then create one matrix dependent variable.

## Split the Dataset into Training Data and Test Data:

ML is about a machine that is going to learn from the data to make predictions.

We need to split the dataset into training set and test set. Using training set, we build the machine learning model and using test set, we test the performance of this machine learning model.

We are building our ML model on training set by establishing some correlation between independent variables and dependent variables and once the ML model understands the correlation between independent variables and dependent variables. We will test if the ML model can apply the correlations it understood based on training set at test set.

In brief, we have to make two different datasets. The training set on which the machine learning model learns and test set on which we test if the ML model learned correctly the correlations.

In Python, model_selection class from scikitlearn library is used to split the dataset into training and test set.

In this project, I have given 70% of data for training and 30% of data for testing.

## Applying Random Forest Classifier:

Random forests are an ensemble learning method for classification, regression and other tasks that operate by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes or mean prediction of the individual trees.

## Accuracy Score:
In this project I have achieved an accuracy of 99% (0.9902912621359223)

## Creating Pickle File:
After creating classifier model we need to create a pickle file, so that it can be used in flask app. This can be done using Serialization.

## Create Flask App: (File Name => FlaskApp.py)

Step 1: Open and Load Pickle File.

Step 2: This app will be running at port number 127.0.0.1:5000

Step 3: Create Flask Welcome(First) Page at Route Page.

Step 4: Creating Predition Page.

Step 5: Passing 'TestFile.csv' and then all the values in it should get predicted.

  We can not do this from the browser once we run the function, so we will use something known as Postman. After testing 'TestFile.csv' through Postman I have got output as => predicted class value for TestFile is [0,0,0,0,1,1,1,1,1]

## Deploying Machine Learning Models Using Flask And Flasgger: (File Name => FrontEndUI.py)

Flasgger helps us to create front end UI in a much easy way.

Step 1: From Flasgger we will import Swagger which is used to generate front end UI.

Step 2: From Swagger I have intialized flask app.

Step 3: This will be running at 127.0.0.1:5000/apidocs/

Step 4: Created two functions
	predict_note_authentication
	predict_note_file

Step 5: In predict_note_authentication function I have used get method to provide input by the user manually.

Step 6: In this different parameters are added such as Variance, Skewness, Curtosis and Entropy.

Step 7: In predict_note_file function I have used post method to provide input directly from the file. (you just have to browse the repective file).

## Building And Running Docker Image:

After Installation of Docker you need to follow following steps

Step 1: Write Docker File. (File Name => Dockerfile)

Step 2: Build Docker Image

Command => docker build -t frontendui .

Step 3: Running our FrontEndUI App

Command => docker run -p 8000:8000 frontendui
