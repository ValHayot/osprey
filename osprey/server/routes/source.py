from flask import Blueprint, jsonify, request
from app import db
from app.models import Source
from app.error import ServiceError

source_routes = Blueprint('source_routes', __name__, url_prefix='/source')

@source_routes.route('/', methods=['GET'])
def all_sources():
    page        = request.args.get('page') or 1
    per_page    = request.args.get('per_page') or 15
    sources     = Source.query.paginate(page=page, per_page=per_page)
    result      = [source.toJSON() for source in sources]
    return jsonify(result), 200

@source_routes.route('/', methods=['POST'])
def create_source():
    try:
        json_data = request.json
        s = Source(**json_data)
        db.session.add(s)
        db.session.commit()
        return jsonify(s.toJSON()), 200
    except ServiceError as s:
        return jsonify(s.toJSON()), s.code
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500
    

@source_routes.route('/<id>', methods=['GET'])
def get_data(id):
    s = Source.query.get(id)
    if s is None:
        return jsonify({}), 404

    return jsonify(s.toJSON()), 200


# def create_new_version():
#     # oh we have created a new version
#     # we run a job somehow, to pull the data? and then run verifier, and store it in Proxystore (or) Globus | path?
#     pass


"""

    1. CLI (me) -> API Endpoint
        i) Creating source
    2. DIFF
    3. Verifier (me)
    4. Timer 
    5. Globus Data
    6. Run on chameleon -> Create an instance | docker install | docker run
"""