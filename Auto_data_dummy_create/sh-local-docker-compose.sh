sudo  chmod -R 777  /var/run/docker.sock
docker-compose -f local-docker-compose.yml up

# docker exec -it dsfm_general_backend  bash -c "python manage.py showmigrations"
# docker exec -it dsfm_general_database bash
# docker exec -it dsfm_general_phpmyadmin bash