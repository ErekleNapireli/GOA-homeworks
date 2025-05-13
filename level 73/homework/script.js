// 2) კომენტარებით ახსენით, რა არის scope JavaScript-ში
// scope წყვეტს თუ სად შეგვიძლია ცვლადის გამოყენება, js-ში გვაქვს 3-ნაირი scope. ესენია: block scope,function scope & global scope. block scope იყენებს let & const keyword-ებს, იგი თავსდება {} ბლოკში და მის გარედან გამოყენება არ შეიძლება. function scope არის scope რომელიც ფუნქციას აქვს და ფუნქციაში მოქმედებს შექმნილი ცვლადები. ის იყენებს var, let & const keyword-ებს. global scope არის ცვლადი რომელიც ფუნქციის გარეთ არის შექმნილი და ყველგან შეგვიძლია მისი გამოყენება 
// 3) კომენტარებით ახსენით, რა არის hoisting-ი
// js-ში შეგვიძლია რომ ცვლადს მნიშვნელობა მივანიჭოთ გამოძახების მერე ან ჯერ მივანიჭოთ მნიშვნელობა და შემდეგ მივცეთ ჩვლადის ტიპი ანუ გამოვიყვანოთ

// შექმენით მსგავსი საიტი, აუცილებლად უნდა ჰქონდეს ფუნქციონალი:
// https://www.frontendmentor.io/challenges/tip-calculator-app-ugJNGbJUX

const form = document.getElementById("form");
const tipAmount = document.getElementById("tip amount")
const total = document.getElementById("total")
const reset = document.getElementById("reset")

form.addEventListener('submit', function(e){
    e.preventDefault();

    const bill1 = form.elements.bill;
    const tip1 = form.elements.tip;
    const people1 = form.elements.people;

    tipAmount.textContent = `Tip amount / person: $${String(Number(bill1.value) * Number(tip1.value) / 100 / (people1.value)).slice(0,4)}`;

    total.textContent = `Tip amount / person: $${String((Number(bill1.value) + Number(bill1.value) * Number(tip1.value) / 100) / Number(people1.value)).slice(0,5)}`;
})

reset.addEventListener('click', function(){
    tipAmount.textContent = "Tip amount / person: $0";
    total.textContent = "Total / person: $0";
})

