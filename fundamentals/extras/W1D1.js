// /* 
//     Acronyms
//     Create a function that, given a string, returns the string’s acronym 
//     (first letter of each word capitalized). 
//     Do it with .split first if you need to, then try to do it without
//     SPLIT EXAMPLE:
//     var str = "Hello world"
//     str.split(" ") => ["Hello", "world"]
function acronym(str){
    var res = ""
     if(str[0] !== " "){
         res += str[0].toUpperCase()
     }

     for(var i = 0; i < str.length; i++){
         if(str[i] === " " && i + 1 <str.length){
          res += str[i + 1].toUpperCase()
         }
     
    }
     return res;
 }


console.log(acronym(" there's no free lunch - gotta pay yer way. "))
//     var str1 = " there's no free lunch - gotta pay yer way. ";
//     var expected1 = "TNFL-GPYW";
    
//     var str2 = "Live from New York, it's Saturday Night Live!";
//     var expected2 = "LFNYISNL";

//     HINT:
//     .toUpperCase()

//     * Turns the given str into an acronym.
//     * - Time: O(?).
//     * - Space: O(?).
//     * @param {string} str A string to be turned into an acronym.
//     * @returns {string} The given str converted into an acronym.
// */

/* 
    String: Reverse
    Given a string,
    return a new string that is the given string reversed

    var str1 = "creature";
    var expected1 = "erutaerc";

    var str2 = "dog";
    var expected2 = "god";


    * Reverses the given str.
    * - Time: O(?).
    * - Space: O(?).
    * @param {string} str String to be reversed.
    * @returns {string} The given str reversed.
*/
function reverseString(str1) {
  var res = "";
  for(var i = str1.length - 1; i >= 0; i--){
   res += str1[i];
  }
  return res;
}

console.log(reverseString("dog"))