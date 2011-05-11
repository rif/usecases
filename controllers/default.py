# -*- coding: utf-8 -*-

def index():
    projects = db(db.project.id>0).select()
    if len(request.args) > 0:
        form = crud.update(db.project, db.project(request.args[0]))
    else:
        form = crud.create(db.project)
    return dict(form = form, projects=projects)

def usecases():
    p = db.project(request.args[0])
    db.usecase.project.default = p.id
    form = crud.create(db.usecase)
    ucs = db(db.usecase.project == p.id).select(orderby=db.usecase.number)
    return dict(project=p, form=form, usecases=ucs)

def uc_detail():
    uc = db.usecase(request.args[0])
    return dict(uc = uc)

@auth.requires_membership('editor')
def uc_edit():
    uc = db.usecase(request.args[0])
    form = crud.update(db.usecase, uc, next=URL('uc_detail', args=(uc.id)), message=T('Usecase updated!'))
    return dict(uc = uc, form = form)

@auth.requires_membership('editor')
def var_add():
    uc = db.usecase(request.args[0])
    db.variation.usecase.default = uc.id
    if len(request.args) == 1:
        form = crud.create(db.variation, next=URL('uc_detail', args=(uc.id)), message=T('Variation created!'))
    else:
        var = db.variation(request.args[1])
        form = crud.update(db.variation, var, next=URL('uc_detail', args=(uc.id)), message=T('Variation updated!'))
    return dict(uc=uc, form=form)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    session.forget()
    return service()
