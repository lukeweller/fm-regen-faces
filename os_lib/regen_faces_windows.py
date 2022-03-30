
from __future__ import print_function
import time
import asyncio
import random
import os.path
import os
import glob
import pickle
import json
import re
import shutil
import sys


##### Nations datas #####
listnations = [{"flag": "AFG","nation": "Afghanistan","ethnicgroup": "Middle east"},{"flag": "AIA","nation": "Anguilla","ethnicgroup": "African"},{"flag": "ALB","nation": "Albanie","ethnicgroup": "South european"},{"flag": "ALG","nation": "Algérie","ethnicgroup": "Middle east"},{ "flag": "AND","nation": "Andorre","ethnicgroup": "South european"},{ "flag": "ANG", "nation": "Angola", "ethnicgroup": "African" }, { "flag": "ARG", "nation": "Argentine", "ethnicgroup": "Hispanic" }, { "flag": "ARM", "nation": "Arménie", "ethnicgroup": "South european" }, { "flag": "ARU", "nation": "Aruba", "ethnicgroup": "Hispanic" }, { "flag": "ASA", "nation": "Samoa américaines", "ethnicgroup": "Hispanic" }, { "flag": "ATG", "nation": "Antigua", "ethnicgroup": "African" }, { "flag": "aus", "nation": "Australie", "ethnicgroup": "South european" }, { "flag": "AUT", "nation": "Autriche", "ethnicgroup": "South european" }, { "flag": "AZE", "nation": "Azerbaïdjan", "ethnicgroup": "Middle east" }, { "flag": "BAH", "nation": "Bahamas", "ethnicgroup": "African" }, { "flag": "BAN", "nation": "Bangladesh", "ethnicgroup": "Indian" }, { "flag": "BAR", "nation": "Barbades", "ethnicgroup": "African" }, { "flag": "BDI", "nation": "Burundi", "ethnicgroup": "African" }, { "flag": "BEL", "nation": "Belgique", "ethnicgroup": "South european" }, { "flag": "BEN", "nation": "Bénin", "ethnicgroup": "African" }, { "flag": "BER", "nation": "Bermudes", "ethnicgroup": "African" }, { "flag": "BFA", "nation": "Burkina Faso", "ethnicgroup": "African" }, { "flag": "BHR", "nation": "Bahreïn", "ethnicgroup": "Middle east" }, { "flag": "BHU", "nation": "Bhoutan", "ethnicgroup": "Indian" }, { "flag": "BIH", "nation": "Bosnie", "ethnicgroup": "South european" }, { "flag": "blr", "nation": "Biélorussie", "ethnicgroup": "North european" }, { "flag": "BLZ", "nation": "Bélize", "ethnicgroup": "African" }, { "flag": "BOL", "nation": "Bolivie", "ethnicgroup": "Hispanic" }, { "flag": "BOT", "nation": "Botswana", "ethnicgroup": "African" }, { "flag": "BRA", "nation": "Brésil", "ethnicgroup": "Hispanic" }, { "flag": "BRU", "nation": "Sultanat de Brunei", "ethnicgroup": "East asian" }, { "flag": "BUL", "nation": "Bulgarie", "ethnicgroup": "North european" }, { "flag": "CAM", "nation": "Cambodge", "ethnicgroup": "East asian" }, { "flag": "CAN", "nation": "Canada", "ethnicgroup": "North european" }, { "flag": "CAY", "nation": "Îles Caïmans", "ethnicgroup": "African" }, { "flag": "CGO", "nation": "Congo", "ethnicgroup": "African" }, { "flag": "CHA", "nation": "Tchad", "ethnicgroup": "African" }, { "flag": "CHI", "nation": "Chili", "ethnicgroup": "Hispanic" }, { "flag": "CHN", "nation": "Chine", "ethnicgroup": "East asian" }, { "flag": "CIV", "nation": "Côte d'Ivoire", "ethnicgroup": "African" }, { "flag": "CMR", "nation": "Cameroun", "ethnicgroup": "African" }, { "flag": "COD", "nation": "RD Congo", "ethnicgroup": "African" }, { "flag": "COK", "nation": "Îles Cook", "ethnicgroup": "Hispanic" }, { "flag": "COL", "nation": "Colombie", "ethnicgroup": "Hispanic" }, { "flag": "COM", "nation": "Comores", "ethnicgroup": "African" }, { "flag": "CPV", "nation": "Îles du Cap-Vert", "ethnicgroup": "African" }, { "flag": "CRC", "nation": "Costa Rica", "ethnicgroup": "Hispanic" }, { "flag": "CRO", "nation": "Croatie", "ethnicgroup": "South european" }, { "flag": "CTA", "nation": "République centrafricaine", "ethnicgroup": "African" }, { "flag": "CUB", "nation": "Cuba", "ethnicgroup": "Hispanic" }, { "flag": "CUW", "nation": "Curaçao", "ethnicgroup": "African" }, { "flag": "cyp", "nation": "Chypre", "ethnicgroup": "South european" }, { "flag": "CZE", "nation": "République tchèque", "ethnicgroup": "North european" }, { "flag": "DEN", "nation": "Danemark", "ethnicgroup": "North european" }, { "flag": "DJI", "nation": "Djibouti", "ethnicgroup": "African" }, { "flag": "DMA", "nation": "Dominique", "ethnicgroup": "African" }, { "flag": "DOM", "nation": "République dominicaine", "ethnicgroup": "Hispanic" }, { "flag": "ECU", "nation": "Équateur", "ethnicgroup": "Hispanic" }, { "flag": "EGY", "nation": "Égypte", "ethnicgroup": "Middle east" }, { "flag": "ENG", "nation": "Angleterre", "ethnicgroup": "North european" }, { "flag": "EQG", "nation": "Guinée Équatoriale", "ethnicgroup": "African" }, { "flag": "ERI", "nation": "Érythrée", "ethnicgroup": "African" }, { "flag": "ESP", "nation": "Espagne", "ethnicgroup": "South european" }, { "flag": "est", "nation": "Estonie", "ethnicgroup": "North european" }, { "flag": "ETH", "nation": "Éthiopie", "ethnicgroup": "African" }, { "flag": "FIJ", "nation": "Îles Fidji", "ethnicgroup": "Hispanic" }, { "flag": "FIN", "nation": "Finlande", "ethnicgroup": "North european" }, { "flag": "fra", "nation": "France", "ethnicgroup": "South european" }, { "flag": "FRO", "nation": "Îles Féroé", "ethnicgroup": "North european" }, { "flag": "GAB", "nation": "Gabon", "ethnicgroup": "African" }, { "flag": "GAM", "nation": "Gambie", "ethnicgroup": "African" }, { "flag": "GEO", "nation": "Géorgie", "ethnicgroup": "South european" }, { "flag": "GER", "nation": "Allemagne", "ethnicgroup": "North european" }, { "flag": "GHA", "nation": "Ghana", "ethnicgroup": "African" }, { "flag": "gib", "nation": "Gibraltar", "ethnicgroup": "South european" }, { "flag": "GNB", "nation": "Guinée-Bissau", "ethnicgroup": "African" }, { "flag": "GRE", "nation": "Grèce", "ethnicgroup": "South european" }, { "flag": "GRN", "nation": "Grenade", "ethnicgroup": "African" }, { "flag": "GUA", "nation": "Guatemala", "ethnicgroup": "Hispanic" }, { "flag": "GUI", "nation": "Guinée", "ethnicgroup": "African" }, { "flag": "GUM", "nation": "Guam", "ethnicgroup": "East asian" }, { "flag": "GUY", "nation": "Guyana", "ethnicgroup": "African" }, { "flag": "HAI", "nation": "Haïti", "ethnicgroup": "African" }, { "flag": "HEF", "nation": "Heffem", "ethnicgroup": "South european" }, { "flag": "HKG", "nation": "Hong Kong", "ethnicgroup": "East asian" }, { "flag": "HON", "nation": "Honduras", "ethnicgroup": "Hispanic" }, { "flag": "HUN", "nation": "Hongrie", "ethnicgroup": "North european" }, { "flag": "IDN", "nation": "Indonésie", "ethnicgroup": "East asian" }, { "flag": "IND", "nation": "Inde", "ethnicgroup": "Indian" }, { "flag": "IRL", "nation": "Irlande", "ethnicgroup": "North european" }, { "flag": "IRN", "nation": "Iran", "ethnicgroup": "Middle east" }, { "flag": "IRQ", "nation": "Irak", "ethnicgroup": "Middle east" }, { "flag": "ISL", "nation": "Islande", "ethnicgroup": "North european" }, { "flag": "ISR", "nation": "Israël", "ethnicgroup": "Middle east" }, { "flag": "ITA", "nation": "Italie", "ethnicgroup": "South european" }, { "flag": "JAM", "nation": "Jamaïque", "ethnicgroup": "African" }, { "flag": "JOR", "nation": "Jordanie", "ethnicgroup": "Middle east" }, { "flag": "JPN", "nation": "Japon", "ethnicgroup": "East asian" }, { "flag": "KAZ", "nation": "Kazakhstan", "ethnicgroup": "Middle east" }, { "flag": "KEN", "nation": "Kenya", "ethnicgroup": "African" }, { "flag": "KGZ", "nation": "Kirghizistan", "ethnicgroup": "Middle east" }, { "flag": "KOR", "nation": "Corée du Sud", "ethnicgroup": "East asian" }, { "flag": "KSA", "nation": "Arabie Saoudite", "ethnicgroup": "Middle east" }, { "flag": "KUW", "nation": "Koweït", "ethnicgroup": "Middle east" }, { "flag": "KVX", "nation": "Kosovo", "ethnicgroup": "South european" }, { "flag": "LAO", "nation": "Laos", "ethnicgroup": "East asian" }, { "flag": "LBR", "nation": "Liberia", "ethnicgroup": "African" }, { "flag": "LBY", "nation": "Libye", "ethnicgroup": "Middle east" }, { "flag": "LCA", "nation": "Sainte-Lucie", "ethnicgroup": "African" }, { "flag": "LES", "nation": "Lesotho", "ethnicgroup": "African" }, { "flag": "LIB", "nation": "Liban", "ethnicgroup": "Middle east" }, { "flag": "LIE", "nation": "Liechtenstein", "ethnicgroup": "North european" }, { "flag": "LTU", "nation": "Lituanie", "ethnicgroup": "North european" }, { "flag": "LUX", "nation": "Luxembourg", "ethnicgroup": "South european" }, { "flag": "LVA", "nation": "Lettonie", "ethnicgroup": "North european" }, { "flag": "MAC", "nation": "Macao", "ethnicgroup": "East asian" }, { "flag": "MAD", "nation": "Madagascar", "ethnicgroup": "African" }, { "flag": "MAR", "nation": "Maroc", "ethnicgroup": "Middle east" }, { "flag": "MAS", "nation": "Malaisie", "ethnicgroup": "East asian" }, { "flag": "MDA", "nation": "Moldavie", "ethnicgroup": "North european" }, { "flag": "MDV", "nation": "Maldives", "ethnicgroup": "Indian" }, { "flag": "MEX", "nation": "Mexique", "ethnicgroup": "Hispanic" }, { "flag": "MGL", "nation": "Mongolie", "ethnicgroup": "East asian" }, { "flag": "MKD", "nation": "Macédoine", "ethnicgroup": "North european" }, { "flag": "MLI", "nation": "Mali", "ethnicgroup": "African" }, { "flag": "MLT", "nation": "Malte", "ethnicgroup": "North european" }, { "flag": "MNE", "nation": "Monténégro", "ethnicgroup": "North european" }, { "flag": "MOZ", "nation": "Mozambique", "ethnicgroup": "African" }, { "flag": "MRI", "nation": "Île Maurice", "ethnicgroup": "African" }, { "flag": "MSR", "nation": "Montserrat", "ethnicgroup": "African" }, { "flag": "MTN", "nation": "Mauritanie", "ethnicgroup": "African" }, { "flag": "MWI", "nation": "Malawi", "ethnicgroup": "African" }, { "flag": "MYA", "nation": "Birmanie", "ethnicgroup": "East asian" }, { "flag": "NAM", "nation": "Namibie", "ethnicgroup": "African" }, { "flag": "NCA", "nation": "Nicaragua", "ethnicgroup": "Hispanic" }, { "flag": "NCL", "nation": "Nouvelle-Calédonie", "ethnicgroup": "Hispanic" }, { "flag": "NED", "nation": "nation-Bas", "ethnicgroup": "North european" }, { "flag": "NEP", "nation": "Népal", "ethnicgroup": "Indian" }, { "flag": "NGA", "nation": "Nigeria", "ethnicgroup": "African" }, { "flag": "NIG", "nation": "Niger", "ethnicgroup": "African" }, { "flag": "NIR", "nation": "Irlande du Nord", "ethnicgroup": "North european" }, { "flag": "NOR", "nation": "Norvège", "ethnicgroup": "North european" }, { "flag": "NZL", "nation": "Nouvelle-Zélande", "ethnicgroup": "South european" }, { "flag": "OMA", "nation": "Oman", "ethnicgroup": "Middle east" }, { "flag": "PAK", "nation": "Pakistan", "ethnicgroup": "Middle east" }, { "flag": "PAL", "nation": "Palestine", "ethnicgroup": "Middle east" }, { "flag": "PAN", "nation": "Panama", "ethnicgroup": "Hispanic" }, { "flag": "PAR", "nation": "Paraguay", "ethnicgroup": "Hispanic" }, { "flag": "PER", "nation": "Pérou", "ethnicgroup": "Hispanic" }, { "flag": "PHI", "nation": "Philippines", "ethnicgroup": "East asian" }, { "flag": "PNG", "nation": "Papouasie-Nouvelle-Guinée", "ethnicgroup": "Hispanic" }, { "flag": "POL", "nation": "Pologne", "ethnicgroup": "North european" }, { "flag": "POR", "nation": "Portugal", "ethnicgroup": "South european" }, { "flag": "PRK", "nation": "Corée du Nord", "ethnicgroup": "East asian" }, { "flag": "PUR", "nation": "Porto-Rico", "ethnicgroup": "Hispanic" }, { "flag": "QAT", "nation": "Qatar", "ethnicgroup": "Middle east" }, { "flag": "ROU", "nation": "Roumanie", "ethnicgroup": "North european" }, { "flag": "RSA", "nation": "African du Sud", "ethnicgroup": "African" }, { "flag": "RUS", "nation": "Russie", "ethnicgroup": "North european" }, { "flag": "RWA", "nation": "Rwanda", "ethnicgroup": "African" }, { "flag": "SAM", "nation": "Samoa", "ethnicgroup": "Hispanic" }, { "flag": "SCO", "nation": "Écosse", "ethnicgroup": "North european" }, { "flag": "SEN", "nation": "Sénégal", "ethnicgroup": "African" }, { "flag": "SEY", "nation": "Seychelles", "ethnicgroup": "African" }, { "flag": "SIN", "nation": "Singapour", "ethnicgroup": "East asian" }, { "flag": "SKN", "nation": "Saint-Kitts-et-Nevis", "ethnicgroup": "African" }, { "flag": "SLE", "nation": "Sierra Leone", "ethnicgroup": "African" }, { "flag": "SLV", "nation": "Salvador", "ethnicgroup": "Hispanic" }, { "flag": "SMR", "nation": "Saint-Marin", "ethnicgroup": "South european" }, { "flag": "SOL", "nation": "Îles Salomon", "ethnicgroup": "Hispanic" }, { "flag": "SOM", "nation": "Somalie", "ethnicgroup": "African" }, { "flag": "SRB", "nation": "Serbie", "ethnicgroup": "South european" }, { "flag": "SRI", "nation": "Sri Lanka", "ethnicgroup": "Indian" }, { "flag": "SSD", "nation": "Soudan du Sud", "ethnicgroup": "African" }, { "flag": "STP", "nation": "São Tomé-et-Príncipe", "ethnicgroup": "African" }, { "flag": "SUD", "nation": "Soudan", "ethnicgroup": "African" }, { "flag": "SUI", "nation": "Suisse", "ethnicgroup": "South european" }, { "flag": "SUR", "nation": "Suriname", "ethnicgroup": "African" }, { "flag": "SVK", "nation": "Slovaquie", "ethnicgroup": "North european" }, { "flag": "SVN", "nation": "Slovénie", "ethnicgroup": "North european" }, { "flag": "SWE", "nation": "Suède", "ethnicgroup": "North european" }, { "flag": "SWZ", "nation": "Swaziland", "ethnicgroup": "African" }, { "flag": "SYR", "nation": "Syrie", "ethnicgroup": "Middle east" }, { "flag": "TAH", "nation": "Tahiti", "ethnicgroup": "Hispanic" }, { "flag": "TAN", "nation": "Tanzanie", "ethnicgroup": "African" }, { "flag": "TCA", "nation": "Îles Turks-et-Caicos", "ethnicgroup": "African" }, { "flag": "TGA", "nation": "Îles Tonga", "ethnicgroup": "Hispanic" }, { "flag": "THA", "nation": "Thaïlande", "ethnicgroup": "East asian" }, { "flag": "TJK", "nation": "Tadjikistan", "ethnicgroup": "Middle east" }, { "flag": "TKM", "nation": "Turkménistan", "ethnicgroup": "Middle east" }, { "flag": "TLS", "nation": "Timor Oriental", "ethnicgroup": "East asian" }, { "flag": "TOG", "nation": "Togo", "ethnicgroup": "African" }, { "flag": "TPE", "nation": "Taipei Chinois", "ethnicgroup": "East asian" }, { "flag": "TRI", "nation": "Trinité-et-Tobago", "ethnicgroup": "African" }, { "flag": "TUN", "nation": "Tunisie", "ethnicgroup": "Middle east" }, { "flag": "TUR", "nation": "Turquie", "ethnicgroup": "Middle east" }, { "flag": "UAE", "nation": "Émirats Arabes Unis", "ethnicgroup": "Middle east" }, { "flag": "UGA", "nation": "Ouganda", "ethnicgroup": "African" }, { "flag": "UKR", "nation": "Ukraine", "ethnicgroup": "North european" }, { "flag": "URU", "nation": "Uruguay", "ethnicgroup": "Hispanic" }, { "flag": "USA", "nation": "États-Unis", "ethnicgroup": "South european" }, { "flag": "UZB", "nation": "Ouzbékistan", "ethnicgroup": "East asian" }, { "flag": "VAN", "nation": "Vanuatu", "ethnicgroup": "Hispanic" }, { "flag": "VEN", "nation": "Vénézuela", "ethnicgroup": "Hispanic" }, { "flag": "VGB", "nation": "Îles Vierges", "ethnicgroup": "African" }, { "flag": "VIE", "nation": "Vietnam", "ethnicgroup": "East asian" }, { "flag": "VIN", "nation": "Saint-Vincent", "ethnicgroup": "African" }, { "flag": "VIR", "nation": "Îles Vierges US", "ethnicgroup": "African" }, { "flag": "WAL", "nation": "nation de Galles", "ethnicgroup": "North european" }, { "flag": "YEM", "nation": "Yémen", "ethnicgroup": "Middle east" }, { "flag": "ZAM", "nation": "Zambie", "ethnicgroup": "African" }, { "flag": "ZIM", "nation": "Zimbabwe", "ethnicgroup": "African" } ]

