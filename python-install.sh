sudo yum -y install yum-utils
sudo yum -y groupinstall development
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install python36u
python3.6 -V
sudo yum -y install python36u-pip
sudo yum -y install python36u-devel
pip3.6 install virtualenv
pip3.6 install --upgrade pip
