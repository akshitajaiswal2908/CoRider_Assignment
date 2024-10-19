from flask import Blueprint, jsonify, request, render_template, redirect
from app import mongo
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId
from flask import request, render_template


user_blueprint = Blueprint('user_blueprint', __name__)


# Rest APIs

@user_blueprint.route("/hello")
def test():
    return "hello world"

@user_blueprint.route('/users',  methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    user_list = [{'id': str(user['_id']), 'name': user['name'], 'email': user['email']} for user in users]
    return jsonify(user_list)

@user_blueprint.route('/users/<id>',  methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})  
    user_response = {'id': str(user['_id']), 'name': user['name'], 'email': user['email']}
    return jsonify(user_response)

@user_blueprint.route('/users',  methods=['POST'])
def create_user():
    data = request.form
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user_id = ObjectId()
    new_user = {
        '_id': new_user_id, 
        'name': data['name'],
        'email': data['email'],
        'password': hashed_password
    }
    mongo.db.users.insert_one(new_user)
    return jsonify({'id': str(new_user_id)})

@user_blueprint.route('/users/<id>',  methods=['PUT'])
def edit_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if not user:
        return jsonify({'message':'user not found'})
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    update_data = {}
    if name:
        update_data['name'] = name
    if email:
        update_data['email'] = email
    if password:
        update_data['password'] = generate_password_hash(password, method='pbkdf2:sha256')

    mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': update_data})
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    user_response = {'id': str(user['_id']), 'name': user['name'], 'email': user['email']}
    return jsonify(user_response)


@user_blueprint.route('/users/<id>',  methods=['DELETE'])
def delete_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if not user:
        return jsonify({'message':'user not found'})
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    return jsonify({})


# Webpages

@user_blueprint.route('/', methods=['GET'])
def index():
    return redirect('/home')

@user_blueprint.route('/home', methods=['GET'])
def homepage():
    return render_template('index.html')

@user_blueprint.route('/home/users', methods=['GET'])
def users_page():
    users = mongo.db.users.find()
    user_list = [{'id': str(user['_id']), 'name': user['name'], 'email': user['email']} for user in users]
    return render_template('users.html', users=user_list)

@user_blueprint.route('/home/users/new', methods=['GET'])
def new_user_page():
    return render_template('new_user.html')

@user_blueprint.route('/home/users/edit/<id>',methods=['GET'])
def edit_user_page(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    user_response = {'id': str(user['_id']), 'name': user['name'], 'email': user['email']}
    return render_template('edit_user.html', user=user_response)

@user_blueprint.route('/home/users/edit/<id>/submit',methods=['POST'])
def edit_user_submit(id):
    edit_user(id)
    return redirect('/home/users')

@user_blueprint.route('/home/users/new/submit',methods=['POST'])
def new_user_submit():
    create_user()
    return redirect('/home/users')