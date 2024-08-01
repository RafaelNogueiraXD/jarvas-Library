from jarvas import Jarvas

jarvas = Jarvas(
    url="http://127.0.0.1:8000/"
)
token_access = jarvas.create_token(email='testerUser@gmail.com',password='123')
jarvas.create_json_file(token_access)
print(jarvas.viewUsers())