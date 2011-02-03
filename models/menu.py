# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('Usecase aplication for filemaker solutions')

#http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Radu Fericean'
response.meta.description = 'Usecase aplication for filemaker solutions'
response.meta.keywords = 'usecase, web2py, python, framework'
response.meta.generator = 'Web2py Enterprise Framework'
response.meta.copyright = 'Copyright 2011'


##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    (T('Home'), False, URL(request.application,'default','index'), [])
    ]
