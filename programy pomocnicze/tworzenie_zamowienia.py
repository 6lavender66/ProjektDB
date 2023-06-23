from pymongo import MongoClient

client = MongoClient('mongodb+srv://Admin:root@siec.hhe2wbq.mongodb.net/') # konto: 'Admin' Hasło: 'root'
db = client['Kiosk']

kolekcja_klienci = db['klienci']
kolekcja_produkty = db['produkty']
kolekcja_zamowienia = db['zamowienia']

# Tworzenie zamówienia
def utworz_zamowienie(klient_id, produkt_id):
    zamowienie = {
        'klient': klient_id,
        'produkt': produkt_id
    }
    zamowienie_id = kolekcja_zamowienia.insert_one(zamowienie).inserted_id
    return zamowienie_id

#tutaj powinno być zautomatyzowane pobieranie ze strony jaki użytkownik co zarobił, program uprosczony D: 

klient_id = ''  
produkt_id = ''  
nowe_zamowienie_id = utworz_zamowienie(klient_id, produkt_id)

'''
# Przykład tworzenia zamówienia
klient_id = 'id_klienta'  # Pobierz odpowiednie ID klienta
produkt_id = 'id_produktu'  # Pobierz odpowiednie ID produktu
nowe_zamowienie_id = utworz_zamowienie(klient_id, produkt_id)

'''
