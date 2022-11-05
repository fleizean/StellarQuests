from genericpath import exists
from importlib.resources import path
import os
from colorama import Fore, init

# First PHASE -> Payment Operations
createaccount_dir = "../stellar-quest-go-main/stellar-quest-go-main/payment_operations/create_account"
payment_dir = "../stellar-quest-go-main/stellar-quest-go-main/payment_operations/payment"
changetrust_dir = "../stellar-quest-go-main/stellar-quest-go-main/payment_operations/change_trust"
manageoffers_dir = "../stellar-quest-go-main/stellar-quest-go-main/payment_operations/manage_offers"
pathpayments_dir = "../stellar-quest-go-main/stellar-quest-go-main/payment_operations/path_payments"

# Second PHASE -> Configuration Operations
accountmerge_dir = "../stellar-quest-go-main/stellar-quest-go-main/configuration_operations/account_merge"
managedata_dir = "../stellar-quest-go-main/stellar-quest-go-main/configuration_operations/manage_data"
setflag_dir = "../stellar-quest-go-main/stellar-quest-go-main/configuration_operations/set_flags"
setoptionshomedomain_dir = "../stellar-quest-go-main/stellar-quest-go-main/configuration_operations/set_options_home_domain"
setoptionsweightsthresholds_dir = "../stellar-quest-go-main/stellar-quest-go-main/configuration_operations/set_options_weights_thresholds_and_signers"

# Third PHASE -> Advanced Operations

bumpsequence_dir = "../stellar-quest-go-main/stellar-quest-go-main/advanced_operations/bump_sequence"
claimablebalances_dir = "../stellar-quest-go-main/stellar-quest-go-main/advanced_operations/claimable_balances"
clawbacks_dir = "../stellar-quest-go-main/stellar-quest-go-main/advanced_operations/clawbacks"
liquiditypools_dir = "../stellar-quest-go-main/stellar-quest-go-main/advanced_operations/liquidity_pools"
sponsorship_dir = "../stellar-quest-go-main/stellar-quest-go-main/advanced_operations/sponsorship"

# Secret PHASE -> NFT's
feebumptransactions_dir = "../stellar-quest-go-main/stellar-quest-go-main/side_quests/fee_bump_transactions"
mintannftonstellar_dir = "../stellar-quest-go-main/stellar-quest-go-main/side_quests/mint_an_nft_on_stellar"

## First Welcome Text
firstwelcome = Fore.CYAN + """
𓆩--------- Stellar Quests ---------𓆪"""
firstwelcome += """""" + Fore.LIGHTRED_EX + """
1- Payment Operations
2- Configuration Operations
3- Advanced Operations
4- Side Quest
5- Exit
"""
firstwelcome += """""" + Fore.CYAN + """𓆩----------------------------------𓆪"""

## First Phase Text
paymentsoperations = Fore.CYAN + """
𓆩--------- Payment Operations ---------𓆪"""
paymentsoperations += """""" + Fore.LIGHTRED_EX + """
1- Create Account Quest
2- Payment Quest
3- Change Trust Quest
4- Manage Offers Quest
5- Path Payments Quest
6- Hiçbiri
7- Exit
"""
paymentsoperations += """""" + Fore.CYAN + """𓆩--------------------------------------𓆪"""

# Second Phase Text
configurationoperations = Fore.CYAN + """
𓆩----------- Configuration Operations -----------𓆪"""
configurationoperations += """""" + Fore.LIGHTRED_EX + """
1- Account Merge Quest
2- Manage Data Quest
3- Set Options - Home Domain Quest
4- Set Options - Weights, Thresholds, and Signers Quest
5- Set Flags Quest
6- Hiçbiri
7- Exit
"""
configurationoperations += """""" + Fore.CYAN + """𓆩------------------------------------------------𓆪"""

