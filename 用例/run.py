#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/16 0:37
# @Author  : brUce 杨
# @File    : run.py

import os

path = os.getcwd()  # 获取当前路径
os.system(f"pytest {path}/ --html=report.html -n=2")  # -n为多进程
# ver = os.system("pytest test_rule_buy.py::MyTestClass::test_1_tichucaimaixuqiu --demo_mode")  # 执行指定用例
# ver = os.system("pytest test_rule_buy.py::RuleBuy::test_8_Submit_application --pdb -s")  # 执行指定用例2
# ver = os.system("pytest D:/测试资料整理/自动化项目整理/PO模型/用例/ --report=自动化报告.html --title=自动化测试报告 --tester=杨靖锋 "
#                 "--desc=qq首页登录测试  --template=1 -n=2")  # -n为多线程/多进程
# ver = os.system("pytest D:/测试资料整理/自动化项目整理/PO模型/用例/ --html=report.html")


