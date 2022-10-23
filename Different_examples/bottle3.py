from flask import Flask, request,render_template
site=Flask(__name__)
@site.route('/')
def home():
    thing=request.values.get('thing')
    height=request.values.get('height')
    color=request.values.get('color')
    return render_template('home.html',thing=thing,height=height,color=color)
site.run(port=5000)