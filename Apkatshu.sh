#!/bin/sh

cat << "EOF"
`;-.          ___,
  `.`\_...._/`.-"`
    \        /     ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -\'-     ,; \'. <
    ;.__     ,;|   > \
   / ,    / ,  |.-\.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /  APKATSHU v1.0
    (_,-'`> .'	 Author : 0xPwny
        (_,'
EOF




Application=$2
Tool=$1

file_base=`basename $Application .apk`
dist_dir="Outpkatshu/"$file_base"_katshu"

if [ ! -f $Application ]; then
	echo "[!]" $Application "not found !"
	exit
fi

jadxx(){

	if which jadx >/dev/null; then
		true
	else
  		echo "[!] You need to install JADX first ."
  		exit
	fi

#check for dir existence and decompile
	if [ -d "$dist_dir" ]; then
		true
	fi
		$(mkdir -p $dist_dir)
	echo "\n[+] Pika Pika is Decompiling the application using jadx ... "

	/root/Desktop/Apkatshu/jadx/build/jadx/bin/jadx $Application -d $dist_dir
}


apkk(){

        if which apktool >/dev/null; then
                    true
        else
                echo "[!] You need to install APKTOOL first ."
                exit
        fi
	echo "\n[+] Pika Pika is Decompiling the application using apktool... "

	$(apktool d $Application -o $dist_dir -q)
}




if [ -z "$Tool" ];then
	echo "\n[*] USAGE : ./Apkatshu.sh  JADX/APKTOOL file.apk \n"
	exit

elif [ "$Tool" = "APKTOOL" ];then
	apkk

elif [ "$Tool" = "JADX" ];then
	jadxx

else
	echo "use one from list"
	exit
fi

echo "[+] Application Successfully Decompiled ^.^ "
sleep 2
echo "[+] Pika Pika extracting importants data from the application ... "

python Extractshu.py $dist_dir

echo "\n[+] Pikatshuuuuuuuuuuuu "
