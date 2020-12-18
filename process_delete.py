#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

#Redirection
print("Location: index.py")
print("")
