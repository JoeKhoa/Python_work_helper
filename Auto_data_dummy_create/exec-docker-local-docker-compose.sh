# docker exec -it dsfm_general_backend  bash 


# docker exec -it dsfm_general_backend  bash -c "python manage.py showmigrations"
docker exec -it dsfm_general_backend  bash -c " python manage.py load_items"


# from django.contrib.auth.models import User
# my_admin = User.objects.create_superuser('admin', 'admin@test.com','admin@123')
# python manage.py shell -c "from django.contrib.auth.models import User ; my_admin = User.objects.create_superuser('admin2', 'admin2@test.com','admin2@123')" 
# python manage.py shell -c "from django.contrib.auth.models import User ; my_admin = User.objects.create_superuser('admin', 'admin@test.com','admin@123')"
# python manage.py shell -c "from django.contrib.auth.models import Employee ; my_admin = User.objects.create(username='field', password='field@123', role='FIELD')"