// 2) შექმენით .map-ის კლონი ფუნქცია.

// არ გამოიყენოთ .map

const numbers = [57, 23, 89, 11, 78, 36, 64, 5, 92, 44];

const newNumbers = numbers.map((curValue, index, curArray) => {
    if (index % 2 === 00) {
        return Math.floor(curValue / 2);
    } else {
        return curValue * 2
    }
})

console.log(newNumbers);

const func = (curValue, index, curArray) => {
    if (index % 2 === 0) {
        return Math.floor(curValue / 2)
    } 

    return curValue * 2;
}

const map = (array, func) => {
    const result = [];
    for (let i = 0; i < array.length; i++){
        result.push(func(array[i], i))
    }
}