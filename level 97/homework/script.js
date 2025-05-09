// 1. **Filter Prime Numbers**
//    - Create an array of numbers and use `filter()` to return only the prime numbers.
const list1 = [1, 2, 3, 4, 5];
const list1filtered = list1.filter((x) => {
    return x ** 2 
})
// 2. **Map to Object Conversion**
//    - Given an array of objects (e.g., users with `id` and `name`), use `map()` to create an array of strings that contains only the names.

// 4. **Filter Objects by Property**
//    - Given an array of objects representing products (each having a `name` and `price`), use `filter()` to return products that are cheaper than a certain value.

// 5. **Map Complex Transformations**
//    - Create an array of objects representing books (with `title` and `author`). Use `map()` to return an array of strings in the format: `"Title by Author"`.

// 6. **Filter Numbers Based on Multiple Conditions**
//    - Given an array of numbers, use `filter()` to return numbers that are both greater than 10 and divisible by 3.

// 7. **Modify Array of Objects (map)**
//    - Given an array of objects representing users with a `name` and `age`, use `map()` to return a new array where all users are considered adults (i.e., add a new `isAdult` property based on their age).

// 8. **Chaining map and filter**
//    - Create an array of numbers. First, use `filter()` to return numbers greater than 50. Then, use `map()` to halve those numbers.

// 9. **Log Word Frequencies (forEach)**
//    - Create an array of words. Use `forEach()` to create an object that tracks how many times each word appears in the array.

// 10. **Filter Objects by Nested Property**
//    - Given an array of objects representing cars (with nested objects for `brand` and `model`), use `filter()` to return only cars of a specific brand.