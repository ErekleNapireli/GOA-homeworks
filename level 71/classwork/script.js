// 1) წამოიღეთ ელემენტები getElementsByClassName'ის საშუალებით
let myp = document.getElementsByClassName('myp');

// 2) წამოიღეთ ელემენტი querySelector'ის მეშვეობით (ჯერ id, შემდეგ class)
let myp2 = document.querySelector('#myp');
let myp3 = document.querySelector('.myp');
<<<<<<< HEAD
// 3) წამოიღეთ js'ში img და შეუცვალეთ: src და width
let img = document.querySelector('#img');
img.src = 'img-src.jpg';
img.width = 100;

// 4) წამოიღეთ js'ში p და შეუცვალეთ: color, backgroundColor და fontSize
let p = document.querySelector('myp');
p.style.color = 'red';
p.style.backgroundColor = 'blue';
p.style.fontSize = '20px';


// 5) js'ის გამოყენებით, შექმენით ახალი p და textNode, შემდეგ textNode ჩასვით პარაგრაფში და პარაგრაფი ჩასვით html'ში მოცემულ div'ში
let textNode = document.createTextNode('blablabla');
let p2 = document.createElement('p');
p2.appendChild(textNode);
div.appendChild(p2);
=======

// 3) წამოიღეთ js'ში img და შეუცვალეთ: src და width
let img = document.querySelector('img');
img.src = 'img-src.jpg';
img.width = '100';

// 4) წამოიღეთ js'ში p და შეუცვალეთ: color, backgroundColor და fontSize
let p = document.querySelector('myp');
p.computedStyleMap.color = 'red';
p.computedStyleMap.backgroundColor = 'blue';
p.computedStyleMap.fontSize = '20px';

// 5) js'ის გამოყენებით, შექმენით ახალი p და textNode, შემდეგ textNode ჩასვით პარაგრაფში და პარაგრაფი ჩასვით html'ში მოცემულ div'ში

let textNode = document.createTextNode('blablabla')
let p2 = document.createElement('p')
p2.appendChild(textNode)
div.appendChild(p2)
>>>>>>> cf69593 (second commit)
