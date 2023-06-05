#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from collections import namedtuple

User = namedtuple('User', ['user_id', 'passwd', 'wechat_openid'])


# 登录校园网/寝室宽带的用户账号(学号, 登录教务处的密码, None)
#  例如： User('202912272625', '123456Abc@#$', None)

class LoginConfig:
    def __init__(self):
        #   id, passwd, network
        self.envs = {str(key).upper(): value for key, value in os.environ.items()}
        self.login_options = {
            'user': User(self.envs['ID'], self.envs['PASSWD'], None),  # 填上学号密码
            # 认证页面的地址
            'url': "http://10.253.0.237" if self.envs['NETWORK'] == 'uestc' else "http://10.253.0.235",
            # 认证页面的地址里的参数ac_id=???
            'ac_id': '1' if self.envs['NETWORK'] == 'uestc' else '3',  # 主楼有线校园网acid=1

            # 网络提供商的类型
            'domain': f'@dx-uestc' if self.envs['NETWORK'] == 'uestc' else f"@{self.envs['NETWORK']}",
            # 电信:"@dx", 移动:"@cmcc", 校园网:"@dx-uestc"

            # 下面的一般不用改
            'test_ip': "114.114.114.114",  # IP to test whether the Internet is connected
            'delay': 16,  # delay seconds
            'max_failed': 3,  # 连续ping失败n次, 认为断网
        }

    def get_login_options(self):
        return self.login_options
