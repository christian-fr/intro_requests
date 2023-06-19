Folgenden Befehl ausführen, um die beiden requirements (benötigte Software-Pakete) zu installieren: 

`$ python3 -m pip install -r requirements.txt`

Dann noch eine Datei `.env` im root-Verzeichnis des Projekts (dort, wo auch diese README.md-Datei liegt) anlegen und mit folgendem Inhalt füllen:

```
ACCESS_TOKEN=<mastodon api access token>
OPENWEATHERMAP_TOKEN=<openweathermap api access token>
LAT=<latitude>
LON=<longitude>
```


