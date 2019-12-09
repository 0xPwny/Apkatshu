# Apkatshu
- Apkatshu its a Tool for extracting urls , emails , ip address , and interesting data from APK files

  <img src="img/Apkatshu.png" alt="apkatshu">

```text
Apkatshu : tool written in bash/python  for extracting urls, emails, ip addresses, and interesting data from APK files. 
The user can choose either JADX or APKTOOL for de-compilation.
```

## USAGE :
- JADX : 

./Apkatshu.sh (JADX/jadx) file.apk

- APKTOOL : 

./Apkatshu.sh (APKTOOL/apktool) file.apk

Searching For other keywords :

  - add the keywords you want to look for them into config/custom.lst
  
  
**fixed** :

- more regex to get more mails 
- .smali for APKTOOL , and .java for JADX
- hide JADX stderr
- Modifications to support python3
- indentation errors
- more regex for ip address extraction and validation


## Special thanks @chmodxx , @b1337k , @ubernoob for their support
