purple=$'\033[1;34m'
reset=$'\033[0;39m'
red=$'\033[0;31m'
green=$'\033[0;32m'

echo "Gerekli Modüller İndiriliyor...";
pip3 install colorama
clear;
echo "Gerekli Modüller İndirildi.";
clear;

read -n1 -p "${purple}StellarQuest'i başlatmak için: [${green}y${purple}/${red}N${purple}]${reset} " input
    echo;
    echo "İşlem başarıyla onaylandı. via: eyagiz";
    sleep 1;
    clear;
    python3 py/stellar.py
    else
    echo "Bir sorun var :("
    fi