import os,sys
import os.path
import re
from PIL import Image, ExifTags
from datetime import datetime

path = sys.argv[1]
tool = sys.argv[2]

if tool == "JADX" or tool == "jadx":
        extension = ".java"
elif tool == "APKTOOL" or tool == "apktool":
        extension = ".smali"
else:
        sys.exit()

imgextension = [".jpg",".jpeg",".png",".gif",".bmp"]
sourcesList = []
imgsourcesList = []
path_save = os.path.join(path, "extracted_data.txt")         


class Extractor:
    def __init__(self, file):
        self.file = file

    def fileReader(self, file):
        f = open(file,"r").read()
        return f

    def runRegEX(self, datatype, regexpression):
        with open(path_save,"a") as fileData:
            data = self.fileReader(self.file)
            results= list(set(re.findall(regexpression, data)))

            for result in results:
                if len(result) < 2:
                    pass
                else:
                    fileData.write('{0}: {1}\n'.format(datatype, result.strip()))

    def runRegEX2(self, datatype, regexpression):
        with open(path_save,"a") as fileData:
            data = self.fileReader(self.file)
            results= list(set(re.findall(regexpression, data)))

    def interes_files(self):
        int_files = open(path_save,"a")
        words = open("config/custom.lst","r").read()
        data = self.fileReader(self.file)

        for word in words.split("\n"):
            if len(word) >= 2:
                if word.upper() in data:
                    int_files.write("{}: {}\n".format(word.upper(),self.file))
                elif word.lower() in data:
                    int_files.write("{}: {}\n".format(word.lower(),self.file))
                elif word in data:
                    int_files.write("{}: {}\n".format(word,self.file))

def getFiles(path):
    for fpath, dirs,files in os.walk(path):
        for file in files:
            if extension in file:
                sourcesList.append(os.path.join(fpath, file))

def getIMGFiles(path):
    for fpath, dirs,files in os.walk(path):
        for file in files:
            for ie in imgextension:
                if ie in file:
                    imgsourcesList.append(os.path.join(fpath, file))

def main():
    with open(path_save,"w") as fileData:
        fileData.write("Info for APK: {0}")

    getFiles(path)
    getIMGFiles(path)

    for sl in sourcesList:
        extractor = Extractor(sl)
        extractor.runRegEX('EMAIL',r'[a-zA-Z0-9\.\-+_!#]+@[a-zA-Z0-9\.\-+_!#]+\.[a-zA-Z]+(?:\([^\x00-\x08\x0E-\x1F\x7F-\xFF]*\))*')
        extractor.runRegEX('URL',r'(?:http|https|ftp|mailto|tel):\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+(?:\?[\w/\-?=%.]*)?(?:#[\w/\-?=%.]*)?')
        extractor.interes_files()

    with open(path_save,"a") as fileData:
        for isl in imgsourcesList:
            img = Image.open(isl)
            img_exif = img.getexif()
            if img_exif != None:
                img_exif_dict = dict(img_exif)
                for key, val in img_exif_dict.items():
                    if key in ExifTags.TAGS:
                        fileData.write('IMG {0} {1}:{2}\n'.format(isl, ExifTags.TAGS[key], repr(val)))

    print(" [+] Sources list successfully generated !")

if __name__ == '__main__':
    main()
