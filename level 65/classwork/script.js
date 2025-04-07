
// 1) განიხილეთ განსხვავებები და მსგავსებები python'ის dictionary'ებსა და js'ის object'ებს შორის
// pyhton-ში dictionary-ში key-ს და values ორივე ბრჭყალებში იწერება, ხოლო js-ში object-ში მხოლოდ value იწერება ბრჭყალებში. გამოძახება იგივენაირად ხდება როგორც python-ში და ასევე js-ში.
// 2) შექმენით რაიმე ობიექტი რომელსაც ექნება 3 property და ერთ-ერთი იქნება რაიმე მეთოდი
const Obj1 = {
    name: "Erekle",
    age: 14,
    greet: function(){
        console.log("Hello, my name is " + this.name);
    }
}

// 3) ახსენით რა განსხვავებაა ფუნქციასა და მეთოდს შორის (დეტალურად)
// ფუნქცია ასრულებს გარკვეულ მოქმედებას საერთოდ, ხოლო მეთოდი ასრულებს გარკვეულ მოქმედებას რაიმე object-ზე.
// 4) შექმენით person Object Constructor 3 property'ით
function Person(name, age, favColor){
    this.name = name;
    this.age = age;
    this.favColor = favColor;
}
// 5) შექმენით მანქანის Object constructor რომელსაც ექნება 5 property, აქედან ერთერთი აუცილებლად უნდა იყოს horsePower და კიდევ ერთი აუცილებლად მეთოდი რომელიც ამ horsePower'ს გაზრდის 100'ით 
function Car(brand, model, year, horsePower, color){
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.horsePower = horsePower;
    this.color = color;
    this.increaseHorsePower = function() {
        this.horsePower += 100;
    }
}



