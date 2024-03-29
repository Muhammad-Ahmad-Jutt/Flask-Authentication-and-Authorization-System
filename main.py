from flask import Flask, json, jsonify, render_template, request
import hashlib
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/users'
app.config['JWT_SECRET_KEY'] = '987654321'
jwt = JWTManager(app)
db = SQLAlchemy(app)
# user and item model for the databse
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(20), nullable=False)

# the logout api
@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Authorization header missing'}), 400
    
    token = auth_header.split()[1] if len(auth_header.split()) > 1 else None
    if not token:
        return jsonify({'error': 'Token missing in Authorization header'}), 400

# the user_info api which show the userdata to the user
@app.route('/user_info', methods=['GET'])
@jwt_required()
def get_user_info():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.filter_by(id=current_user_id).first()
        if user:
            return jsonify({'username': user.username})
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# the items api which only show api uing is signed in
@app.route('/items', methods=['GET'])
@jwt_required()
def getall_item():
    try:
        items = Items.query.all()
        # Convert the query result to a list of dictionaries
        items_list = [{'id': item.id, 'item_name': item.item_name} for item in items]
        return {'success': True, 'items': items_list}
    except Exception as e:
        return {'success': False, 'message': str(e)}



# the index api
@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

# The authentication system which authenticate a person
def authenticate(username, password):
    try:
        user = User.query.filter_by(username=username, password_hash=password).first()
        if user:
            return user.id
        else:
            return ''
    except Exception as e:
        # Handle the exception and return a custom error message
        return f"Error occurred during authentication: {str(e)}"
# the password to jash converter function
def passtohash(password):
    hpassword = hashlib.sha256(password.encode('utf-8'))
    password = hpassword.hexdigest()
    return password
# the login api fnction
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        data = json.loads(request.data)
        username = data['username']
        password = passtohash(data['password'])
        result = authenticate(username, password)
        if result:
            token = create_access_token(result)
            return jsonify({'token': token})
        else:
            return 'User not found'
# the create user api which create a new user to the database
@app.route('/create_user', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        data = json.loads(request.data)
        username = data['username']
        password = passtohash(data['password'])
        try:
            new_user = User(username = username, password_hash = password)
            db.session.add(new_user)
            db.session.commit()
            return {'success':True, 'Message': 'User created sucessfull'}
        except Exception as e:
            return {'Failed':False, 'Message': str(e)}

# the default main funciton
if __name__ == '__main__':
    app.run(debug=True)