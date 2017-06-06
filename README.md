# traveler

[![Build Status](https://travis-ci.org/travelgeezer/traveler.svg?branch=master)](https://travis-ci.org/travelgeezer/traveler)
[![Coverage Status](https://coveralls.io/repos/github/travelgeezer/traveler/badge.svg?branch=master)](https://coveralls.io/github/travelgeezer/traveler?branch=master)
[![Code Climate](https://codeclimate.com/github/travelgeezer/traveler/badges/gpa.svg)](https://codeclimate.com/github/travelgeezer/traveler)


### Todo List
-------------

- hello world

- 学习该语言的语法

- 实现一个TODO List

- 熟记你所使用的IDE，编辑器的各种快捷建

- 集成 Vue | React | Angular

- 构建一个RESTfull服务

- 尝试设计一个API

- 尝试使用不同过的IDE和编辑器

- 尝试使用命令行工具

- 尝试使用快捷键代替鼠标

- 尝试使用GNU/Linux

- 写一个简单的测试

- 写一个Mock测试

- 写一个Stub测试

- 尝试使用TDD开发一个简单的功能

- 尝试做一些简单的重命名变量

- 尝试一些提取变量的操作

- 尝试做一些重命名现有的函数

- 使用一些针对不同开发环境的插件

- 用Toggle来管理应用的一些新特性

- ～～尝试搭建CI环境～～

- 尝试使用CI创建Build

- 使用虚拟机安装GNU/Linux操作系统

- 理解Tomacat和Jetty的关系

- 使用Docker安装应用程序

- 使用Docker作应用容器

- 尝试回顾自己做的一个项目的Well, Less Well

- 搭建一个静态服务器

- 使用反向代理

- 尝试使用自动部署工具

- 试着添加Google Analytics服务

- 尝试用分析工具分析数据

- 试着用编程来分析数据

- 使用分层架构设计应用

- 了解Pipe and Filters模式


### Read Books
--------------

-《HTML与CSS》(第二版)

-《JavaScript 权威指南》

-《JavaScript 高级程序设计》

-《全栈应用开发：精益实践》


### 技术栈
---------

- python

- django

- Django REST Framework

- unittest: 单元测试框架

##### setup

1. 安装 python3 version >= 3.6
2. 安装 mysql
3. 创建数据库: mysql -e 'create database traveler;' -u root
4. 同步数据库: python3 manage.py makemigrations && python3 manage.py migrate
5. 安装依赖: pip3 install -r requirements.txt
6. 运行测试: python3 manage.py test
7. 运行Demo: python3 manage.py runserver


## Workflow

1. 获取上游最新代码：``git pull --rebase``
2. 添加修改功能，**小步提交**，即实现某个小功能就本地小步提交一次。如：
    1. 添加某个库，提交一次。
    2. 完成 UI 设计，提交一次。
    3. 完成功能，提交一次。
    4. 编写测试，提交一次。
    5. 修复 Lint，提交一次。
3. 编写、运行测试 ``python3 manage.py test``
4. 提交到服务器
5. 来一个 Pull Request


### 提交信息规范

建议提交信息按如下规范：

```
[任务分类] 主要修改组件：修改内容
```

示例 1，``[T] home: create home app`` 。其中的 ``T`` 表示这是一个技术卡，``home`` 表示修改的是 主页，``create home app`` 则表示创建了主界面用到的app。

示例 2，``[Edit] views: add create article api``。其中的 ``Edit`` 表示修改的是edit app 下的内容，``views`` 则表示修改的是 ``views.py``，``add create article api`` 则表示是添加了创建文章的api接口


