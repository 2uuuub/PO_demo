#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 13:08
# @Author  : brUce 杨
# @File    : self.py

import pytest
from seleniumbase import BaseCase
from PO模型.对象.page import LoginPage


class RuBe(BaseCase):
    # LoginPage.dakaiwangzhi()

    # 打开网址
    def dakaiwangzhi(self):
       self.open(LoginPage.url)

    # 切换frame

    def qiehaunframe(self):
        self.switch_to_frame(LoginPage.iframe)

    # 点击账号密码登录
    def dianjizhanghaomimadenglu(self):
        self.click(LoginPage.btn1)

    # 输入账号
    def shuruyonghuming(self, username):
        self.fill(LoginPage.user, username)

    # 输入密码
    def shurumima(self, password):
        self.fill(LoginPage.pwd, password)

    # 点击授权并登录按钮
    def dianjidengluanniu(self):
        self.click(LoginPage.button)

    def test_1_DengLu(self):
        self.dakaiwangzhi()
        self.qiehaunframe()
        self.dianjizhanghaomimadenglu()
        self.shuruyonghuming('384036208')
        self.shurumima('ypp.com.cn')
        self.dianjidengluanniu()

        # 断言
        self.wait_for_element_present(LoginPage.assert_text, timeout=100)


if __name__ == '__main__':
    pytest.main()
