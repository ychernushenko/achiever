def login():
    f = open("templates/login.html")
    out = ""
    for line in f:
        out += line
    return out
