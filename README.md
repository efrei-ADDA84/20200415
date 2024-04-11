# RAPPORT :

Fonctionnalité :
En Python, une fonction appelée get_weather est créée pour interroger l'API openweathermap en utilisant les coordonnées de longitude et de latitude. Ensuite, une fonction principale, main, est créée pour appeler cette fonction avec les paramètres requis et renvoyer les données météorologiques.

Configuration requise et environnement virtuel :
Un fichier requirements.txt est généré pour lister les dépendances utilisées, et un environnement virtuel Python est configuré à l'aide de .venv.

Dockerfile :
Un fichier Dockerfile est ensuite créé pour spécifier la version de Python, installer les dépendances à partir de requirements.txt à l'aide de pip, et indiquer la commande à exécuter pour démarrer l'application.

Connexion à Docker :
La connexion à Docker est établie à l'aide de la commande docker login.

Création de l'image Docker :
L'image Docker est construite à l'aide de la commande docker build, avec une étiquette spécifique.

Publication de l'image sur Docker Hub :
L'image Docker est mise à disposition sur Docker Hub en utilisant la commande docker push.

Démarrage de l'image :
Enfin, l'image Docker est lancée en utilisant docker run avec les variables d'environnement nécessaires pour spécifier la latitude, la longitude et la clé d'API.
