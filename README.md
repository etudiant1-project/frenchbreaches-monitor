# frenchbreaches-monitor

Conteneur de monitoring simple qui vérifie un frenchbreaches.com pour un nom de domaine donné et retourne un code de sortie.

# Construction de l’image

docker build -t breach-monitor:1.0 .

# Charger l’image dans Minikube

minikube image load breach-monitor:1.0

# Déployer le Pod

kubectl apply -f pod.yaml

# Consulter les logs

kubectl logs breach-monitor
