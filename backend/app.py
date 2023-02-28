from flask import Flask, jsonify, request #import libraries
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = '' #update to actual db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Course(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    credits = db.Column(db.String(100))
    capacity = db.Column(db.String(100))
    CRN = db.Column(db.String(100))


    #Constructor for course class
    def __init__(self, name, credits, capacity, crn):
        self.name = name
        self.credits = credits
        self.capacity = capacity
        self.crn = crn
class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'credits', 'capacity', 'crn')

course_schema = CourseSchema()
courses_schema = CourseSchema(many = True)

@app.route('/', methods = ['GET'])
def get_courses():
    return jsonify({"Hello" : "World"})

@app.route('/add', methods = ['POST'])
def add_course():
    name = request.json['name']
    credits = request.json['credits']
    capacity = request.json['capacity']
    crn = request.json['crn']

    course = Course(name, credits, capacity, crn)
    db.session.add(course)
    db.session.commit()
    return course_schema.jsonify(course)

if __name__ == "__main__":
    app.run(debug = True)