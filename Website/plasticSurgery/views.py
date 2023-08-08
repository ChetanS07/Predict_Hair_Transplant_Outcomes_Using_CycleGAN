from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import default_storage
import os

def getImage(request):
    return render(request,'getImage.html')

def result(request):
    dataset_directory = '.\\datasets\\plastic_surgery\\testA'
    result_directory = '.\\results\\plasticSurgery\\test_latest\\images'

    # Get a list of all the files in the directory
    d_files = os.listdir(dataset_directory)
    r_files= os.listdir(result_directory)

    print(d_files)
    print(r_files)

    for file in d_files:
        filepath = os.path.join(dataset_directory, file)
        os.remove(filepath)

    for file in r_files:
        filepath = os.path.join(result_directory, file)
        os.remove(filepath)

    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['preopimg']
        filename = uploaded_file.name
        filename = 'before.jpg'
        pathname = default_storage.save('D:\\MiniProject\\Website\\project\\datasets\\plastic_surgery\\testA\\' + filename, uploaded_file)
        pathname = default_storage.url(pathname)

         # code to produce result
        os.system('python test.py --dataroot datasets/plastic_surgery/testA --name plasticSurgery --model test --no_dropout')

        return redirect('/view')

    return HttpResponse("<h1>Failed to record image, Try Again</h1>")


def view(request):
    context = {
        'before':'\\result\\media\\before_real.png',
        'after' :'\\result\\media\\before_fake.png'
    }
    # print(context)
    return render(request, 'view.html', context)


# D:\MiniProject\Website\project