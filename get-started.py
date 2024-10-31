from jarvas import Jarvas

jarvas = Jarvas(
    url="http://127.0.0.1:8000",
    app_name='bubble sort',
    social_media="discord"
)

token_access = jarvas.create_token(email='testerUser@gmail.com',password='123')
jarvas.create_json_file(token_access)
