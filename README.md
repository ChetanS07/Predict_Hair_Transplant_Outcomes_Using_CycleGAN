# Predict_Hair_Transplant_Outcomes_Using_CycleGAN

**This project aims to predict the post-operative outcomes of hair transplant surgery. The project uses a CycleGAN model for training, and the dataset is created manually.**

**Steps for training the model or using the existing one**
1. You can train the model by yourself or you can use the model provided by us.
2. If you choose to train model by yourself, then you can use this google colab file "HairTransplantPrediction.ipynb" for training purpose.
3. You can create your own dataset if you want, else you can use the dataset provide by us.

**Steps to run website**
1. Install the "django" on your system.
2. cd to "Website" folder
3. create a virtual environment and activate it.
4. now install all the required libraries by running command
    ``pip install -r requirements.txt``
5. download the pretrained model from https://drive.google.com/file/d/1G8tjn-m6rOSKTFtF5U2YNjL4IHXGCLop/view?usp=drive_link
6. copy this file and paste into "checkpoints/plasticSurgery/
7. set proper paths in "plasticSurgery/views.py"
8. finally run the command to start server
    ``python manage.py runserver``

**Snapshot of website**

image upload:

![Screenshot 2023-08-09 001900](https://github.com/ChetanS07/Predict_Hair_Transplant_Outcomes_Using_CycleGAN/assets/95538723/ba4a2873-dfbf-47a2-9bab-f9256fa1ec3a)

result:

![Screenshot 2023-08-09 001838](https://github.com/ChetanS07/Predict_Hair_Transplant_Outcomes_Using_CycleGAN/assets/95538723/09b4e8f8-e03f-4322-9d06-aa38f9285d68)


