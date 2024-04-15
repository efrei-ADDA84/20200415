# Rapport

Dans le cadre de notre projet, nous avons opté pour l'utilisation du framework Flask en Python pour créer une API, avec le fichier `app.py` servant de point d'entrée.

Pour assurer la portabilité et la gestion des dépendances, nous avons créé un fichier `requirements.txt` contenant les dépendances nécessaires, et nous avons utilisé un environnement virtuel Python via `.venv`.

Pour faciliter le déploiement et l'exécution de notre application, nous avons mis en place un fichier `Dockerfile`. Ce fichier spécifie la version de Python requise, installe les dépendances à partir du fichier `requirements.txt` et définit la commande à exécuter pour démarrer le service.

La démarche de déploiement commence par une connexion à Docker via la commande `docker login`, suivie de la création de l'image Docker à l'aide de `docker build`. Pour rendre cette image accessible à d'autres utilisateurs, nous l'avons poussée vers Docker Hub avec `docker push`. Nous avons également étiqueté cette image avec une version spécifique.

Une fois l'image disponible sur Docker Hub, elle peut être lancée à l'aide de la commande `docker run`, où des variables d'environnement telles que `API_KEY` peuvent être configurées selon les besoins.

Pour automatiser ce processus, nous avons configuré un workflow GitHub Action nommé `docker-image.yml`. Ce workflow est déclenché à chaque nouveau commit et se charge de construire et de pousser l'image Docker vers Docker Hub.

Pour garantir la sécurité des informations sensibles, telles que les identifiants de connexion à Docker, nous avons utilisé les secrets du repository GitHub. Ces secrets sont intégrés au workflow GitHub Action et permettent une connexion automatisée à Docker sans compromettre la sécurité.
