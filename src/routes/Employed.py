from flask import Blueprint, jsonify, request
from models.entities.Employed import Employed
from models.employedModel import EmployedModel
import uuid

main=Blueprint('employed_blueprint', __name__)

@main.route('/')
def get_employed():
    try:
        employ=EmployedModel.get_employed()
        return jsonify(employ)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/<id>')
def get_employ(id):
    try:
        empl=EmployedModel.get_employ(id)
        if empl != None:
            return jsonify(empl)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/add',methods=['POST'])
def add_employ():
    try:
        name=request.json['name']
        charge=request.json['charge']
        salary=request.json['salary']
        startdate=request.json['startdate']
        id = uuid.uuid4()
        employ = Employed(str(id),name,charge,salary,startdate)

        affected_rows=EmployedModel().add_employ(employ)
        if affected_rows == 1:
            return jsonify(employ.id)
        else:
            return jsonify({'message':"error on insert"}),500

        
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/update/<id>',methods=['PUT'])
def update_employ(id):
    try:
        name=request.json['name']
        charge=request.json['charge']
        salary=request.json['salary']
        startdate=request.json['startdate']
        employ = Employed(id,name,charge,salary,startdate)

        affected_rows=EmployedModel().update_employ(employ)
        if affected_rows == 1:
            return jsonify(employ.id)
        else:
            return jsonify({'message':"no employed updated"}),404

        
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/delete/<id>',methods=['DELETE'])
def delete_employ(id):
    try:
        employ=Employed(id)
        affected_rows=EmployedModel.delete_employ(employ)
        if affected_rows == 1:
            return jsonify(employ.id)
        else:
            return jsonify({'message':"No employed deleted"}),404

        
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

    