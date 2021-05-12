from flask import Blueprint , render_template 
auth = Blueprint('auth', __name__)


@auth.route('/Feauters')
def Feauters():
    return render_template("feauters.html")

@auth.route('/Pricing')
def Pricing():
    return render_template("pricing.html")



@auth.route('/About')
def About():
    return render_template("about.html")



@auth.route('/Support')
def Support():
    return render_template("support.html")

