# Cài đặt dự án ở local


## Chuẩn bị
```bash
# Tạo local .env file
cp local.env .env
```
Khi chạy docker-compose bị **lỗi volume**, thì chạy:
```bash
sh local_run_create_host_vol
```


## Cài đặt
Cấu trúc file local
```
|- local_readme.md
|- local_run_create_host_vol
|- local-docker-compose.yml
|- local.env
```
**PHẢI** cài đặt lại port cho mỗi máy dev `.env` file, để tránh bị đụng port dưới máy của mỗi bạn.
```js
// Example 
# Start config DEV
API_HOST_PORT=7010
DB_HOST_PORT=9821
REDIS_HOST_PORT=6379
PHPMYADMIN_HOST_PORT=9822
# /End config DEV
```


## Chạy docker
```bash
# build image (chạy lần đầu tiên)
docker-compose -f local-docker-compose.yml build
# start container
docker-compose -f local-docker-compose.yml up

#Nếu bị lỗi permision denied file gunicorn_run
ERROR: Cannot start service api: OCI runtime create failed: container_linux.go:349: starting container process caused "exec: \"./gunicorn_run\": permission denied": unknown
ERROR: for api  Cannot start service api: OCI runtime create failed: container_linux.go:349: starting container process caused "exec: \"./gunicorn_run\": permission denied": unknown
ERROR: Encountered errors while bringing up the project.
#Chạy lệnh:
chmod 744 gunicorn_run
```



List **container name**:
* `dsfm_general_backend`
* `dsfm_general_celery`
* `dsfm_general_database`
* `dsfm_general_redis`
* `dsfm_general_phpmyadmin`

URLs:
```bash
# backend
    http://localhost:7010/
# phpmyadmin 
    http://localhost:9822/
```

Lệnh truy cập vào các container:
```bash 
# Script:
    docker exec -it <container-name> bash
# ex:
# backend container
    docker exec -it dsfm_general_backend bash
# database container
    docker exec -it dsfm_general_database bash
# phpmyadmin container
    docker exec -it dsfm_general_phpmyadmin bash
```


## Setup database
```bash
# Console container: dsfm_general_database
docker exec -it dsfm_general_database bash
```
Account login (user | password): root | root@123
#### Exec MySQL
```bash
mysql -u root -p
type password: # type root-password
```
* Exit MySQL: Type `exit;` and Enter
#### Create database (optional)
```sql
DROP DATABASE dsfm_general;
CREATE DATABASE dsfm_general CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
#### Create user (optional)
```sql
GRANT ALL ON dsfm_general.* TO 'dsfm_general'@'%' IDENTIFIED BY 'dsfm_general@123';
FLUSH PRIVILEGES;
```
#### SQL Dump Import
Copy file SQL to `/vol_sync/mysql/scripts`.
```sql
DROP DATABASE dsfm_general;
CREATE DATABASE dsfm_general CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL ON dsfm_general.* TO 'dsfm_general'@'%' IDENTIFIED BY 'dsfm_general@123';
FLUSH PRIVILEGES;

USE dsfm_general;
source /var/www/scripts/<dump-sql-file>;
```


## Setup Django

### Generate staticfiles
```bash
# Console container: dsfm_general_backend
docker exec -it dsfm_general_backend bash
```

```bash
# exec createsuperuser
python manage.py collectstatic
```
* Link API docs: http://localhost:7010/docs


### Migrate Database

```bash
# Console container: dsfm_general_backend
docker exec -it dsfm_general_backend bash
```

```bash
# backup exists migrations
cp -r dsfm_general/migrations dsfm_general/migrations_bk
```

```bash
# clear exists migrations (3 scripts)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/__pycache__/*.pyc"  -delete
find . -path "*/migrations/*.pyc"  -delete
```

```bash
# exec migrate database
python manage.py makemigrations
python manage.py migrate
```


### Create Superuser
```bash
# Console container: dsfm_general_backend
docker exec -it dsfm_general_backend bash
```

```bash
# exec createsuperuser
python manage.py createsuperuser

# django asks:
Username (leave blank to use 'root'): 'root' #type your-username
Email address: 'root@example.com' #type your-email
Password: '123456' #type your-password
Password (again): '123456' #type your-password
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: 'y' #type y
Superuser created successfully.
```
```bash
python manage.py createsuperuser --username=root --email=root@example.com

# django ask:
Password: '123456' #type your-password
Password (again): '123456' #type your-password
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: 'y' #type y
Superuser created successfully.
```


* Your superuser (username | password): `root | 123456`
* Link login: http://localhost:7010/admin

----
Done.