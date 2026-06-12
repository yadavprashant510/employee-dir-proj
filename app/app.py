from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from models import db, Employee

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():

    search = request.args.get("search", "")

    if search:
        employees = Employee.query.filter(
            Employee.name.contains(search)
        ).all()
    else:
        employees = Employee.query.all()

    return render_template(
        "index.html",
        employees=employees
    )


@app.route("/employee/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        employee = Employee(
            name=request.form["name"],
            email=request.form["email"],
            department=request.form["department"]
        )

        db.session.add(employee)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/employee/delete/<int:id>")
def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )