/*
*Prime Gaps
*
*by Cameron
*/

//an array to store primes we have already check
//to save time when drawing new screens
var checkedPrimes=[];
var lastprime;

//a simple function  to check if a number is prime
var isPrime=function(x){
    
    //check to see if we have already computed whether
    //the number is prime or not
    if (checkedPrimes[x] !== undefined){
        //use the result we have stored in the array
        return checkedPrimes[x];
    }
    
    //we only need to check from i=2 to sqrt(x) for factors
    //to see if a number is prime
    var maxi=sqrt(x);
    for(var i=2;i<=maxi;i++){
        //check to see if i is a factor
        if (x%i === 0){
            //i is a factor so the number is not prime
            //store the result in our array and return false
            checkedPrimes[x]=false;
            return false;
        }
        
    }
    
    //if we reach here we have check all numbers from 2 
    //to sqrt(x) and haven't found a factor, so x must be 
    //prime
    //store the result in our array and return true
    checkedPrimes[x]=true;
    return true;
};

var sumgap;
var maxgap;
var num;
var topy;
var bottomy;
var leftx;
var rightx;
var xScale;
var yScale;
var lastplotx0;
var lastploty0;
var lastplotx1;
var lastploty1;
var lastplotx2;
var lastploty2;


var init=function(){
    sumgap=0;
    maxgap=0;
    num=2;
    topy=85;
    bottomy=topy+250;
    leftx=75;
    rightx=250+leftx;
    xScale= rightx-leftx;
    yScale= 25;
    lastprime=2;
    lastplotx0=leftx;
    lastploty0=bottomy;
    lastplotx1=leftx;
    lastploty1=bottomy;
    lastplotx2=leftx;
    lastploty2=bottomy;
    
};



//
//This function just draws the axes and text
//
var drawAxes=function(){
    background(200, 200, 200);
    
    fill(255, 255, 255);
    rect(leftx,topy,rightx-leftx,bottomy-topy);
    
    fill(0, 0, 175);
    textSize(25);
    text("Prime Gaps",leftx+60,topy-55);
    textSize(15);
    fill(0, 50, 255);
    text("Difference between last prime in BLUE",leftx,topy-35);
    textSize(15);
    fill(255, 0, 0);
    text("Average Prime Gap in RED",leftx,topy-20);
    textSize(15);
    fill(255, 0, 255);
    text("Maximum Prime Gap in PURPLE",leftx,topy-5);
    
    fill(200, 0, 240);
    textSize(15);
    text("Press SHIFT to PAUSE plotting",leftx+25,bottomy+40);
    text("Press DOWN to reset plotting",leftx+25,bottomy+60);
    
    
    fill(0, 0, 0);
    stroke(0, 0, 0);
    //y axis
    text(yScale,leftx-50,topy);
    text(0,leftx-50,bottomy);
    line(leftx,bottomy,leftx,topy);
    for(var i=1;i<=5;i++){
        stroke(0, 0, 0,100);
        line(leftx+i*(rightx-leftx)/5,bottomy,leftx+i*(rightx-leftx)/5,topy);
    }
    
    //x axis
    text(xScale,rightx,bottomy+20);
    text(0,leftx,bottomy+20);
    line(leftx,bottomy,rightx,bottomy);
    for(var j=1;j<=5;j++){
        stroke(0, 0, 0,100);
        line(leftx,bottomy+(topy-bottomy)*j/5,rightx,bottomy+(topy-bottomy)*j/5);
        
    }
    
};

init();
drawAxes();

var pauseplot=false;
var draw= function() {
    
    if(!pauseplot){
        
    
    
    if(isPrime(num)){
        //if the number is prime increment primesfound
        lastprime=num;
    }
    var primegap=num-lastprime;
    sumgap += primegap;
    var avggap = sumgap/(num-2+1);
    if (primegap > maxgap){
        maxgap=primegap;
    }
    //plot the (num, primegap) point on the graph
    //this stuff just makes it scale to the graph
    var plotx0= leftx+(rightx-leftx)*num/xScale;
    var ploty0= bottomy+(topy-bottomy)*primegap/yScale;
    stroke(0, 50, 255);
    
    line(lastplotx0,lastploty0,plotx0,ploty0);
    lastplotx0=plotx0;
    lastploty0=ploty0;
    
    //plot the (num, avggap) point on the graph
    //this stuff just makes it scale to the graph
    var plotx1= leftx+(rightx-leftx)*num/xScale;
    var ploty1= bottomy+(topy-bottomy)*avggap/yScale;
    stroke(255, 0, 0);
    strokeWeight(3);
    line(lastplotx1,lastploty1,plotx1,ploty1);
    strokeWeight(1);
    lastplotx1=plotx1;
    lastploty1=ploty1;
    
    //plot the (num, maxgap) point on the graph
    //this stuff just makes it scale to the graph
    var plotx2= leftx+(rightx-leftx)*num/xScale;
    var ploty2= bottomy+(topy-bottomy)*maxgap/yScale;
    stroke(255, 0, 255);
    strokeWeight(3);
    line(lastplotx2,lastploty2,plotx2,ploty2);
    strokeWeight(1);
    lastplotx2=plotx2;
    lastploty2=ploty2;
    
    
    //if our points starting going off the right of the
    //graph we rescale the graph
    if(num > xScale){
        xScale *= 2;
        maxgap=0;
        sumgap=0;
        num=2;
        lastprime=2;
        lastplotx0=leftx;
        lastploty0=bottomy;
        lastplotx1=leftx;
        lastploty1=bottomy;
        lastplotx2=leftx;
        lastploty2=bottomy;
        drawAxes();
    }
    
    //if our points starting going off the top of the
    //graph we rescale the graph
    if(primegap > yScale){
        yScale *= 2;
        maxgap=0;
        sumgap=0;
        num=2;
        lastprime=2;
        lastplotx0=leftx;
        lastploty0=bottomy;
        lastplotx1=leftx;
        lastploty1=bottomy;
        lastplotx2=leftx;
        lastploty2=bottomy;
        drawAxes();
    }
    
   //let's get a new point
    num++;
    
    }
    
    
};

var keyPressed=function(){
    if(keyCode === SHIFT){
        pauseplot=!pauseplot;
    }
    
    if(keyCode === DOWN){
        init();
        drawAxes();
    }
    
    
};
