#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/16 0:37
# @Author  : brUce 杨
# @File    : 多进程运行.py

import os

# ver = os.system("pytest test_rule_buy.py::MyTestClass::test_1_tichucaimaixuqiu --demo_mode")
# ver = os.system("pytest test_rule_buy.py::RuleBuy::test_8_Submit_application --pdb -s")
ver = os.system("pytest D:/测试资料整理/自动化项目整理/PO模型/用例/ --report=自动化报告.html --title=自动化测试报告 --tester=杨靖锋 "
                "--desc=qq首页登录测试  --template=1 -n=2")  #-n为多线程/多进程
# ver = os.system("pytest D:/测试资料整理/自动化项目整理/PO模型/用例/ --html=report.html")
