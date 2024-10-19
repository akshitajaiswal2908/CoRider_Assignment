from flask import Blueprint, request, render_template, redirect
from app import mongo
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId
from flask import request, render_template


user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/')
def index():
    return render_template('index.html')

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    user_list = [{'id': str(user['_id']), 'name': user['name'], 'email': user['email']} for user in users]
    return render_template('users.html', users=user_list)

@user_blueprint.route('/users/new', methods=['GET'])
def new_user():
    return render_template('new_user.html')

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.form
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = {
        '_id': ObjectId(), 
        'name': data['name'],
        'email': data['email'],
        'password': hashed_password
    }
    mongo.db.users.insert_one(new_user)
    return redirect('/users')

@user_blueprint.route('/users/edit/<id>', methods=['GET', 'POST'])
def edit_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})  
    if not user:
        return render_template('error.html', message='User not found'), 404

    if request.method == 'POST':
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
        return redirect('/users')  

    return render_template('edit_users.html', user=user)


@user_blueprint.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.form
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if not user:
        return render_template('error.html', message='User not found'), 404
    updated_data = {'name': data['name'], 'email': data['email']}
    if 'password' in data and data['password']:
        updated_data['password'] = generate_password_hash(data['password'], method='pbkdf2:sha256')
    mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': updated_data})
    return redirect('/users')

@user_blueprint.route('/users/delete/<id>', methods=['GET'])
def delete_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if not user:
        return render_template('error.html', message='User not found'), 404
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    return redirect('/users')
