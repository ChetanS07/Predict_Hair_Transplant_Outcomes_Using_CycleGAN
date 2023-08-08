import os

dataset_directory = '.\\datasets\\plastic_surgery\\testA'
result_directory = '.\\results\\plasticSurgery\\test_latest\\images'

# Get a list of all the files in the directory
files = os.listdir(dataset_directory)
files= os.listdir(result_directory)

print(files)

# # Loop through the files and delete them
# for file in files:
#     filepath = os.path.join(directory, file)
#     os.remove(filepath)