#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 13:01
# @Author  : brUce 杨
# @File    : page.py


from seleniumbase import BaseCase


class LoginPage(BaseCase):
    # 网址
    url = 'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101487368&redirect_uri=https%3A%2F%2Fpacaio.match.qq.com%2Fqq%2FloginBack%3Fsurl%3Dhttps%3A%2F%2Fwww.qq.com%2F&state=5b481c68e379d'
    iframe = 'ptlogin_iframe'
    # 账号密码登录
    btn1 = '//*[@id="switcher_plogin"]'
    # 用户名栏
    user = '[id="u"]'
    # 密码栏
    pwd = '[id="p"]'
    # 授权并登录按钮
    button = '[value="授权并登录"]'
    # 断言出现元素
    assert_text = '[bosszone="jrht_logo"]'











