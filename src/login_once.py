# !/usr/bin/env python
# -*- coding:utf-8 -*-
from BitSrunLogin.LoginManager import LoginManager
from config import LoginConfig

if __name__ == '__main__':
    login_options = LoginConfig().get_login_options()
    user = login_options['user']
    LoginManager(**login_options).login(username=user.user_id, password=user.passwd)
