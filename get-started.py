from jarvas import Jarvas

jarvas = Jarvas(
    url="https://8dff-186-251-193-131.ngrok-free.app",
    phone="5555996852212"
)
token_access = jarvas.create_token(email='testerUser@gmail.com',password='123')
jarvas.create_json_file(token_access, file_name="credentials.json")
print(jarvas.view_users())