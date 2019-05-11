



// SCROLL DOWN FOR CODE. VIDEO COMING SOON

// Challenges & Questions:

// 1a. Speed up my method of building the primes[] array.
// 1b. How did I decide the size the primes[] array?

// 2. Can you turn this into a prime counting function?


background(0, 0, 0);
/*
 * Sieve of Eratosthenes Algorithm
 *
 * Input: upperBound (how far we look for primes)
 */
var sieve = function(upperBound) {

// ignore all input less than 2
    if (upperBound < 2){
        return;
    }
    
// build array to mark numbers with
var isComposite = [upperBound];

// array to hold primes (HOW DID I DECIDE THIS SIZE?)
var primes = [upperBound/log(upperBound)];

// mark 0, 1 as not prime
isComposite[0] = 1;
isComposite[1] = 1;

// loop from 2 to sqrt(upperBound)
for (var m = 2; m*m <= upperBound; m++){
    // if prime (ie !== 1)
    if (isComposite[m] !== 1){
      // now mark off all multiples starting at m^2
      for (var z = m*m; z <= upperBound; z += m){
        // mark position z as composite (ie. === 1) 
        isComposite[z] = 1;
      }
    }
}
// END OF SIEVE

// This is just a rough way to store primes in
// a separate array (this can be improved)
var p = 0;
// print all primes by scanning array
for (var h = 0; h <= upperBound; h++){
    // when you find a unmarked number
    if (isComposite[h] !== 1){
    // put it in the prime array
    primes[p] = h;
    // increment to next cell in array
    p++;
    }
}

// PRINT ARRAY
// this step isn't actually needed just for display
var b = 0;
var c = 15;
for (var a = 0; a <= 311; a++){
    b = b+40;
    textSize(20);
    // print out prime in position a from the array
    text(primes[a],b,c);
    if (b > 350){
    b = 0;
    c += 25;
    }
}

};


// CALL SIEVE FUNCTION (function is above)

draw = function() {
    // input how large a list of primes you need
    var primeLimit = 452;
    // call the sieve algorithm
    sieve(primeLimit);
    
};





