// 1) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade (ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)

let score = Number(prompt("Enter your grade (10-100): "));

if (score >= 90) {
    alert("Grade A");
} else if (score >= 80 && score <= 89) {
    alert("Grade B");
} else if (score >= 70 && score <= 79) {
    alert("Grade C");
} else if (score >= 60 && score <= 69) {
    alert("Grade D");
} else if (score >= 0 && score <= 59) {
    alert("Grade F");
}


// 2) მომხმარებელს შემოატანინეთ საკუთარი ასაკი, თუ იქნება 13 წელზე ნაკლების გამოუტანეთ You are kid, თუ იქნება 18 წელზე ნაკლების მაგრამ 13'ზე მეტის გამოუტანეთ You are not adult yet და თუ იქნება 18 წელზე მეტის გამოუტანეთ You are adult

let age = Number(prompt("Enter your age: "))

if (age < 13) {
    alert("You are kid");
} else if (age < 18 && age > 13){
    alert("You are not adult yet");
} else if (age > 18 && age == 18){
    alert("You are adult");
}

// 3) დაწერეთ მეორე დავალება პითონის კოდითაც და შემდეგ შეადარეთ js'ით დაწერილ კოდს, ამოწერეთ სინტაქსური განსხვავებები
// js-ში გვაქვს ცვლადის შენახვის 3 გზა (let,const,var) ხოლო პითნში მხოლოდ ერთი. js-ში ვიყენებთ block-ს რომ ალერტი გამოვიტანოთ ამა თუ იმ შემთხვევაში ხოლო პითნში print-ს, ორ წერტილს და ინდენტაციის მეშვეობით.js-ში ინდენტაცია არ არის სავალდებულო. ასევე python-სი and-ს ვიყენებთ, ხოლო js-ში &&. 

// 4) შექმენით while loop'ი რომელიც გამოიტანს რიცხვებს 0'დან 100'ის ჩათვლით
for (let i = 0; i <101; i++){
    console.log(i);
}

// 5) შექმენით for loop'ი რომელიც გამოიტანს რიცხვებს 5'დან 10'ის ჩათვლით
for (let x = 5; x <11; x++){
    console.log(x);
}