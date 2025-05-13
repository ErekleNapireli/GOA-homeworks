// 8 kyu
// https://www.codewars.com/kata/53dc54212259ed3d4f00071c

// https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
function findAverage(array) {
    let result = 0;
    
    for(const num of array) {
        result += num
    }
    
    if(array.length === 0) {
        return 0;
    }
    
    return return result / array.length;
    }

// https://www.codewars.com/kata/5513795bd3fafb56c200049e
function countBy(x, n) {
    const result = [];
    
    for(let i = 1; i <= n; i++) {
      result.push(i * x);
    }
    
    return result;
}
// https://www.codewars.com/kata/5a00e05cc374cb34d100000d
const reverseSeq = n => {
    const result = [];
    
    for(let i = n; i > 0; i--) {
        result.push(i);
    }
    
    return result;
};

// 6 kyu
// https://www.codewars.com/kata/5839edaa6754d6fec10000a2

function findMissingLetter(array) {
    const alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    for(let i = 0; i < array.length - 1; i++) {
    if(alphabet[alphabet.indexOf(array[i]) + 1] !== array[i + 1]) {
        return alphabet[alphabet.indexOf(array[i]) + 1];
        }
    }
    
}
