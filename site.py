#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import jinja2


templateLoader = jinja2.FileSystemLoader( searchpath="template" )
templateEnv = jinja2.Environment( loader=templateLoader )

templateVars = {
    "title": "Xavier Raffin | Architecte logiciel à Tisséo : open source, JavaScript, C++, Linux, Python ..."
    }

templateIndex = templateEnv.get_template( "index.html" )
with open('index.html', 'w') as f:
    f.write( templateIndex.render( templateVars ) )

templateNews = templateEnv.get_template( "about.html" )
with open('about.html', 'w') as f:
    f.write( templateNews.render( templateVars ) )




