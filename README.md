### <h1>Wellcome to SDK Jarvas</h1>
<p>
  This is a tool to use the jarvas API, so in this repositori you can find the SDK represented by the "jarvas.py" file, and the tutorial wich I gonna explain for you Now! ⬇️
</p>
<hr/>
<img src="img/jarvas-help.png" />
<h1>How to use</h1>
<p>
  First you need run the file "get-start.py", in this file you gonna make a login in Jarvas then you create your credentials to access the API, to do that a prepare a acount for you, so use that:
</p>
<i>
  You just run this file one time to generate the Json web Token.
</i>
<ul>
  <li>
      email = testerUser@gmail.com
  </li>
  <li>
      senha = 123
  </li>
</ul>
<p>What this code do? let me explain for you😊. In the "jarvas.createToken" you are making the login and generate you access token, then when you run the "jarvas.create_json_file" you are making yours</p1>

```
token_access = jarvas.create_token(email='testerUser@gmail.com',password='123')
jarvas.create_json_file(token_access)
```
Basicamente eu estou fazendo uma aplicação no qual usuário ele vai poder executar uma aplicação por exemplo um bubble sort e durante o bubble sort vai ser enviado algumas informações para uma API chamada jarvas e aí essa API jarvas vai tratar essas informações que o usuário enviou e vai enviar isso para uma API de mensageria e essa API de mensageria vai enviar uma mensagem para o usuário o objetivo disso é basicamente quando o usuário executar uma aplicação muito extensa ele saber o que está acontecendo na API dele na aplicação dele sem a necessidade de ele ficar checando o computador então ele teria facilidade de poder checar apenas o celular dele como por exemplo checar o WhatsApp e vê que está acontecendo na aplicação dele porque seriam enviadas informações como por exemplo a sua aplicação concluiu 60%, essa seria basicamente a primeira funcionalidade dessa aplicação chamada javas a segunda funcionalidade seria basicamente o usuário poder interagir de volta pela rede social então enquanto na primeira ele vai receber uma mensagem do bot dizendo qual estado tá aplicação dele e a segunda funcionalidade seria de perguntar pro bot que estado está porque pode ser que durante a execução ele coloque lá no código dele que ele não quer receber essas mensagens e que ele quer apenas requisitar elas então a segunda funcionalidade dessa API seria basicamente  ele poder pedir informações pela rede social em conclusão a gente pode dizer que a primeira função da aplicação que eu estou desenvolvendo executar um programa externo e esse programa  externo realizar re quise sono para API bote jarvas e essa API enviar uma mensagem para ele do estado da aplicação externa que executou e a segunda funcionalidade é ele fazer requisições  pra play bot via rede social 
