# Oh soldier Prettify my Folder
# path, dictionary file, format
# def soldier("C://", "harry.txt", "jpg")
import os
def soldier(path,file,format):
    os.chdir(path)
    i=1
    many_files=os.listdir(path)

    with open(file) as f:
        filelist=f.read().split("\n")         #not to be included

    
    for file in many_files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1]==format:
            os.rename(file,f"{i}.{format}")
            i+=1

soldier(r"C:\All dekstop files and codes\Testing"
        ,r"C:\All dekstop files and codes\python codes\ext.txt",".jpg")
