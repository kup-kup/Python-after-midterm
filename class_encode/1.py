import base64 as b64

pas = "password123"
en = b64.b64encode(pas.encode("UTF-8"))
print(en)

de = b64.b64decode(en)
print(de)