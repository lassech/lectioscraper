# lectioscraper
Scraper lectioskema og fører det over i en google kalender
Lærere kan overføre deres skema til google kalender. 


## sådan kommer du i gang
1) Download python scriptet og gem det i en mappe som du kan huske 

## klargøring af google
1) Følg skridt 1 på denne side: 1. ) https://developers.google.com/google-apps/calendar/quickstart/python
   Det er vigtigt at client_secret.json er gemt i samme mappe som python skriptet
2) Opret en google kalender som du vil bruge til at gemme dit lectio skema i.
3) Find calenderid. Det skal du bruge senere. https://docs.simplecalendar.io/find-google-calendar-id/

## Python
1) Du skal downloade python 3 fra pythons hjemmeside. https://www.python.org/
   Det er vigtigt at det er version 3, da man ikke kan være sikker på at version virker.
2) Når python er installeret skal, du åbne en terminal. På windows åbnes den ved at trykke windowstast + r, skriv cmd og tryk enter.
   Her skal du installere en række biblioteker som får scriptet til at virke. Det gøres ved at skrive følgende efterfulgt af enter: 
  "pip install --upgrade requests bs4 httplib2 apiclient oauth2client google-api-python-client datetime argparse"
3) så skal du åbne lectio.py i en teksteditor. Notepad kan bruges, men du kan også vælge at downloade en mere avanceret. Fx                    https://atom.io/
4) Gå til 29-39. Her skal du definerer skoleid, lærerid, uger og c_id. Der står i boksen, hvad der skal indsættes.
5) I din terminal skriver går du hen til din mappe og skriver python lectio.py.
6) Nu burde lectioskemaet eksporteres til din google kalender.  