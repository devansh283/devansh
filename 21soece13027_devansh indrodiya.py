import PySimpleGUI as sg
import datetime
import os
import os.path
import shutil

from datetime import datetime

def file_extension(filename):
    split_tup = os.path.splitext(filename)
    return split_tup[1]

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.fromtimestamp(t)

def directory_exists(temp_dest):
    return os.path.isdir(temp_dest)

def create_directory(d, dir):
    path=os.path.join(d, dir)
    os.mkdir(path)

def file_exists(f):
    return os.path.exists(f)

def movefile(s, d):
    shutil.move(s, d)

sg.theme("Reddit")

layout = [[sg.Text("")], [sg.Text("Choose Source folder: ", size=(20, 1)), sg.InputText(), sg.FolderBrowse()], [sg.Text("Choose Destination folder: ", size=(20, 1)), sg.InputText(), sg.FolderBrowse()], [sg.Text("")], [sg.Button("Submit", size=(8, 1))]]

window = sg.Window("Project Based Learning", layout, size=(600,200))
    
while True:
    event, values = window.read()

    if values[0] == '':
        print("Source Path can't be empty")
        continue

    if values[1] == '':
        print("Destination Path can't be empty")
        continue
    
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    
    elif event == "Submit":
        source=values[0]
        destination=values[1]
        break

fileDict = {
            'js' : 'javascript',
            'docx' : 'documents',
            'html' : 'web',
            'css' : 'web',
            'zip' : 'compressed',
            'py' : 'python',
            'img' :'images',
            'png' :'images',
	        'jpg' :'images',
            'jpeg' : 'images',
            'txt' :'text',
            'exe' : 'executable file',
            'class':'class',
            'java': 'java'}


source += '/'
destination += '/'

for filename in os.listdir(source):
   
    extension=(file_extension(filename))
    extension=extension[1:]
    try:
        extension = fileDict[extension]
    except KeyError:
         pass

    if extension == '':
        continue

    temp = destination + extension

    if not(directory_exists(temp)):
        create_directory(destination, extension)

    s = source + filename
    d = destination + extension + '/' + filename

    if file_exists(d):
        print(filename, " already exists")
        continue
    
    movefile(s, d)

for foldername in os.listdir(source):
    temp = source
    temp += foldername
    temp += '/'
    for file in os.listdir(temp):

        print(file)
        t = temp + file
        print(t)
        year = str(modification_date(t))
        
        y = year[:4]
        month = year[5:7]   
        print(month)  
        os.chdir(temp)
        if os.path.exists(y):
            print(y," folder is exist")
        else:
           os.mkdir(y)
           print(y,"folder is created")
        d = temp + y 
        print(d)
        os.replace(t,d +"/"+file)

        for f in os.listdir(d):
            os.chdir(d)
            if os.path.exists(month):
                print(month," folder is exist")
        else:
           os.mkdir(month)
           print(month,"folder is created")
        si = d +"/"+ month
        fi = d +"/"+ file
        print(fi)
        print(si)
        os.replace(fi,si +"/"+file)
            
