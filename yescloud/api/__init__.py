from flask import Flask, Blueprint
from flask_restx import Api


# Create a new Flask instance
app = Flask(__name__)

# Disable JSON key ordering.from flask import Flask, Blueprint
from flask_restx import Api


# Results per page
MAX_RESULTS_PER_PAGE = 100

# Create a new Flask instance
app = Flask(__name__)

# Disable JSON key ordering.
app.config['JSON_SORT_KEYS'] = False
# Flask-RESTX: Disable X-Fields entry on Swagger
app.config['RESTX_MASK_SWAGGER'] = False
# Use our own way to report errors instead
app.config['ERROR_INCLUDE_MESSAGE'] = False

# Create alpha blueprint
alpha_blueprint = Blueprint('api', __name__, url_prefix='/api/alpha')

# Create Flask-RestX Api
# Put Swagger UI on a separate /ui path, don't "take over" the root path
api = Api(alpha_blueprint, title='YesCloud REST API', version='0.0.1-alpha', description='Swagger interface for YesCloud VM management REST API', doc='/ui/', ordered=True)

# TODO: add namespaces
from .vm import api as vm_api
from .network import api as net_api
api.add_namespace(vm_api)
api.add_namespace(net_api)

# Register blueprint
app.register_blueprint(alpha_blueprint)
