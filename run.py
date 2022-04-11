from myapp.main import create_app
from myapp import blueprint
from myapp.main.model import blacklist
from myapp.main.model import customer,order,product

config_name='development'
app=create_app(config_name)
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)