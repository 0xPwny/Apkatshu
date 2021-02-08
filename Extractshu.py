import os,sys
import re
from PIL import Image, ExifTags

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

class Extractor:
    def __init__(self, file):
        self.file = file

    def fileReader(self, file):
        f = open(file,"r").read()
        return f

    def validate_ip(self, ip):
        if ":" in ip:
            ip = ip.split(":")[0]
        m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
        return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))

    def runRegEX(self, datatype, regexpression):
        with open("EX_DATA.txt","a") as fileData:
            data = self.fileReader(self.file)
            results= list(set(re.findall(regexpression, data)))

            for result in results:
                if len(result) < 2:
                    pass
                else:
                    fileData.write('{0}: {1}\n'.format(datatype, result.strip()))

    def runRegEX2(self, datatype, regexpression):
        with open("EX_DATA.txt","a") as fileData:
            data = self.fileReader(self.file)
            results= list(set(re.findall(regexpression, data)))

            for result in results:
                if self.validate_ip(ip):
                    fileData.write('{0}: {1}\n'.format(datatype, result.strip()))

    def interes_files(self):
        int_files = open("EX_DATA.txt","a")
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
    with open("EX_DATA.txt","w") as fileData:
        write("Info for APK: {0}", path)

    getFiles(path)
    getIMGFiles(path)

    for sl in sourcesList:
        extractor = Extractor(sl)
        extractor.runRegEX('EMAIL',r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
        extractor.runRegEX('URL',r'(?:https?|ftp):\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+')
        extractor.runRegEX2('IP',r'[0-9]+(?:\.[0-9]+){3}')
        extractor.runRegEX2('IPS',r'[0-9]+(?:\.[0-9]+){3}:[0-9]+')
        extractor.interes_files()

    with open("EX_DATA.txt","a") as fileData:
        for isl in imgsourcesList:
            img = Image.open(isl)
            img_exif = img.getexif()
            if img_exif != None:
                img_exif_dict = dict(img_exif)
                for key, val in img_exif_dict.items():
                    if key in ExifTags.TAGS:
                        fileData.write('IMG {0} {1}:{2}\n'.format(isl, ExifTags.TAGS[key], repr(val)))

    print("[+] Sources list successfully generated !")

if __name__ == '__main__':
    main()
