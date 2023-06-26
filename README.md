# Five Programming Problems

Inspired by [Five programming problems every Software Engineer should be able to solve in less than 1 hour](https://web.archive.org/web/20200414191515/http://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour). 

## Problem 1

> Write three functions that compute the sum of the numbers in a given
> list using a for-loop, a while-loop, and recursion.

[problem1.py](src/problem1.py)

## Problem 2

> Write a function that combines two lists by alternatingly taking
> elements. For example: given the two lists `[a, b, c]` and
> `[1, 2, 3]`, the function should return `[a, 1, b, 2, c, 3]`.

[problem2.py](src/problem2.py)

## Problem 3

> Write a function that computes the list of the first 100 Fibonacci
> numbers. By definition, the first two numbers in the Fibonacci
> sequence are 0 and 1, and each subsequent number is the sum of the
> previous two. As an example, here are the first 10 Fibonnaci
> numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

[problem3.py](src/problem3.py)

## Problem 4

> Write a function that given a list of non negative integers,
> arranges them such that they form the largest possible number. For
> example, given [50, 2, 1, 9], the largest formed number is 95021.

[problem4.py](src/problem4.py)

## Problem 5

> Write a program that outputs all possibilities to put + or - or
> nothing between the numbers 1, 2, ..., 9 (in this order) such that
> the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 =
> 100.

[problem5.py](src/problem5.py)

-----

Additional problems
-------------------

## Problem 6

> Write a program to determine if the parentheses (), the brackets [], and the braces {}, in
> a string are balanced.  
> For example:  
> {{)(}} is not balanced because ) comes before (  
> ({)} is not balanced because ) is not balanced between {} and similarly the { is not  
> balanced between ()  
> [({})] is balanced  
> {}([]) is balanced  
> {()}[[{}]] is balanced

[problem6.py](src/problem6.py)

## Problem 7

> Write a program to generate all potential anagrams of an input string.  
> For example, the potential anagrams of "biro" are  
> biro bior brio broi boir bori  
> ibro ibor irbo irob iobr iorb  
> rbio rboi ribo riob roib robi  
> obir obri oibr oirb orbi orib  

[problem7.py](src/problem7.py)

## Problem 8

```text
Validate credit card number by Luhn algorithm.

0.) Given a Credit card number: 79927398713

1.) Starting from the rightmost digit, double the value of every second digit:
 7    9    9    2    7    3    9    8    7    1    3
      *2        *2        *2        *2        *2       
============================
      18.       4.        6.       16.        2


2.) If doubling of a number results in a two digit number i.e greater than 9
    (e.g., 6 × 2 = 12), then add the digits of the product (e.g.,
    12: 1 + 2 = 3, 15: 1 + 5 = 6), to get a single digit number.)

 7    9    9    2    7    3    9    8    7    1    3
      *2        *2        *2        *2        *2       
 ============================
     18.        4.        6.       16.        2
 ============================
      9.        4.        6.        7.        2


3.) Now take the sum of all the digits.

 7    9    9    2    7    3    9    8    7    1    3
      *2        *2        *2        *2        *2       
 =============================
     18.        4.        6.       16.        2
 =============================
      9.        4.        6.        7.        2
 =============================
 7.    9.   9.   4.   7.   6.   9.   7.    7.   2.   3.     =.    70

4.) If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; else it is not valid.
```

[problem8.py](src/problem8.py)
