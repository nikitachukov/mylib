﻿drop database if EXISTS django;
CREATE DATABASE django;
GRANT ALL ON django.* TO 'django'@'localhost' IDENTIFIED BY 'django';
