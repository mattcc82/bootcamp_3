
def index():
    return dict()


def get_data():
    import os
    from data_pull import data_pull, group_by_name

    # get filter vars
    decade = request.vars.decade

    # filter definitions
    decades = [
        range(1979, 2020),
        range(1990, 2000),
        range(2000, 2010),
        range(2010, 2020)
    ]

    # filter init
    filter = {}

    filter['year_of_release'] = decades[decade]

    path = os.path.join(request.folder, 'private/data/data.h5')
    source = '/data/'

    output = {}

    # output = data_pull(path, source)
    # return output.reset_index().to_json(orient="records")

    df = data_pull(path, source, filter)

    output['raw_data'] = df
    output['grouped_by_name_data'] = group_by_name(df.copy())
    output['grouped_by_name_data'].columns = output['grouped_by_name_data'].columns.get_level_values(0)

    output['raw_data'] = output['raw_data'].reset_index().to_json(orient="records")
    output['grouped_by_name_data'] = output['grouped_by_name_data'].reset_index().to_json(orient="records")

    return response.json(output)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


