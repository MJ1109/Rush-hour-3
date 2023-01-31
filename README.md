# Rush-hour-3
Voor het vak Algoritmen en Heuristieken was het de bedoeling dat wij in een team van drie personen een casus oplossen aan de hand van een algoritme en heuristieken. 
De casus die wij hebben gekozen heet **Rush Hour** en is gebaseerd op een bord spelletje met dezelfde naam:

<img src="https://denkspellenparadijs.nl/837-thickbox/rush-hour2x.jpg" width="400" height="400" alt="Rush hour spel"/>

[Rush Hour game](https://www.thinkfun.com/) 

## Doel van het spel
Het doel van het spel is om de weg vrij te maken voor de rode auto, zodat deze een vrije doorgang heeft naar de uitgang. Hierbij is de uitdaging dat de wagens die de weg versperren niet van directie mogen veranderen. Dit betekend dat ze of  horizontaal of verticaal mogen bewegen. De wagens bestaan uit auto's en vrachtwagens. De vrachtwagens nemen drie blokjes in beslag, de auto's maar twee.

## De opdracht 
De opdracht bevat meerdere boards om op te lossen. Hierbij variëren de bord groottes van 6x6 (standaard) naar 9x9 en zelfs 12x12. Hierbij is het zelfs mogelijk om een custom board in te kunnen laden, mocht dat gewenst zijn. 
De boards zijn allemaal op dezelfde manier opgebouwd:
+ Een vierkant bord
+ Auto's en vrachtwagens 
    + Het type voertuig wordt bepaald aan de hand van de lengte (length = 2 is auto en length = 3 is een vrachtwagen)
+ De voertuigen bezitten allemaal een oriëntatie 'H' of 'V' (horizontaal of vertivaal)
+ De rode auto wordt aangegeven met de letter 'X'
+ Het veld is opgebouwd in een tabel. 
    + De bovenste linker hoek is aangegeven met positie (1, 1)

Het doel van de opdracht is om door middel van algoritmes het spel zo snel mogelijk op te lossen. De algoritmes mogen zelf uitgekozen worden. 

## Bestanden
In deze repository zijn een aantal bestanden de vinden: 
+  **Classes** 
    + Een map met daarin de gameboards. Hierin zitten de speelborden die opgelost dienen te worden. 
    + Een cars file met daarin de Cars class, dit bestand laadt de auto's in
    + Een board file met daarin de Board class. Dit bestand maakt het speelbord aan en laadt de auto's hierop in. 
    + Een queue file waarin de stappen worden bijgehouden

+  **Algoritmes**
    + De baseline: hierin is een random algoritme te vinden. 
    + Het breadth first algoritme: hierin is het breadth first algoritme te zien
    + Het best first algoritme: hier is de implentatie van het best first algoritme te vinden. 

## Libraries
Om de code in deze repository werkend te krijgen zijn er een aantal libraries nodig die dankzij PyPi gemakkelijk te installeren zijn met de volgende commando's: 

+ Matplotlib 
    ```
    install -U matplotlib
    ```
+ Pandas 
    ```
    pip install pandas
    ```
+ Numpy
    ```
    pip install numpy
    ```

## Gebruik
De code kan gerund worden door het volgende commando uit te voeren: 

     python3 main.py Rushhour6x6_1.csv
    
## Auteurs
+ Amy Oppong 11201061
+ Manuja Jaggan 14736950
+ Zoëy Zorgvol 12212563
