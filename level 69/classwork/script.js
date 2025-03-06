// 1) შექმენით ცვლადი სადაც შეინახავთ ახლანდელ Date'ს
const currentDate = new Date();
console.log(currewntDate)
// 2) ჯერ გამოიტანეთ ეს ცვლადი, შემდეგ კი გამოიყენეთ და გამოიტანეთ ყველა მეთოდი რომელიც რესურსებშია ჩაგდებული
console.log(currentDate.getFullYear());
console.log(currentDate.getMonth());
console.log(currentDate.getDate());
console.log(currentDate.getDay());
console.log(currentDate.getHours());
console.log(currentDate.getMinutes());
console.log(currentDate.getSeconds());
console.log(currentDate.getMilliseconds());
// 3) გააკეთეთ დროის ამთვლელი პროგრამა, html + js'ით, ისეთი როგორიც მე გავაკეთე

setInterval(() => {
    const now = new Date();
    let hours = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();
    const clock1 = hours + ":" + minutes + ":" + seconds;

    document.getElementById("myp").textContent = clock1;
},1000);