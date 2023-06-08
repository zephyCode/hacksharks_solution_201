from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.app_context().push()
# db = SQLAlchemy(app)


# class Database(db.Model):
#     id = db.Column("id", db.Integer, primary_key=True)
#     email = db.Column("email", db.String(255))
#     topic = db.Column("topic", db.String(255))
#
#     def __init__(self, ids, email, topic):
#         self.id = ids
#         self.email = email
#         self.topic = topic


# db.create_all()


@app.route('/', methods=['POST', 'GET'])
def submit():
    # if request.method == "POST":
        # id_data = request.form.get('id')
        # email_data = request.form.get('email')
        # topic_data = request.form.get('topic')
        # new_data = Database(id_data, email_data, topic_data)
        # db.session.add(new_data)
        # db.session.commit()
    return render_template('submit.html')


if __name__ == "__main__":
    app.run(debug=True, port=8080)
