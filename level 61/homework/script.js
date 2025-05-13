// 2) შედარების ოპერატორებზე გააკეთეთ 5-5 მაგალითი
console.log(12 === 12);
console.log(5 === 3 );
console.log(4 === 44);
console.log(17 ===17);
console.log(2 === 6);

console.log(4 > 5);
console.log(6 > 10);
console.log(10 > 22);
console.log(23 > 0);
console.log(4 > 3);

console.log(10 < 11);
console.log(11 < 20);
console.log(3 < 3);
console.log(34 < 10);
console.log(1 < 4);


// 3) კომენტარებით ახსენით, თუ რა არის alert, confirm, prompt
// alert არის ფუნქცია, რომელიც წყვეტს საიტის მუშაობას და მომხმარებელს ატყობინებს რაიმეს შესახებ, უმეტესად ეს ბაურზერებშია ჩაშენებული და გამოყენებული. confirm-იც ფანჯარით ამოდის როგორც alert მაგრამ ეს მომხმარებელს confirm ს აკეთებინებს. prompt ამოდის ფანჯარით როგორც alert და confirm მაგრამ მოხმარებელს შეუძლია შემოტანა input-ით მასში.
// 4) მომხარებელს გამოუტანეთ confirm box-ი, სადაც მას შეეკითხებით არის თუ არა ზრდასრული, თუ ის დააჭერს ok ღილას, გამოუტანეთ "You are adult", სხვა შემთხვევაში "You are kid"
if (confirm("Are you adult?")) {
    alert("You are adult");
} else{
    alert("You are kid");
}

// 5) კარგად გადიმეორეთ ნასწავლი მასალა