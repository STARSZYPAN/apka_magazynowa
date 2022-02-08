
user_choice = -1

names=[]

quantitys=[]

units=[]

prices=[]






print("Co chcesz teraz zrobić?: ")

def show_produkt():   
    names_index=0
    for name in names:
        print(name + "["+ str(names_index) + "]")
        names_index += 1
  
    
        
def add_produkt():
        name=input('Wpisz nazwę produktu:  ')
        names.append(name)
        print('Dodano produkt')
#def add_quantity():
        #quantity=input('Wpisz ilość produktu:  ')
        #quantitys.append(quantity)
        #print('Dodano ilość produktu')
#def add_unit():
        #unit=input('Wpisz jednostkę  miary produktu:  ')
        #units.append(unit)
        #print('Dodano jednostkę miary')
#def add_price():
        #price=input('Wpisz cenę produktu:  ')
        #price.sappend(price)
        #print('Dodano cenę')

def delete_produkty():
    produkt_index = int(input('Podaj indeks produktu do usunięcia:'))

    if produkt_index <0 or produkt_index > len(names) -1:
        print('produkt o tym indeksie nie istnieje')
        return

    names.pop(produkt_index)
    print('Usunięto produkt')

def save_produkt_to_file():
    file = open('produkty.txt' , 'w')

    for name in names:2

    file.write(name + "\n")
    file.close()

def load_produkty_from_file():
    try:

        file = open ('produkty.txd')

        for line in file.readlines():
           names.append(line.strip())

        file.close()

    except FileNotFoundError:
        return
def dowidzenia():
    exit
load_produkty_from_file()




while user_choice !=5:
    if user_choice==1:
        
        print("Name\tQuantity\tUnit\tUnit Price (PLN)\tIndex")
        print("----\t--------\t----\t----------------\t------")
        show_produkt()

    if user_choice==2:
        add_produkt()

    if user_choice==3:
        delete_produkty()

    if user_choice==4:
       save_produkt_to_file()
    
    if user_choice==5:
       dowidzenia()
    
    



    print()
    print('1.Pokaz towary')
    print('2.Dodaj towary')
    print('3.Usuń towary')
    print('4.Zapisz zmiany w magazynie')
    print('5.Wyjdź')

    user_choice=int(input('Wybierz operację: '))
    print()
