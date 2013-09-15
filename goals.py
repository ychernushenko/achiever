import db_connect
def goal(userid):
    out = db_connect.getHtml(userid)
    return out
