from flask import Flask, jsonify

todo = Flask(__name__)

students = [
    {
        'id':1,
        'name':'Lion1',
        'age':20
    },
{
        'id':2,
        'name':'Lion2',
        'age':20
    },
{
        'id':3,
        'name':'Lion3',
        'age':20
    }
]

@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/student/get/<int:id>')
def get_student_by_id(id):
    print(id)
    for std in students:
        if std['id'] == id:
            return jsonify(std)
        print(std)
    return jsonify('Not Found')

if __name__ == '__main__':
    todo.run(
        debug=True
    )