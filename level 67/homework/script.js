// 1)შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების მასივს და დააბრუნებს ამ რიცხვების ჯამს
function sumOfArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

// 2)მენით ფუნქცია, რომელიც მიიღებს რიცხვების მასივს და დააბრუნებს მის მინიმალურ და მაქსიმალურ მნიშვნელობებს.
function minMax(arr) {
    let minNum = arr[0];

    for(let i = 0; i < arr.length; i++) {
        if (arr[i] < minNum) {
        minNum = arr[i];
        }
    }

    let maxNum = arr[0];
    for(let i = 0; i < arr.length; i++) {
        if (arr[i] > maxNum) {
            maxNum = arr[i];
        }
    }
    return [minNum, maxNum];
}
console.log(minMax([1, 2, 3, 4, 5]));


// 3)დაწერეთ ფუნქცია, რომელიც შექმნის N სიგრძის მასივს შემთხვევითი რიცხვებით (1-100 შუალედში).
function createArr(num1, num2) {
    let num1 = Math.floor(Math.random() * 100) + 1;
    let num2 = Math.floor(Math.random() * 100) + 1;
}
console.log(createArr(num1, num2));
// 4)შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების მასივს და დააბრუნებს ახალ მასივს, სადაც ყველა ელემენტი იქნება მისი კვადრატი.
function squareArr(arr) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        newArr.push(arr[i] * arr[i]);
    }
    return newArr;
}
console.log(squareArr([1, 2, 3, 4, 5]));
// 5)დაწერეთ ფუნქცია, რომელიც მიიღებს რიცხვს და დააბრუნებს მის:

// Math.floor() გამოყენებით დამრგვალებულ მნიშვნელობას
// Math.ceil() გამოყენებით დამრგვალებულ მნიშვნელობას
// Math.round() გამოყენებით დამრგვალებულ მნიშვნელობას
function mixture(num) {
    return Math.floor(num), math.ceil(num), Math.round(num);
}