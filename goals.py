import db_connect
def goal():
    out = db_connect.getHtml("XiaoTeZhu")
    return out
