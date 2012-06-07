#!/usr/bin/env python
#
# Copyright 2011 Yuji Takabatake ( yuji.takabatake@gmail.com )
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import os.path
import re
import tornado.auth
import tornado.database
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

import unicodedata
import datetime
import difflib
from HTMLParser import HTMLParser
import Image
from cStringIO import StringIO
import time
import facebook

# Sending email
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate


define("port", default=8888, help="run on the given port", type=int)
define("facebook_app_url", default="https://connect.facebook.net/en_US/all.js", \
       help="Facebook Application URL")
define("facebook_app_id", default="", help="Facebook Application ID")
define("facebook_app_secret", default="", help="Facebook Application Secret")

define("mysql_host", default="", help="cloudswan database host")
define("mysql_database", default="", help="cloudswan database name")
define("mysql_user", default="", help="cloudswan database user")
define("mysql_password", default="", help="cloudswan database password")


class Application(tornado.web.Application):
  def __init__(self):
    pass
