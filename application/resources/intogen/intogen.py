from flask import Blueprint

intogen = Blueprint("intogen", __name__)

#fbsdhfbsd
@intogen.route("/home")
@intogen.route("/")
def course_insights_home():
    return "intogen home"
