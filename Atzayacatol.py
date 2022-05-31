from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import load_workbook
import webbrowser

print("Atzayacatol v1 \n ( ͡° ͜ʖ ͡°) \n ")

def menu():
    print("1. Web Scrap HP")
    print("2. Musiquita")
    print("3. BTC Price")
    print("4. Salir")
    
menu()

option = int(input("Selecciona tu destino \n"))

while option != 4:
    if option ==1:
#variables para las urls
        CC = input("Saca CC:\n")
        OID = input("Saca OID:\n")
        urlC = "https://www.hp.com/"+CC +"/products/printers/product-details/product-specifications/"+OID
        urlACC = "https://www.hp.com/"+CC +"/products/printers/product-details/"+OID
        specs = requests.get(urlC)
        acc = requests.get(urlACC)
        print("Product Catalog URL: "+urlC)
        print("Accesories URL: "+urlACC)
#scrappy
        soup = BeautifulSoup(specs.content, "html.parser")
        soup3 = BeautifulSoup(acc.content, "html.parser")

#assign
        container = soup.find_all("th", class_="c-product-all-details-table__th h5")
        espec = soup.find_all("td", class_="c-product-all-details-table__td h5 m-text-rte")
        acc = soup3.find_all("h4", class_="c-product-accessory__name")

#crea dataframes
        specsDF = pd.DataFrame({"Container" : container, "Value" : espec})
        accDF = pd.DataFrame({"Accesorios" : acc})

#reporting
        reporte = input("Quieres reporte en excel? y/n ")
        if reporte == "y":
            specsDF.to_csv("export.csv", index=False)
            accDF.to_csv("export2.csv", index=False)
    
    #limpia DF1
            a_file = open("export.csv", "r", encoding='utf8')
            lines = a_file.readlines()
            a_file.close()
            new_file = open("export.csv", "w", encoding='utf8')
            for line in lines:
                    line=BeautifulSoup(line, "lxml").text
                    new_file.write(line)
            new_file.close()
    
    #limpia DF2
            a_file2 = open("export2.csv", "r", encoding='utf8')
            lines2 = a_file2.readlines()
            a_file2.close()
            new_file2 = open("export2.csv", "w", encoding='utf8')
            for line2 in lines2:
                line2=BeautifulSoup(line2, "lxml").text
                new_file2.write(line2)
            new_file2.close()
    
    #pasa a xlsx
            read_file = pd.read_csv (r'export.csv')
            read_file.to_excel (r'chido.xlsx', index = None, header=True)
    
    #agrega el sheet de accesorios
            book = load_workbook("chido.xlsx")
            writer = pd.ExcelWriter("chido.xlsx", engine = 'openpyxl')
            writer.book = book
            accDF.to_excel(writer, sheet_name = 'Top Accesorios')
            writer.save()
            writer.close()

        else:
            print("no report")
        
    
    elif option ==2:
        webbrowser.open('https://www.youtube.com/watch?v=zUovVSnhEU0')
        break
    
    elif option ==3:
        

        break
    
     
    else:
        print("Error: opcion invalida")
        break
print("Toma agua, bye")

        