from flask import Flask, jsonify
from flasgger import Swagger


fileYaml = 'swagger.yaml'
app = Flask(__name__) #variable flask app
app.config['SWAGGER'] = {
    'title': fileYaml,
    'uiversion': 3
}
class testYaml():
    # build ininisialization
    def __init__(self):
        self.dataYaml = fileYaml

    # build dataSwagger function
    def dataSwagger(self, dataYaml = fileYaml):
        self.dataYaml = dataYaml
        app.config.from_object(__name__)    
        Swagger(app, template_file= self.dataYaml)

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called.')

if __name__ == "__main__":
  try:
    Mytest = testYaml()
    # Mytest.dataSwagger(dataYaml= 'gatewayMobile.yaml') # api mobile
    Mytest.dataSwagger() # api web
    app.run(debug=True)
    Mytest.__del__() # api web

  except OSError as err:
      print("OS error: {0}".format(err))
