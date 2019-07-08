window.onload = function(){
    
    var nav = document.getElementById("thelist");
    var shoes = document.getElementById("theproduct");

    scrollMenu( nav,shoes );

    //获取ul（图片外框）
    var box = document.getElementById("box");
    //获取li（图片）
    var li = box.getElementsByTagName("li");
    //获取单个li宽度（单张图片宽度）
    var liWidth = li[0].scrollWidth;
    //获取左按钮
    var butL = document.getElementById("butL");
    //获取右按钮
    var butR = document.getElementById("butR");
    //获取小圆点
    var dot = document.getElementById("dot").getElementsByTagName("li");
    //定义数字
    var index = 0;
    //定义开关
    var flag = true;
    
    //更改图片外框宽度（图片的数量*单张图片的宽度）
    box.style.width = li.length*liWidth+"px";
    
    //点击下一张
    butR.onclick = function(){
       //判断flag是否为true
        if(flag){
            //更改flag为false
            flag = false;
            //数字加1
            index++;
            //判断数字是否等于图片的总数量
            if(index == li.length){
                //将数字改为0
                index = 0;
            };
            //更改图片外边框的left，向左边移动，移动的尺寸为数字*单张图片图片的宽度                         
            box.style.left = -index*liWidth+"px";
            //遍历循环查找小圆点下标位置
            for(var i = 0 ; i < dot.length; i++){
               //判断小圆点的下标位置是否与数字相同
               if(i == index){
                    //更改已匹配到li，将已写好的css样式id名字赋给它
                    dot[index].id = "dotIs";
                }else{
                    //去掉未匹配的id名字
                    dot[i].id = "";
                };
            };
            //延迟执行，500毫秒之后执行，延迟的时间与css的transition: all 0.5s;的5s一致
           setTimeout(function(){
                //改变flag为true
                flag = true;
            },500)
        };
    };
    
    //点击上一张
    butL.onclick = function(){
        //判断flag是否为true
        if(flag){
            //更改flag为false
            flag = false;
            //数字减1
            index--;
            //判断数字是否小于0
            if(index < 0){
                //将数字图片总数的数字
                index = li.length-1
            };
            //更改图片外边框的left，向右边移动，移动的尺寸为数字*单张图片图片的宽度
            box.style.left = -index*liWidth+"px";
            //遍历循环查找小圆点下标位置
            for(var i = 0 ; i < dot.length; i++){
                //判断小圆点的下标位置是否与数字相同
                if(i == index){
                    dot[index].id = "dotIs";
                    //更改已匹配到li，将已写好的css样式id名字赋给它
                }else{
                    //去掉未匹配的id名字
                    dot[i].id = "";
                };
            };
            //延迟执行，500毫秒之后执行，延迟的时间与css的transition: all 0.5s;的5s一致
            setTimeout(function(){
                //改变flag为true
                flag = true;
            },500);
        };
    };
    
    //设置自动播放
    function play(){
        //连续不断持续的执行
        lunbo = setInterval(function(){
            //数字加1
            index++;
            //判断数字是否等于图片的总数量
            if(index == li.length){
                //将数字改为0
                index = 0;
            };
            //更改图片外边框的left，向左边移动，移动的尺寸为数字*单张图片图片的宽度
            box.style.left = -index*liWidth+"px";
            //遍历循环查找小圆点下标位置
            for(var i = 0 ; i < dot.length; i++){
                //判断小圆点的下标位置是否与数字相同
                if(i == index){
                    //更改已匹配到li，将已写好的css样式id名字赋给它
                    dot[index].id = "dotIs";
                }else{
                    //去掉未匹配的id名字
                    dot[i].id = "";
                };
            };
            //每3000（3秒）执行一次。
        },3000);
    };
    
    //设置停止自动播放
    function stop(){
        //停止（lunbo）已写好的持续执行方法。
        clearTimeout(lunbo);
    };
    
    //默认启动自动播放
    play();
    
    //点击圆点
    for(var i = 0; i < dot.length; i++){
        //给每个小圆点赋值，每个小圆点都有一个相对应的数字。
        dot[i].is = i;
        //鼠标移入小圆点
        dot[i].onmouseover = function(){
            //停止图片自动播放
            stop();
        }
        
        //鼠标移出小圆点
        dot[i].onmouseout = function(){
            //图片继续自动播放
            play();
        }
        
        //点击小圆点
        dot[i].onclick = function(){
            //更改图片外边框的left，向选择的小圆点移动方向，移动的尺寸为小圆点的数字*单张图片图片的宽度
            box.style.left = -this.is*liWidth+"px";
            //循环遍历小圆点
            for(var i = 0 ; i < dot.length; i++){
                //判断小圆点的数字是否等于选中的小圆点数字
                if(i == this.is){
                    //更改数字（index）等于的小圆点选中的数字
                    index = dot[i].is;
                    //更改已匹配到li，将已写好的css样式id名字赋给它
                    dot[this.is].id = "dotIs";
                }else{
                    //去掉未匹配的id名字
                    dot[i].id = "";
                };
            };
        };
    };
    
    //鼠标移入左按钮
    butL.onmouseover = function(){
        //停止自动轮播
        stop();
        //左按钮显示
        butL.style.display = "block";
        //右按钮显示
        butR.style.display = "block";
    };
    
    //鼠标移出左按钮
    butL.onmouseout = function(){
        //继续自动轮播
        play();
        //左按钮隐藏
        butL.style.display = "none";
        //右按钮隐藏
       butR.style.display = "none";
    }
    
    //鼠标移入右按钮
    butR.onmouseover = function(){
        //停止自动轮播
        stop();
        //左按钮显示
        butL.style.display = "block";
        //右按钮显示
        butR.style.display = "block";
    };
    
    //鼠标移出右按钮
    butR.onmouseout = function(){
       //继续自动轮播
        play();
        //左按钮隐藏
        butL.style.display = "none";
        //右按钮隐藏
        butR.style.display = "none";
    }
    
    //鼠标移入图片
    box.onmouseover = function(){
        //停止自动轮播
        stop();
        //左按钮显示
       butL.style.display = "block";
        //右按钮显示
        butR.style.display = "block";
    };
    
   //鼠标移出图片
    box.onmouseout = function(){
       //继续自动轮播
       play();
        //左按钮隐藏
        butL.style.display = "none";
       //右按钮隐藏
        butR.style.display = "none";
    }
   
    
}

function scrollMenu( obj,target ){
    window.onscroll = function(){

        var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        var top = target.offsetTop;
        //当滚动高度大于目标元素的位置，导航条显示
        if( scrollTop>=top-100){
            obj.className="fixed"
        }else{
            obj.className = "list";
        }
    }
}