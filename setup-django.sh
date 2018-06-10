#install django
sudo yum --enablerepo=extras install epel-release -y
sudo yum update -y
sudo yum install python-devel python-setuptools python-pip -y
sudo pip install --upgrade pip
pip install django
pip install djangorestframework
pip install djangorestframework-jwt
pip install django-angular
