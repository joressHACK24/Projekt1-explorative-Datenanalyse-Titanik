# Titanic Exploratory Data Analysis (EDA)

## Projektübersicht
Dieses Projekt umfasst eine detaillierte explorative Datenanalyse (EDA) des bekannten Titanic-Datensatzes von Kaggle. Ziel war es, die Daten zu bereinigen, fehlende Werte zu behandeln und durch fundierte visuelle Analysen verborgene Muster aufzudecken, um die Überlebenswahrscheinlichkeit der Passagiere zu verstehen. Dieses Projekt ist Teil meiner Entwicklung zum AI/ML Engineer.

## Tech Stack
* **Programmiersprache:** Python 3
* **Datenmanipulation & Cleaning:** Pandas, NumPy
* **Datenvisualisierung:** Matplotlib, Seaborn

## Die 5 wichtigsten Erkenntnisse meiner Analyse

Basierend auf 10 detaillierten Visualisierungen konnten folgende Schlüsse gezogen werden:

1. **Geschlecht und Klasse als Hauptfaktoren:** Frauen hatten eine signifikant höhere Überlebensrate als Männer. Unter den weiblichen Überlebenden befanden sich größtenteils Passagierinnen der 1. und 2. Klasse. Die Korrelations-Heatmap bestätigt, dass das Geschlecht ("Sex") der stärkste Prädiktor für das Überleben ist.
2. **Altersstrukturen ("Women and children first"):** Kleinkinder wiesen im Verhältnis zu ihrer Anzahl an Bord eine sehr hohe Überlebensrate auf. Die Altersgruppe der 20- bis 30-Jährigen verzeichnete hingegen absolut gesehen die meisten Todesfälle, was darauf hindeutet, dass junge Erwachsene und ältere Menschen geringere Chancen hatten.
3. **Wirtschaftlicher Status und Einschiffungshafen:** Passagiere mit sehr günstigen Tickets (0$ - 25$) wiesen die höchste Sterblichkeitsrate auf. Ein Großteil der Überlebenden stammte aus der Ticket-Kategorie 25$ - 50$. Zudem zeigt sich, dass Passagiere, die in Cherbourg eingeschifft sind, die höchsten Überlebenschancen hatten. Dies korreliert stark mit der Tatsache, dass in Cherbourg die teuersten Tickets gekauft wurden (überwiegend 1. Klasse).
4. **Extreme Preisschwankungen in der 1. Klasse:** Bei den Ticketpreisen der 1. Klasse gibt es enorme Schwankungen und Ausreißer. Dies deutet analytisch auf Sammelbuchungen für Familien oder Rabattaktionen hin.
5. **Einfluss der Begleitung:** Interessanterweise hatte die Tatsache, ob jemand alleine reiste (ohne registrierte Verwandte), keinen zwingend negativen Einfluss auf die Überlebenschancen. Über 280 Alleinreisende konnten gerettet werden.

## Key Visualisierungen
*(Hier ist ein Beispiel meiner Datenvisualisierung. Das vollständige Set von 10 Plots befindet sich hier).*

![Titanic Datenvisualisierung](https://github.com/joressHACK24/KIingenieur-/blob/f7a0a993cee4094595ec7295da1ea2bd11b24117/Projekt1-Explorative%20DatenAnalyse/visualisierung_dataset_titanik.png)

## Lokale Ausführung
Um dieser Skript lokal auszuführen:
1. Repository klonen: `git clone https://github.com/joressHACK24/KIingenieur-.git`
2. Abhängigkeiten installieren: `pip install pandas numpy matplotlib seaborn`
