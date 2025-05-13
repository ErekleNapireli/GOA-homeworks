// 1) პირველი ვერსიით გააკეთეთ იგივენაირი ანიმაცია, მაგრამ საათის ისრის მიმართულების მაგივრად ყუთმა იმოძრაოს საათის ისრის მიმართულების საწინააღმდეგოდ


const child = document.getElementById('child');

let x = 0;
let y = 0; 

const moveDown = setInterval(() => {
    y += 1;
    child.style.top = `${y}px`;
    if (y == 450) {
        clearInterval(moveDown);
        const moveRight = setInterval(() => {
            x += 1;
            child.style.left = `${x}px`;
            if (x == 450) {
                clearInterval(moveRight);
                const moveUp = setInterval(() => {
                    y -= 1;
                    child.style.top = `${y}px`;
                    if (y == 0) {
                        clearInterval(moveUp);
                        const moveLeft = setInterval(() => {
                            x -= 1;
                            child.style.left = `${x}px`;
                            if (x == 0) {
                                clearInterval(moveLeft);
                            }
                        }, 5);
                    }
                }, 5);
            }
        }, 5);
    }
}, 5);

// second version


let direction = "right";

const move = setInterval(function(){
    if(direction == "bottom"){
        y--;
        if(top == 450){
            direction = "right";
        }
    } else if(direction == "right"){
        x++;
        if(x == 450){
            direction = "left";
        }
    } else if(direction == "left"){
        left--;
        if(left == 0){
            direction = "top";
        }
    } else{
        y--;
        if(y == 0 && left == 0){
            direction = "right";
        }
    }

    child.style.left = x + 'px';
    child.style.top = y + 'px';
}, 5);