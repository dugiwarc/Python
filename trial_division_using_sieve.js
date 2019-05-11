
// SCROLL DOWN FOR CODE. VIDEO COMING SOON!

// Challenge question

// 1. Is it possible to improve this sieve method?



background(0, 0, 0);
 /** 
 * Primality Test
 * Goal: Check whether a number is prime or composite
 */
 /* big primes to test with
 4093082899
 10000500001
 99999199999

 546732534463
 */
 
 // NUMBER TO PERFORM PRIMALITY TEST ON: (change me!)
 var numtest = 160;
 
 // Algorithm A step counter
 var Asteps = 1;
  // Algorithm C step counter
 var Bsteps = 1;

 /**
  * trialDivision Algorithm
 *  (lazy method / skip multiples of 2)
 * 
 * Input: a single integer we want to test (numtest)
 * Output: TRUE if prime, FALSE if composite
 * 
 * ABOUT: This is a very simple method of checking
 * if a number is prime. Given some number n, it checks if        
 * any integer (starting from 3 to the square root of n)
 * skipping all multiples of 2.
 */ 
var trialDivision = function(inputNum){
    Asteps++;
    // assume inputNum is prime
    // var primeCheck = true; (not relevant anymore)
// make sure input is above 1
if (inputNum < 2){
    return 1;
}
    // check if input num is divisible by 2
    if (inputNum % 2 === 0) {
    // if 2 return true (prime) otherwise return false 
        return (inputNum === 2);
    }
    // loop until test <= square root of inputNum
    for(var test = 3; test*test <= inputNum; test += 2){
        Asteps++;
    // check if test divides inputNum
        if (inputNum % test === 0){
        // found a factor!
        return false;
        }
    
    } 
    // Didn't find factor, therfore return true 
    return true;
 };
 
   
/**
 * sieveDivision Algorithm
 * Sieve to sqrt(n) + Trial division
 * 
 * Input: a single integer we want to test (numtest)
 * Output: TRUE if prime, FALSE if composite
 * 
 * ABOUT: This algorithm first builds list of primes.
 * then does a trial divsion on primes up to the
 * square root of the input
 */ 
var sieveDivision = function(upperBound) {
Bsteps++;
// build array to mark
var isComposite = [upperBound];
// prime array counter
var p = 0;
// make sure input is above 1
if (upperBound < 2){
    return 1;
}
// loop from 2 to sqrt(upperBound)
for (var m = 2; m*m <= upperBound; m++){
    Bsteps++;
    // if prime (ie !== 1)
    if (isComposite[m] !== 1){
        // check if m divides upperBound
        if (upperBound % m === 0){
            // found prime divisor, therfore composite! 
            return false;
         }
      // now mark off all composites starting at m^2
      // which are multiples of m
      for (var z = m*m; z*z <= upperBound; z += m){
        Bsteps++;
        // mark position z as composite (1) 
        isComposite[z] = 1;
      }
    }
}

// must be prime
return true;
 };

 
// ***********DISPLAY STUFF BELOW***************** 

// TRIAL DIVISION
textSize(14);
fill (255, 238, 0);
text("Trial Division",64,13);
fill (255, 255, 255);
textSize(16);
text(numtest+"  ",63,35);

// make sure input is value
if (trialDivision(numtest) === 1){
fill (22, 173, 224);
text("N/A", 62, 55);    
}
// if prime output prime
else if (trialDivision(numtest) === true){
fill (22, 173, 224);
text("is prime", 62, 55);    
}
// or else composite
else{
fill (222, 22, 22);
text("is composite", 62, 55);    
}


// SIEVE DIVISION
textSize(14);
fill (255, 238, 0);
text("Sieve sqrt(n) + trial div",227,13);
// output the number chosen + "is"
textSize(16);
fill(255, 255, 255);
text(numtest+"  ",271,35);

// make sure input is value
if (sieveDivision(numtest) === 1){
fill (22, 173, 224);
text("N/A", 265, 55);    
}

else if (sieveDivision(numtest) === true){
fill (22, 173, 224);
text("is prime", 271, 54);    
}
// or else output composite
else{
fill (222, 22, 22);
text("is composite", 269, 54);    
}


// ***********END DISPLAY***************** 

// ***********Complexity Visualization***************** 

textSize(13);
// TRIAL DIVISION
fill(1+Asteps/5000, 100, 100);
rect(11,392 - Asteps/10000,186,1000);
fill(255, 247, 0);
text("# Steps: "+Asteps,59,389);

// SIEVE DIVISION
fill(1+Bsteps/10000, 100, 100);
rect(217,392 - Bsteps/10000,172,1000);
fill(255, 247, 0);
text("# Steps: "+Bsteps,261,388);

stroke(230, 51, 51);
strokeWeight(14);
line(0,81,400,81);
fill(255, 255, 255);
text("STEP LIMIT!",155,86);

// ***********END Complexity Visualization***************** 