## Third Phase Text
advancedoperations = Fore.CYAN + """
𓆩--------- Advanced Operations ---------𓆪"""
advancedoperations += """""" + Fore.LIGHTRED_EX + """
1- Bump Sequence Quest
2- Sponsorships Quest
3- Claimable Balances Quest
4- Clawbacks Quest
5- Liquidity Pools Quest
6- Hiçbiri
7- Exit
"""
advancedoperations += """""" + Fore.CYAN + """𓆩---------------------------------------𓆪"""
## Side Quest Phase NFT's Text
sidequest = Fore.CYAN + """
𓆩--------- Side Quest ---------𓆪"""
sidequest += """""" + Fore.LIGHTRED_EX + """
1- Fee Bump Transactions Quest
2- Mint An NFT on Stellar Quest
3- Hiçbiri
4- Exit
"""
sidequest += """""" + Fore.CYAN + """𓆩------------------------------𓆪"""
######################

flag_in_dir = 0

while(1):
    print(firstwelcome + Fore.WHITE)
    secim = input("Quest numarası giriniz: ")
    if secim == "1":
        os.system('cls')
        print(paymentsoperations + Fore.WHITE)
        secim2 = input("Payment Quest numarası giriniz: ")
        if secim2 == "1":
            flag_in_dir = 1
            os.chdir(createaccount_dir)
            os.system("go run solution.go")
        elif secim2 == "2":
            flag_in_dir = 1
            os.chdir(payment_dir)
            os.system("go run solution.go")
        elif secim2 == "3":
            flag_in_dir = 1
            os.chdir(changetrust_dir)
            os.system("go run solution.go")
        elif secim2 == "4":
            flag_in_dir = 1
            os.chdir(manageoffers_dir)
            os.system("go run solution.go")
        elif secim2 == "5":
            flag_in_dir = 1
            os.chdir(pathpayments_dir)
            os.system("go run solution.go")
        elif secim2 == "6":
            continue
        elif secim2 == "7":
            exit()
    elif secim == "2":
        os.system('cls')
        print(configurationoperations + Fore.WHITE)
        secim2 = input("Configuration Quest numarası giriniz: ")
        if secim2 == "1":
            flag_in_dir = 1
            os.chdir(accountmerge_dir)
            os.system("go run solution.go")
        elif secim2 == "2":
            flag_in_dir = 1
            os.chdir(managedata_dir)
            os.system("go run solution.go")
        elif secim2 == "3":
            flag_in_dir = 1
            os.chdir(setoptionshomedomain_dir)
            os.system("go run solution.go")
        elif secim2 == "4":
            flag_in_dir = 1
            os.chdir(setoptionsweightsthresholds_dir)
            os.system("go run solution.go")
        elif secim2 == "5":
            flag_in_dir = 1
            os.chdir(setflag_dir)
            os.system("go run solution.go")
        elif secim2 == "6":
            continue
        elif secim2 == "7":
            exit()
    elif secim == "3":
        print(advancedoperations + Fore.WHITE)
        secim2 = input("Advanced Quest numarası giriniz: ")
        if secim2 == "1":
            flag_in_dir = 1
            os.chdir(bumpsequence_dir)
            os.system("go run solution.go")
        elif secim2 == "2":
            flag_in_dir = 1
            os.chdir(sponsorship_dir)
            os.system("go run solution.go")
        elif secim2 == "3":
            flag_in_dir = 1
            os.chdir(claimablebalances_dir)
            os.system("go run solution.go")
        elif secim2 == "4":
            flag_in_dir = 1
            os.chdir(clawbacks_dir)
            os.system("go run solution.go")
        elif secim2 == "5":
            flag_in_dir = 1
            os.chdir(liquiditypools_dir)
            os.system("go run solution.go")
        elif secim2 == "6":
            continue
        elif secim2 == "7":
            exit()
    elif secim == "4":
        os.system('cls')
        print(sidequest + Fore.WHITE)
        secim2 = input("Side Quest numarası giriniz: ")
        if secim2 == "1":
            flag_in_dir = 1
            os.chdir(feebumptransactions_dir)
            os.system("go run solution.go")
        elif secim2 == "2":
            flag_in_dir = 1
            os.chdir(mintannftonstellar_dir)
            os.system("go run solution.go")
        elif secim2 == "3":
            continue
        elif secim2 == "4":
            exit()
    elif secim == "5":
        exit()
    else:
        print("Girdiğiniz numara ile eşleşen bir veri yok.")
    if flag_in_dir == 1:
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        os.chdir("py")
        