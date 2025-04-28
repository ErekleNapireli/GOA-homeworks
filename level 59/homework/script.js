// 2) შექმენით 3 ცვლადი, სამივეში მომხმარებელს შემოატანინეთ რაიმე რიცხვი და შემდეგ გამოიტანეთ მათი ჯამი
let num1 = Number(prompt("Enter first number: "));
let num2 = Number(prompt("Enter second number: "));
let num3 = Number(prompt("Enter third number: "));
alert(`Sum of the numbers is: ${num1 + num2 + num3}`);

// 3) შექმენით 2 ცვლადი, ორივეში მომხმარებელს შემოატანინეთ რაიმე წინადადება, შემდეგ შეაერთეთ და გამოიტანეთ console'ში
let smt1 = prompt("Enter a sentence: ");
let smt2 = prompt("Enter another sentence: ");
console.log(`${smt1} ${smt2}`);

// 4) ვინც ვერ გააკეთეთ, თავიდან შეეცადეთ გააკეთოთ მესამე საკლასო დავალება 
// 3) შექმენით რაიმე ფორმა, სადაც იქნება name input და submit ღილაკი (არ დაგავიწდეთ რომ name input'ს მისცეთ name attribute), გამოიყენეთ addEventListener იმისთვის რომ submit ღილაკზე დაჭერისას console'ში გამოიტანოს მომხმარებლის შემოტანილი სახელი
document.getElementById("form").addEventListener("submit", function(event){
    event.preventDefault();
    const name = document.getElementById("fname").value;
    const name2 = document.getElementById("lname").value;
    console.log(name + name2 )});
// 5) ახსენით რაში გვჭირდება name attribute'ები მეოთხე დავალებაში

// 6) + უყურეთ ჩანაწერს თავიდან