##### Here we read the .rtf file, the double check is simply for my personal use #####
if os.path.exists(".\\Sans titre.rtf") == True:
    my_file = open(".\\Sans titre.rtf", "r+", encoding="utf8")
    lines_of_file = my_file.readlines()
elif os.path.exists(".\\Faces regens.rtf") == True:
    my_file = open(".\\Faces regens.rtf", "r+", encoding="utf8")
    lines_of_file = my_file.readlines()
else : 
    print("ERROR : THE TEXT FILE \"Faces regens.rtf\" DOES NOT EXIST, PLEASE CHECK PART 3 IN TUTORIAL")
    sys.exit()

##### Here we read the lines of the file one by one #####
for line in lines_of_file:
    ##### Here we check if the line is a player line or a unused line #####
    if line.startswith('\n') or line.startswith('| --------') or line.startswith('| IDU') or line.startswith('| UID') or line.startswith('| EID') or line.startswith('| IU') or line.startswith('| ID') or line.startswith('| ID') or line.startswith('| ÖID') or line.startswith('| ΜID') or line.startswith('| УИН') or line.startswith('| 编​号') or line.startswith('| 編​號') :
        continue
    else:
        ##### Here we search for the datas in the file .rtf #####
        infos = line[2:].split('| ')
        pID = infos[0].strip()
        ##### Here we check if the lines printed in game has the script view applied #####
        if pID.isdigit() == False:
            print("ERROR : THE TEXT FILE DOES NOT CONTAIN PLAYER LIST WITH \"Heffem Faces\" VIEW APPLICATED, PLEASE CHECK PART 3 IN TUTORIAL")
            continue
            
        ##### Here we define the datas #####
        pNAT = infos[1].strip()
        pNAT2 = infos[2].strip()
        pNAME = infos[3].strip()
        pHAIRLONG = infos[4].strip()
        pHAIRCOL = infos[5].strip()
        pSKINCOL = infos[6].strip()
        print("• "+pNAME+" - NAT : "+pNAT+' - ID : '+pID)
        
        ##### Here we check if the player is a real player or a newgen #####
        if int(pID) > 1915400000:

            ##### Here we check the ethnic group with the game ethnic value #####
            if pSKINCOL == '1':
                pETHNIC = 'Hispanic'
            elif pSKINCOL == '2':
                pETHNIC = 'Middle east'
            elif pSKINCOL == '3':
                pETHNIC = 'African'
            elif pSKINCOL == '4':
                pETHNIC = 'Indian'
            elif pSKINCOL == '5':
                pETHNIC = 'East asian'
            elif pSKINCOL == '7':
                pETHNIC = 'Hispanic'
            elif pSKINCOL == '8' :
                pETHNIC = 'Mixed'
            elif pSKINCOL == '9':
                pETHNIC = 'Mixed'
            elif pSKINCOL == '10':
                pETHNIC = 'East asian'
            ##### For europeans I applied some differences, I define the ethnic group by nation #####
            else:
                for nation in listnations:
                    if nation['flag'].upper() == pNAT:
                        pETHNIC = nation['ethnicgroup']
                        pNATION = nation['nation']
            for nation in listnations:
                if nation['flag'].upper() == pNAT:
                    pNATION = nation['nation']

            ##### Here we check the hair colour #####
            listcolour = ['Blonde','Light Brown','Dark Brown','Red','Black','Grey']
            if pHAIRCOL == '1' or pHAIRCOL == '2' or pHAIRCOL == '7' or pHAIRCOL == '8' or pHAIRCOL == '9' or pHAIRCOL == '10'  :
                pHAIRCOL2 = 'Blonde'
            elif pHAIRCOL == '3':
                pHAIRCOL2 = 'Light Brown'
            elif pHAIRCOL == '11' or pHAIRCOL == '12' :
                pHAIRCOL2 = 'Dark Brown'
            elif pHAIRCOL == '13' or pHAIRCOL == '14':
                pHAIRCOL2 = 'Red'
            elif pHAIRCOL == '5' or pHAIRCOL == '6' or pHAIRCOL == '7' or pHAIRCOL == '15' or pHAIRCOL == '16' or pHAIRCOL == '17' or pHAIRCOL == '18':
                pHAIRCOL2 = 'Black'


            ##### Here we check if the script already put a face for the player #####
            pIMGName = str(pID) + '.png'
            pIMG = ".\\Faces ethnic script\\IN GAME Faces Regens\\" + str(pID) + ".png"
            if os.path.exists(pIMG) == True:
                print('\t=> Already processed\n')
                continue

            ##### Here we pick a face for the player in the good ethnic group folder #####
            listfaces = os.listdir('.\\Faces ethnic script\\'+pETHNIC+'\\'+pHAIRCOL2)
            pCHOICEFACE = random.choice(listfaces)

            ##### Here we put the picked face in the folder and write the line for the config.xml #####
            shutil.copy(".\\Faces ethnic script\\"+pETHNIC+'\\'+pHAIRCOL2+'\\'+pCHOICEFACE,".\\Faces ethnic script\\IN GAME Faces Regens\\"+str(pID)+".png")
            line = "\t\t<record from='"+str(pID)+"' to='graphics/pictures/person/"+str(pID)+"/portrait'/>\n"
            my_file = open(".\\Faces ethnic script\\IN GAME Faces Regens\\config.xml", "r")
            config = my_file.readlines()
            config.insert(-3, line)
            my_file.close()
            my_file = open(".\\Faces ethnic script\\IN GAME Faces Regens\\config.xml", "w")
            config = "".join(config)
            my_file.write(config)
            my_file.close()

            print('\t=> Face added : '+pNAME+' - '+pNATION+' - '+pETHNIC+' - '+pHAIRCOL2+'\n')
        else:
            print('\t=> Real Player\n')

print("-------- END OF THE SCRIPT YOU CAN CLOSE IT --------")



