#!/bin/bash
NC='\033[0m'
RED='\033[1;38;5;196m'
GREEN='\033[1;38;5;040m'
ORANGE='\033[1;38;5;202m'
BLUE='\033[1;38;5;012m'
BLUE2='\033[1;38;5;032m'
PINK='\033[1;38;5;013m'
GRAY='\033[1;38;5;004m'
NEW='\033[1;38;5;154m'
YELLOW='\033[1;38;5;214m'
CG='\033[1;38;5;087m'
CP='\033[1;38;5;221m'
CPO='\033[1;38;5;205m'
CN='\033[1;38;5;247m'
CNC='\033[1;38;5;051m'

cat << "EOF" 
                    $$\                 $$\               $$\                 
                    $$ |                $$ |              $$ |                
 $$$$$$\   $$$$$$\  $$ |  $$\ $$$$$$\ $$$$$$\    $$$$$$$\ $$$$$$$\  $$\   $$\ 
 \____$$\ $$  __$$\ $$ | $$  |\____$$\\_$$  _|  $$  _____|$$  __$$\ $$ |  $$ |
 $$$$$$$ |$$ /  $$ |$$$$$$  / $$$$$$$ | $$ |    \$$$$$$\  $$ |  $$ |$$ |  $$ |
$$  __$$ |$$ |  $$ |$$  _$$< $$  __$$ | $$ |$$\  \____$$\ $$ |  $$ |$$ |  $$ |
\$$$$$$$ |$$$$$$$  |$$ | \$$\\$$$$$$$ | \$$$$  |$$$$$$$  |$$ |  $$ |\$$$$$$  |
 \_______|$$  ____/ \__|  \__|\_______|  \____/ \_______/ \__|  \__| \______/ 
          $$ |                                                                
          $$ |                                                                
          \__|                                                                

EOF

Application=$2
Tool=$1
todate=$(date +"%Y-%m-%d")
file_base=`basename $Application .apk`
dist_dir="Outpkatshu/"$file_base"_katshu_$todate"


usage() { echo -e "Usage: ./lazyrecon.sh apktool/jadx file.apk " 1>&2; exit 1; }

while getopts ":h" option; do
   case $option in
      h) # display Help
         usage
         exit;;

     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
	 *)
            usage
            ;;

   esac
done

if [ ! -f  "${Application}" ] && [[ ! -f  ${Tool} ]]; then
   usage; exit 1;
fi

jadxx(){

	if which jadx >/dev/null; then
		true
	else
  		echo "[!] You need to install JADX first ."
  		exit
	fi


	if [ -d "$dist_dir" ]; then
		true
	fi
		$(mkdir -p $dist_dir)
	echo -e ${RED}  "\n[+] Pika Pika is Decompiling the application using jadx ... "

	jadx $Application -d $dist_dir > /dev/null
}


apkk(){

        if which apktool >/dev/null; then
                    true
        else
                echo "[!] You need to install APKTOOL first ."
                exit
        fi
	echo -e ${BLUE}  "\n[+] Pika Pika is Decompiling the application using apktool... "

	$(apktool d $Application -o $dist_dir -q)
}

function final(){
echo -e ${PINK} "[*] the extracted data has been saved to ".$dist_dir
echo -e -n ${YELLOW}"\n[*] Which Type of data you want to extract \n "
echo -e "  ${NC}[${CG}"1"${NC}]${CNC} urls"
echo -e "   ${NC}[${CG}"2"${NC}]${CNC} emails"
echo -e "   ${NC}[${CG}"3"${NC}]${CNC} Exit"
echo "\n[+] Select: "
        read pikatshu
                if [ $pikatshu -eq 1 ]; then
                        urls
                elif [ $pikatshu -eq 2 ]; then
                        emails
                elif [ $pikatshu -eq 3 ]; then
                      exit
                fi

}
function urls(){
	cat ./$dist_dir/extracted_data.txt | sort -u | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*"  | tee ./$dist_dir/extracted_urls.txt
	echo " [*] Extracted urls saved to ".$dist_dir/"extracted_urls.txt"
	final
}
function emails(){
	cat ./$dist_dir/extracted_data.txt | sort -u | grep -Eo '[[:alnum:]+\.\_\-]*@[[:alnum:]+\.\_\-]*' | tee ./$dist_dir/extracted_emails.txt
	final
}

function main(){

	echo -e ${GREEN} "[+] Application Successfully Decompiled ^.^ "
	sleep 2
	echo -e ${GREEN} "[+] Pika Pika extracting importants data from the application ... "

	python Extractshu.py $dist_dir $Tool
	final 
	urls
	emails
echo   "[+] Pikatshuuuuuuuuuuuu\n"
}
main
