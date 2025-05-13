// 2) თავიდან გააკეთეთ დროის ამთვლელი მოწყობილობა, რომელიც გამოიტანს მხოლოდ წუთებს და წამებს

const myp = document.getElementById("myp");

let minutes = Number(prompt("Enter amount of minutes"));
let seconds = Number(prompt("Enter amount of seconds"));

const counter = setInterval(() => {
    if (String(seconds).length == 1 && String(minutes).length == 1){
        myp.textContent = `0${minutes}:0${seconds}`;
    } else if (String(seconds).length == 1){
        myp.textContent = `${minutes}:0${seconds}`;
    } else {
        myp.textContent(`{minutes}:${seconds}`);
    }
    if (minutes == 0 && seconds == 0){
        clearInterval(counter);
    }
    if (seconds == 0){
        seconds = 60;
        minutes -= 1;
    }
    seconds-= 1;

}, 1000)
// 3) setInterval'ის გამოყენებით შექმენით პროგრამა რომელიც დაიწყებს 0'იდან და ყოველ ნახევარ წამში გამოიტანს რიცხვებს (ყველა გამეორებაზე 1'ით გაიზრდება) როდესაც ეს ავა 15'ზე მაშინ გაჩერდეს setInterval


// 4) გამოიტანეთ 3 ბრძანება:
// console.log(1)
// console.log(2)
// console.log(3)
// 
// მაგრამ ისე ქენით რომ პროგრამის გაშვებიდან 1 წამში გამოიტანოს ჯერ 2'იანი, შემდეგ მეორე წამს გამოიტანოს 1'იანი და ბოლოს 3'იანი (გააკეთეთ setTimeout'ით)


setTimeout(() => {
    console.log(1)
}, 2000)
setTimeout(() => {
    console.log(2)
}, 1000)
setTimeout(() => {
    console.log(3)
}, 3000)



