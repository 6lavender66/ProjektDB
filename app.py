#Aplikacja umożliwia dodawanie klientów sklepu internetowego do bazy danych MongoDB. 

### UWAGA ###
# prosze przeczytać plik README w venu 

from flask import Flask, render_template, request                          
from pymongo import MongoClient                                             

# Inicjacja obiektu aplikacji Flask.                                                             
app = Flask(__name__)                                                 
# Połączenia z klastrem za pomocą "connection string into your application code" 
client = MongoClient('mongodb+srv://Admin:root@siec.hhe2wbq.mongodb.net/') # konto: 'Admin' Hasło: 'root'
db = client['Kiosk']                                                            
kolekcja = db['klienci_aplikacja']

# Dekorator? odpowiada za / 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pobieranie danych z formularza i tworzenie dokumentu klienta
        klient = {
            'imie': request.form['imie'],
            'nazwisko': request.form['nazwisko'],
            'email': request.form['email']
        }
        # Dodawanie dokumentu klienta do kolekcji "klienci_aplikacja"
        klient_id = kolekcja.insert_one(klient).inserted_id
        return f'Dodano klienta o ID: {klient_id}'

    # Renderowanie szablonu "index.html" w przypadku metody GET
    return render_template('index.html')

# Warunek sprawdzający, czy skrypt jest uruchamiany 
if __name__ == '__main__':
    # Uruchamianie aplikacji Flask w trybie debugowania (jeżli warunek wyżej spełniony)
    app.run(debug=True)                                                      



'''
Dokumentacja kodu aplikacji Flask dla dodawania klientów do bazy danych MongoDB

    Nazwa modułu: app.py

    Opis:

Moduł app.py zawiera kod aplikacji internetowej napisany we frameworku Flask Pythona. 
Aplikacja łączy się z bazą danych MongoDB za pomocą biblioteki pymongo. 
Pozwala dodawać klientów do bazy poprzez formularz na stronie głównej.

    Struktura kodu:

-Importuj wymagane moduły i biblioteki
-Inicjalizacja obiektu aplikacji Flask
-Utwórz połączenie z bazą danych MongoDB
-Utwórz odwołanie do kolekcji w bazie danych
-Definicja funkcji obsługującej endpoint '/'
-Uruchom aplikację w trybie debugowania

    Endpointy:

„/”: strona główna, dostępna dla metod GET i POST. 
Dla metody GET wyświetla formularz dodawania klienta. 
Dla metody POST pobiera dane z formularza, tworzy dokument klienta i dodaje go do kolekcji w bazie danych.

    Zależności:

Flask: Framework do budowania aplikacji internetowych w Pythonie.

Pymongo: biblioteka do pracy z MongoDB w Pythonie.

    W razie problemów:

- Należy mieć zainstalowane sterowniki Flask oraz Pymongo.
- Uruchom skrypt app.py przy użyciu interpretera języka Python,
ja używałem osobiście Visal Studio Code, powinno działać na innych

Aplikacja będzie obsługiwana na http://localhost:5000/ lub http://127.0.0.1:5000/
'''
