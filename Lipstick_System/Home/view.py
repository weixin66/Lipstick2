from Lipstick_System import app
from Lipstick_System.mongo import lipsticks,users
from flask import render_template

@app.route('/home')
def home():
    return render_template('Home/HomePage.html')
@app.route('/pic_search')
def Picture_search():
    return render_template('Search/Pic_Search.html')
@app.route('/color_search')
def Color_search():
    return render_template('Search/Color_Search.html')
@app.route('/text_search')
def Text_search():
    brands_result = lipsticks.distinct('brand')
    re=""
    lips={};
    result=[];
    i=0;
    for x in brands_result:
        lips[i]=lipsticks.find({ "brand": x },{"_id":0, "name": 1, "color": 1, "color_code": 1 })
        lipstick=[];
        for y in lips[i]:
            lipstick.append(y["name"]+"->"+y["color"]+"->"+y["color_code"]);
        result.append(lipstick);
        re=re+","+x
        i+=1;
    return render_template('Search/Text_Search.html',brand=re,lips=result)