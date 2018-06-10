# Traveb

A progressive web app to connect distant travelers and local business to provide/seek service as exchange.

### Prerequisites
1. Virtualenv running on fedora(centos 7) preferred
2. Django 1.1
3. Python 3.6
4. Angular 5
5. MySQL (Mariadb)

```markdown
**Setting up the environment**

***Server***

# 1.Installing Virtual Environment (optional)
$`sh setupenv.sh`

# 2.Installing Python3.6 and pip
$`sh python-install.sh`

# Installing Django framework
$`sh setup-django.sh`

# Installing MySQL(mariadb) and load the database schema from the repo
$`yum install mariadb mariadb-server`
$`mysql_secure_installation`
$`mysql -u(username) -p(password) < traavn.sql`

# Setting up mysql to django models(assuming you have knowledge on dhango manage functionalities)
$`python manage.py makemigration`
$`python manage.py migrate`

**Client**

# Installing installing node.js along npm
$`sh install-nodejs.sh`

# Installing Angular/cli
$`npm install -g @angular/cli`

```
## Done Application is ready
