from flask import Flask
from routes.home import home_route

#inicialização
app = Flask(__name__)

app.register_blueprint(home_route)

#execucao sempre no final do codigo
app.run(debug=True)
 