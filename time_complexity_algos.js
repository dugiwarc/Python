 background(0, 0, 0);

// VIDEO COMING SOON - Brit, Nov 18th 2014

// Try improving the algorithm A so that it beats B in the worse case

 /** 
 * Primality Test
 * Goal: Check whether a number is prime or composite
 */
 /* big primes to test with
 546732534463
 9876432123421
 98764321234349
 54673257461630679457  
 */
 
 var numtest = 5467361;
 // Algorithm A step counter
 var Asteps = 1;
 // Algorithm B step counter
 var Bsteps = 1;

 /**
 * Trial Division Primality Test (slow method)
 * Input: a single integer we want to test (numtest)
 * Output: TRUE if prime, FALSE if composite
 * 
 * ABOUT: This is a very simple method of checking
 * if a number is prime. Given some number n, it checks if        
 * any integer (starting from 2 to the square root of n)
 * divides evenly into it.
 */ 
var isPrimeA = function(inputNum){
     Asteps = Asteps+2;
     // assume inputNum is prime
     var primeCheck = true;
    // loop until test <= square root of inputNum
    var upperBound = floor(sqrt(inputNum));

    for(var test = 2; test <= upperBound; test++){
        Asteps = Asteps+3;
    // check if test divides inputNum
        if (inputNum % test === 0){
        // found a factor!
        primeCheck = false;
        }
    
    } // end of loop
    // return TRUE or FALSE
    return primeCheck;
 };
 
  /**
 * Improved Trial Division (smarter method)
 * Input: a single integer we want to test (numtest)
 * Output: TRUE if prime, FALSE if composite
 * 
 * ABOUT: This attempts to reduce the number of steps
 * by using information about composite numbers. It also
 * returns as soon as it finds a witness.
 */ 
 var isPrimeB = function(inputNum){
     Bsteps = Bsteps+3;
     // assume inputNum is prime
     var primeCheck = true;
    // check if input num is divisible by 2
    if (inputNum % 2 === 0) {
    // if 2 return true (prime) otherwise return false 
        return (inputNum === 2);
    }
    var upperBound = floor(sqrt(inputNum));
    // loop until test <= square root of inputNum
    for(var test = 3; test <= upperBound; test += 2){
        Bsteps = Bsteps+3;
    // check if test divides inputNum
        if (inputNum % test === 0){
        // found a factor!
        return false;
        }
    
    } 
    // Didn't find factor, therfore return true 
    return true;
 };

 
// ***********DISPLAY***************** 

// ALGORITHM A
textSize(14);
fill (255, 238, 0);
text("Algorithm A",80,13);
fill (255, 255, 255);
textSize(16);
text(numtest+" is ",34,35);
// if prime output prime
if (isPrimeA(numtest) === true){
fill (22, 173, 224);
text("prime", 91, 55);    
}
// or else composite
else{
fill (222, 22, 22);
text("composite", 77, 55);    
}

// ALGORITHM B
textSize(14);
fill (255, 238, 0);
text("Algorithm B",269,13);
// output the number chosen + "is"
textSize(16);
fill(255, 255, 255);
text(numtest+" is ",205,35);

// if prime output prime
if (isPrimeB(numtest) === true){
fill (22, 173, 224);
text("prime", 261, 54);    
}
// or else output composite
else{
fill (222, 22, 22);
text("composite", 261, 54);    
}


// ***********END DISPLAY***************** 

// ***********Complexity Visualization***************** 

textSize(13);
// Algorithm A
fill(1+Asteps/5000, 100, 100);
rect(35,390 - Asteps/10000,150,1000);
fill(255, 247, 0);
text("# Steps: "+Asteps,48,389);

// Algorithm B
fill(1+Bsteps/10000, 100, 100);
rect(215,392 - Bsteps/10000,150,1000);
fill(255, 247, 0);
text("# Steps: "+Bsteps,239,388);


stroke(230, 51, 51);
strokeWeight(10);
line(0,81,462,81);
fill(255, 255, 255);
text("STEP LIMIT!",155,86);

// ***********END Complexity Visualization***************** 