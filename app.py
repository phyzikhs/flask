from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
# from datetime import DateTime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	"""docstring for Todo"""
	content = db.Column(db.String(200), nullable=False)

	# date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__():
		return '<Task %r>' % self.id


@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)