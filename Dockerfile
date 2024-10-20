# Utiliser l'image officielle de PostgreSQL
FROM postgres:14

# Configuration des variables d'environnement pour Postgres
ENV POSTGRES_DB=spotify
ENV POSTGRES_USER=modeste
ENV POSTGRES_PASSWORD=Hunter15@gdd.tg

# Exposer le port par défaut de PostgreSQL
EXPOSE 5432

# Commande pour démarrer PostgreSQL (c'est la commande par défaut pour l'image postgres)
CMD ["postgres"]