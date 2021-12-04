
# Blindness Detection Using Deep Learning

Blindness here referring to DiabeticRetinopathy detection
People suffer from diabetes are likely to have this disease.
The symptoms are swelling, blurness etc.
unfortunately this disease is irreversible - It cannot be cured if it is not detected at the mild stage!
The doctor has to analyse the fundus images of the patient taken by technician, 
all the prominent features or symptoms may not be clearly visible at mild stage which makes it difficult to diagnose it at mild stage
So using automatic tools to detect it using deep learning is proposed which will take fundus image as input ans classifies it into five class(stages of diabetic retinopathy)-
1. Mild
2. Moderate
3. Proliferate
4. Severe
5. No diabetic retinopathy

### This repository consists of -
app.py - deployment code
diabetic_retinopathy.ipynb - model training code
train.csv - labeling of images 
static folder - consists of css and js files
template folder - consists of hmtl files

### The sample of dataset -
![download](https://user-images.githubusercontent.com/66114853/144719873-66906303-d64d-4628-9fbd-c2250995b2b6.png)


### The dataset consists of five classes -
![bkkhb](https://user-images.githubusercontent.com/66114853/144719867-6ea45e8d-6626-4159-becb-fa8bfd8a0034.PNG)


### The architecture used here is RESNET18
### The Model Summary is shown below -
![1](https://user-images.githubusercontent.com/66114853/144719617-56b204c8-c477-4286-a0b3-af154be40589.PNG)
![2](https://user-images.githubusercontent.com/66114853/144719842-e7b3c478-25fb-4331-892b-5d718e4b8047.PNG)
![3](https://user-images.githubusercontent.com/66114853/144719849-dddd2296-b74b-4103-8269-bad818ad3eb9.PNG)


### Screenshots of tool I have developed -
The below is the Home page - This page includes the Risk factors, Symptoms, When to visit a doctor and information about five classes

![home page](https://user-images.githubusercontent.com/66114853/144719894-20d1b254-206c-478b-a946-7ea82b460fac.PNG)


The below is Predict page - The user has to upload a fundus image and the diagnosis will be displayed

![predictt](https://user-images.githubusercontent.com/66114853/144719978-928f44b5-c5f9-4e81-8268-c581f5817a6e.PNG)
