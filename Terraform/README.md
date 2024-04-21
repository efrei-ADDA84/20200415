#### Prérequis
- J'ai installé Terraform sur ma machine locale.
- J'ai installé et configuré Azure CLI pour accéder à mon abonnement Azure.
- Mon compte Azure dispose des permissions nécessaires pour créer et gérer des ressources.

#### Structure du Projet
Mon projet contient principalement le fichier `main.tf`, qui configure les ressources Azure suivantes :
- **Adresse IP publique (`azurerm_public_ip`)**: Crée une adresse IP publique dynamique.
- **Interface réseau (`azurerm_network_interface`)**: Configure une interface réseau pour la VM.
- **Machine Virtuelle Linux (`azurerm_linux_virtual_machine`)**: Déploie une VM utilisant une image d'Ubuntu Server.

Pour assurer la configuration correcte des ressources réseau, j'ai utilisé la commande Azure CLI suivante pour créer manuellement l'interface réseau dans le réseau virtuel spécifié :

#### Déroulement et Configuration
1. **Initialisation de Terraform**:
   terraform init

   Cette commande initialise le projet en téléchargeant les providers nécessaires.

2. **Planification des Ressources**:
   terraform plan

   Permet de visualiser les actions que Terraform exécutera.

3. **Application du Plan**:
   terraform apply

   J'exécute le plan pour créer les ressources. Les ressources pour l'adresse IP publique et l'interface réseau sont créées sans problème.

#### Problèmes rencontrés
Lors de la création de la machine virtuelle, j'ai rencontré un problème :

**Erreur rencontrée**:
```plaintext
Error: creating Linux Virtual Machine (Subscription: "765266c6-9a23-4638-af32-dd1e32613047"
Resource Group Name: "ADDA84-CTP"
Virtual Machine Name: "devops-20200415"): performing CreateOrUpdate: unexpected status 404 (404 Not Found) with error: PlatformImageNotFound: The platform image 'Canonical:UbuntuServer:22.04-LTS:latest' is not available. Verify that all fields in the storage profile are correct. For more details about storage profile information, please refer to https://aka.ms/storageprofile
```

Le processus est bloqué à la création de la machine virtuelle à cause d'une erreur indiquant que l'image spécifiée de `Ubuntu Server 22.04-LTS` n'est pas disponible. Je dois vérifier l'image utilisée et m'assurer que les spécifications correspondent à celles disponibles dans ma région Azure ou choisir une autre image compatible.
