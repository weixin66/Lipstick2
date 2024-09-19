$(document).ready(function() {
    var lip=document.getElementById("msg");//抓color
    var condition=document.getElementById("condition");//抓提示句
    var result=document.getElementById("result");//抓結果
    
    if(lip.textContent.includes("color")){
        Color=lip.textContent.slice(1, -1).replace(/'/g,'"');
        var theLip=JSON.parse(Color);
        console.log(theLip.color);
        condition.style.background=theLip.color_code;
        condition.textContent="以"+theLip.brand+"的"+theLip.color+"搜尋的結果:"
    }
    else{
        condition.style.background=lip.textContent;
        condition.textContent="以此顏色搜尋的結果:"
    }
    var lips=[]
    Color=result.textContent.slice(2, -2).replace(/'/g,'"').split("}, {");
    for (y in Color){
        var theLip=JSON.parse(JSON.stringify("{"+Color[y]+"}"));
        eval('var obj='+theLip);
        lips.push(obj)
    }
    for (y in lips){
        a='<div class="lipstick">';
        a+='<img class="mx-auto rounded lip-pic"referrerpolicy="no-referrer" src='+lips[y]["pic"]+'/>';
        a+='<p>🤍</p>';//🧡要寫若在收藏庫中換成紅心
        a+='<h5>'+lips[y]["brand"]+"-"+lips[y]["color"]+'</h5>';
        a+='<h6>'+lips[y]["price"]+'</h6>';
        a+='</div>';
        $(".col-md-4").append(a);
    }
})