# Checkpoint 3 Python Flask correction and deploy



# Introduction

Voici venu le moment du 3ème checkpoint.

- - -

C'est un point d'étape qui a pour principal objectif de **vérifier si tu as bien assimilé les compétences vues jusqu'à présent**.

Tu vas travailler sur un projet Python Flask, accompagné d'une infrastructure gérée avec OpenTofu et Ansible.

---

# 🤓 Objectifs

✅ Valider les compétences acquises durant ces dernières semaines de formation :

- Utiliser OpenTofu pour créer un conteneur LXC ;
- Utiliser Ansible pour configurer ce conteneur ;
- Déployer une application Python Flask ;
- Corriger des bugs sur un projet Flask pour le rendre fonctionnel ;
- Intégrer le projet Flask dans un pipeline CI/CD GitLab ;

🎯 Compétences du titre évaluées

- [ ] Automatiser la création de serveurs à l'aide de scripts
- [ ] Automatiser le déploiement d'une infrastructure
- [ ] Sécuriser l'infrastructure
- [ ] Mettre l'infrastructure en production dans le cloud
- [ ] Préparer un environnement de test
- [ ] Gérer des containers
- [ ] Automatiser la mise en production d'une application avec une plateforme
- [ ] Définir et mettre en place des statistiques de services
- [ ] Exploiter une solution de supervision

---

# 💪 Challenge

## Contexte

L'entreprise "Wild DevOps School" (WDS), spécialisée dans la formation et l'accompagnement en DevOps, connaît une croissance rapide. 

Afin de mieux gérer ses ressources d'infrastrcture, l'équipe a décidé de développer une application interne pour inventorier et suivre l'état des serveurs utilisés pour les formations et projets clients.

Une ébauche du projet a été entamé sur le framework Python Flask mais celle-ci contient des bugs et ne répond pas encore complètement aux besoins. 

De plus, le processus de déploiement et de maintenance de l'application n'est pas encore automatisé.

En tant que membre de l'équipe DevOps, tu es chargé·e de :

- Assurer la correction des bugs du projet Flask afin qu’il fonctionne comme prévu :

- Automatiser le déploiement et les tests à l'aide d'outils comme GitLab CI/CD et Ansible :

- Préparer un pipeline de déploiement incluant la création et la configuration du conteneur ;
  - Configurer le serveur avec les dépendances nécessaires à l'application ;
  - Tester l'application via un processus automatisé.
  - Intégrer des outils de supervision pour garantir la visibilité sur l'état du conteneur hébergeant l'application.

Le tout doit être sécurisé.

Concernant l'application, à terme celle-ci doit permettre de gérer l'inventaire des serveurs (ajouter, modifier, supprimer et consulter les serveurs).

Certains bugs empêchent le bon fonctionnement de la version fournie. À toi de les identifier et de les corriger.

Pour que les membres de l'équipe puisse la tester, l'application doit être déployée sur un conteneur LXC accessible localement depuis le serveur de l'entreprise nommé "wcs-cyber-node01".

## Requirements 

- Projet à cloner et à utiliser pour envoyer tes réponses : [checkpoint-3-python-flask-correction-and-deploy](https://gl.wilders.dev/checkpoint/checkpoint-3-python-flask-correction-and-deploy)
- python3 venv
- flask
- opentofu
- provider bpg/proxmox
- ansible

---

## Partie 1 : Préparer l'environnement OpenTofu

### 1.1 Installer et configurer OpenTofu

- Installer OpenTofu sur ton système ;
- Créer un conteneur LXC sur le serveur "wcs-cyber-node01" tournant sous Debian 12.

---

## Partie 2 : Configurer le conteneur avec Ansible

### 2.1 Installer les dépendances

- Configurer un inventaire pour le conteneur LXC ;
- Installer Python et ses dépendances pour Flask ;
- Installer Docker et ses dépendances ; 
- Préparer un scénario de test avec Molecule

---

## Partie 3 : Déboguer le projet Flask

### 3.1 Analyse des bugs

- Télécharge le projet fourni ;
- Identifie les problèmes dans le code.

### 3.2 Corriger les bugs

- Corrige les erreurs pour que le projet fonctionne ;
- Teste les fonctionnalités (ajouter, modifier, supprimer un serveur).

---

## Partie 4 : Pipeline GitLab

### 4.1 Automatiser les tests et le déploiement

- Écris un pipeline GitLab CI/CD pour :
  - Tester le projet ;
  - Construire et publier une image Docker ;
  - Déployer l'image sur le conteneur LXC.

---

## Partie 5 : Livrables

- Dépôt Git contenant le projet corrigé ;
- Captures d'écran des résultats fonctionnels ;
- Pipeline CI/CD fonctionnel.

