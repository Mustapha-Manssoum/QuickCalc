# QuickCalc / CICD
QuickCalc is a lightweight web-based calculator built with **Python**, containerized using **Docker**, and deployed on **Kubernetes** via **GitHub Actions** and **ArgoCD**.

# Install ArgoCD
```
helm repo add argo https://argoproj.github.io/argo-helm   
helm repo update
kubectl create namespace argocd
helm install argocd argo/argo-cd --namespace argocd
```

# Apply ArgoCD Application
```
kubectl apply -f argocd-application.yaml
```

# Access ArgoCD UI
```
kubectl port-forward service/argocd-server -n argocd 9090:443
```

# 🔐 Retrieve ArgoCD Admin Password
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```
# Creating Image Pull Secrets (for GHCR)
To allow Kubernetes to pull images from GitHub Container Registry:
```
kubectl create secret docker-registry ghcr-secret --docker-server=ghcr.io --docker-username=YOUR_USERNAME --docker-password=YOUR_PAT --namespace=default
```

# Access QuickCalc app in Kubernetes
```
kubectl port-forward svc/quick-calc-service 8080:8080
```

# 🧹 Cleanup
```
helm uninstall argocd -n argocd
kubectl delete ns argocd
kubectl delete deployment,svc quick-calc
```
