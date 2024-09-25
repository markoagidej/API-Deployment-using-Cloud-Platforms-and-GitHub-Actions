from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

app = Flask(__name__)
ma = Marshmallow(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cloud_db_m37j_user:MOy24Zfi7CGRat1TDCNQw4BNS6HNCgWW@dpg-crq6v6u8ii6s73cqdkjg-a.oregon-postgres.render.com/cloud_db_m37j'
app.config['SQLALCHEMNY_TRACK_MODIFICATIONS'] = False

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)

class Sum(Base):
    __tablename__ = "Sum"
    id: Mapped[int] = mapped_column(primary_key=True)
    num1: Mapped[int] = mapped_column(db.Integer, nullable=False)
    num2: Mapped[int] = mapped_column(db.Integer, nullable=False)
    result: Mapped[int] = mapped_column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Sum {self.id}: {self.num1} + {self.num2} = {self.result}'
    
class SumSchema(ma.Schema):
    id = fields.Integer()
    num1 = fields.Integer()
    num2 = fields.Integer()
    result = fields.Integer()

sums_schema = SumSchema(many=True)

@app.route('/sum', methods=['GET'])
def find_all():
    sums = db.session.execute(db.select(Sum)).scalars()
    return sums_schema.jsonify(sums), 200

@app.route('/sum', methods=["POST"])
def sum():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})

@app.route('/sum/result/<int:sum>', methods=['GET'])
def find_result(sum):
    sums = db.session.execute(db.select(Sum).where(Sum.result == sum)).scalars()
    return sums_schema.jsonify(sums), 200

with app.app_context():
    db.drop_all()
    db.create_all()