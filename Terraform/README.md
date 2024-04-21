#### Prérequis
- J'ai installé Terraform sur ma machine locale.
- J'ai installé et configuré Azure CLI pour accéder à mon abonnement Azure.
- Mon compte Azure dispose des permissions nécessaires pour créer et gérer des ressources.

#### Structure du Projet
Mon projet contient principalement le fichier `main.tf`, qui configure les ressources Azure suivantes :
- **Adresse IP publique (`azurerm_public_ip`)**: Crée une adresse IP publique dynamique.
- **Interface réseau (`azurerm_network_interface`)**: Configure une interface réseau pour la VM.
- **Machine Virtuelle Linux (`azurerm_linux_virtual_machine`)**: Déploie une VM utilisant une image d'Ubuntu Server.

#### Actions supplémentaires
Pour assurer la configuration correcte des ressources réseau, j'ai utilisé la commande Azure CLI suivante pour créer manuellement l'interface réseau dans le réseau virtuel spécifié :
```bash
az network nic create \
    --resource-group ADDA84-CTP \
    --name devops-20200415 \
    --vnet-name network-tp4 \
    --subnet internal
```
Cette commande a permis de s'assurer que l'interface réseau est correctement configurée et prête à être utilisée par la machine virtuelle.

#### Déroulement et Configuration
1. **Initialisation de Terraform**:
   ```bash
   terraform init
   ```
   Cette commande initialise le projet en téléchargeant les providers nécessaires.

2. **Planification des Ressources**:
   ```bash
   terraform plan
   ```
   Permet de visualiser les actions que Terraform exécutera.

3. **Application du Plan**:
   ```bash
   terraform apply
   ```
   J'ai exécuté le plan pour créer les ressources. L'étape de `terraform apply` a fonctionné avec succès, ajoutant 2 ressources et en modifiant 1, sans aucune destruction.

4. **Utilisation de Terraform Destroy**:
   Pour nettoyer l'environnement et éviter les coûts inutiles, j'ai utilisé la commande `terraform destroy`:
   ```bash
   terraform destroy
   ```
   J'ai confirmé avec 'yes' et les ressources, y compris la machine virtuelle, l'interface réseau, et l'adresse IP publique ont été détruites sans problème.


