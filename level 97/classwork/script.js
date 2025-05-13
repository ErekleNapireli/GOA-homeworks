// შექმენით .forEach მეთდის კლონი

// არ გამოიყენოთ .forEach

const names = ["Liam", "Emma", "Noah", "Olivia", "Ava", "William", "Sophia", "James", "Isabella", "Benjamin"];

names.forEach((curValue, index) => {
    if(index % 2 === 0) {
        console.log(`${curValue} is on even index`);
    } else {
        console.log(`${curValue} is on odd index`);
    }
})

for (let i = 0; i < names.length; i++) {
    if (i % 2 === 0) {
        console.log(`${names[i]} is on even index`);
    } else {
        console.log(`${names[i]} is on odd index`);
    }
    console.log(`${names[i]} is on ${[i]} index`);
}
