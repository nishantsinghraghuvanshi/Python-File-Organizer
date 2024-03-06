import os

dire = input("Enter Directory : ")
direc = dire.replace("\ " , "/")

#first lets make all the extension folder
extension = []
a = os.listdir(direc)
for i in a:
    file_type = i[-3:]
    if (file_type not in extension):
        extension.append(file_type)
print(extension)

#Now time to make folder Extension Wise :-)


try:
    for i in extension:
        os.mkdir(direc+"/"+i.capitalize())
except:
    print(".......")



#Now Its time to move the items

for i in a:
    if(i[-3:] == "pdf"):
        os.rename(direc+"/"+i,direc+"/Pdf/"+i)
    elif(i[-3:] == "exe"):
        os.rename(direc+"/"+i,direc+"/Exe/"+i)
    elif(i[-3:] == "png"):
        os.rename(direc+"/"+i,direc+"/Png/"+i)
    elif(i[-3:] == "jpg"):
        os.rename(direc+"/"+i,direc+"/Jpg/"+i)
    elif(i[-3:] == "jar"):
        os.rename(direc+"/"+i,direc+"/Jar/"+i)
    elif(i[-3:] == "mp4"):
        os.rename(direc+"/"+i,direc+"/MP4/"+i)
    elif(i[-3:] == "mp3"):
        os.rename(direc+"/"+i,direc+"/MP3/"+i)
    elif(i[-3:] == "zip"):
        os.rename(direc+"/"+i,direc+"/Zip/"+i)
    elif(i[-3:] == "rar"):
        os.rename(direc+"/"+i,direc+"/Rar/"+i)
    elif(i[-3:] == "iso"):
        os.rename(direc+"/"+i,direc+"/Iso/"+i)
    elif(i[-2:] == "py"):
        os.rename(direc+"/"+i,direc+"/Py/"+i)
    elif(i[-4:] == "html"):
        os.rename(direc+"/"+i,direc+"/Html/"+i)
