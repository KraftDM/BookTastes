import cgi

def get():
    print("ke1")
    form = cgi.FieldStorage()
    print("ke2")
    searchterm =  form.getvalue('recept_name')
    print("ke3")
    print(searchterm)