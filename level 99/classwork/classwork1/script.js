// 1) გამოიყენეთ reduce რომ დათვალოთ list'ში მყოფი რიცხვების ჯამი


const list1 = [1, 2, 3, 4, 5];

const list1reduced = list1.reduce((res, cur) => {
    return res + cur
})
// 2) გამოიყენეთ reduce რომ დათვალოთ list'ში მყოფი რიცხვების ნამრავლი

const list2 = [1, 2, 3, 4, 5];

const list2reduced = list2.reduce((res, cur) => {
    return res * cur
})