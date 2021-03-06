# LectioScraper
LectioScraper opsamler dit lectioskema og fører det over i en google kalender.
Undervisere kan hermed overføre deres skema til en google kalender, der let kan deles med andre. 


## update 09.04.2018.
Har du brugt lectioScraper før denne dato, kan det være en idé at oprette en ny kalender eller slette alle kommende aktiviteter. Da der ellers vil kunne forekomme dobbelte aktiviteter. Har du oplevet problemer med aktiviteter som fyldte flere dage, er dette nu rettet.

## Sådan kommer du i gang
1) Download python scriptet, og gem det i en mappe, som du kan huske. Det er filen LectioScraper.py

## Klargøring af google
1) Følg skridt 1 på denne side: https://developers.google.com/google-apps/calendar/quickstart/python
   Det er vigtigt, at client_secret.json er gemt i samme mappe som python skriptet
2) Opret en google kalender, som du vil bruge til at gemme dit lectio skema i. 
3) Find calenderid. Det skal du bruge senere. https://docs.simplecalendar.io/find-google-calendar-id/

## Python
1) Du skal downloade python 3 fra pythons hjemmeside. https://www.python.org/
   Det er vigtigt at det er version 3, da man ikke kan være sikker på at version 2 virker.
   Husk at krydse Add Python to environment variables af
2) Når python er installeret, skal du åbne en terminal. På windows åbnes den ved at trykke windowstast + r, skriv cmd og tryk enter.
   Her skal du installere en række biblioteker som får scriptet til at virke. Det gøres ved at skrive følgende efterfulgt af enter: 
  "pip install --upgrade requests beautifulsoup4 bs4 httplib2 apiclient oauth2client google-api-python-client datetime argparse lxml"
  Du kan godt copypaste i terminalen.
   - Det kan være nødvendigt at eksekere cmd som administrator. Tryk windows startmenu. Søg på kommandoprompt - højreklik herpå og tryk kør     som administrator. 
3) så skal du åbne lectio.py i en teksteditor. Notepad kan bruges, men du kan også vælge at downloade en mere avanceret. Fx                    https://atom.io/
4) Gå til linje 29-39. Her skal du definere skoleid, lærerid, uger og c_id. Der står i boksen, hvad der skal indsættes.
5) I din terminal skriver, går du hen til din mappe og skriver "python LectioScraper.py" efter fulgt af enter. På windows kan du gå hen til     din mappe ved at skrive fx "cd c:\LectioScraper\"
   Første scriptet eksekveres skal du godkende det i din google calender.
6) Nu burde lectioskemaet eksporteres til din google kalender.  
   Eksekver gerne scriptet en gang om dagen eller når du ved at har været store ændringer i dit lectioskema.

## Bat fil
For at gøre programmet lettere at eksekvere i windows, kan du lave en bat fil. 

1) I mappen er der et eksempel som du kan downloade og tilpasse (ls.bat). 
2) Den første linje skal ændres fra ”cd C:\Users\rklc\Dropbox\LectioScraper” til ”cd ’mappen med python scriptet’”
3) Nu burde du kunne klikke på bat-filen og programmet burde køre.
