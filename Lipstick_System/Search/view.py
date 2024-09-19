from Lipstick_System import app
import re
from flask import render_template, request
from Lipstick_System.mongo import lipsticks
from math import dist

@app.route('/passform', methods=["POST"])
def passColor():
    input=request.form["confirmColor"]
    r=int(input[1:3], 16)
    g=int(input[3:5], 16)
    b=int(input[5:7], 16)
    input=f'rgb({r},{g},{b})'
    main=(r,g,b)
    res=[]
    for y in lipsticks.find({},{"_id":0}):
        if y['color_code']:
            other=eval(y['color_code'][4:-1])
            print(other)
            if(dist(main,other)<10):
                res.append(y)
    
    return render_template('Search/RecommendPage.html',color=input,result=res)   
 
@app.route('/passtext', methods=["POST"])
def passText():
    input=request.form["confirmColor"]
    input=re.sub("[\'[\"]", "", input)
    input=input.strip(']').split("->")
    lip_result = lipsticks.find({"name":input[0],"color":input[1]},{"_id":0})
    lip=[y for y in lip_result]
    main=eval(lip[0]['color_code'][4:-1])
    
    res=[]
    for y in lipsticks.find({},{"_id":0}):
        if y['color_code']:
            other=eval(y['color_code'][4:-1])
            print(other)
            if(dist(main,other)<50):
                res.append(y)
    
    return render_template('Search/RecommendPage.html',color=lip,result=res )