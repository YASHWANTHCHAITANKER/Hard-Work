// 1. ways to print in javascript
// console.log('Hello World');
// alert("this site may contains harmful content");
// document.write("This is script text by using document.write")

// 2. Javascript console API
// console.log('Hello World', 5 + 5, 'we can pass multiple argument in console.log');
// console.warn("this is warning by console.warn");
// console.error("error expected by console.error");
// console.clear();
// console.assert(4 == 9);

// 3. Javascript variables
// containers to store variables[variable]

// var num1 = 50;
// var num2 = 50;
// console.log(num1 + num2);

// 4. Data types in javascript
// numbers 
// var numb1 = 30;
// var numb2 = 20;

// string
// var str1 ="my first name is yashwanth";
// var str2 ='my last name is chaitanker';

// objects or keywords 
// var marks = {
//        yshwanth: 99,
//        karthik: 89.99,
//        rithik:90.87
// }
// console.log(numb1);
// console.log(numb2);
// console.log("sum of numb1 and numb2 is",numb1 + numb2);

// console.log(str1);
// console.log(str2);
// console.log(str1 + str2);

// console.log(marks);

// var a = true;
// var b = false;
/*var x = 16 , y = 15;
if(x>y)
{
       console.log(a);
}
else
{
       console.log(b);
}*/
// console.log(a , b);

// var und = undefined;
// console.log(und);

// var n = null;
// console.log(n);

/* In javascript we have two data types they are
1.Primitive data type: undefined, null, boolean, number, string, symbol
2.Reference data types: Arrays,Objects
*/

// var arr = [10,20,30,"yashwanth",50,"rithik"];
// console.log(arr);
// console.log(arr[3]);

// Operators in javascript
// Arithmetic
/*var a = 200;
var b = 100;
console.log("The value of a + b is",a+b);
console.log("The value of a - b is",a-b);
console.log("The value of a * b is",a*b);
console.log("The value of a / b is",a/b);*/

// Comparision Operator
/*var x = 50;
var y = 40;
console.log(x == y);
console.log(x <= y);
console.log(x >= y);
console.log(x > y);
console.log(x < y);*/

// Assignment Operator
/*var c = b;
c += 2;// c = c + 2
c -= 2;// c = c - 2
c /= 2;// c = c / 2
c *= 2;// c = c * 2*/
// console.log(c);

// Logocal opeartor
// [AND OR NOT]
// OR
/*console.log(true  || true)
console.log(true  || false)
console.log(false || true)
console.log(false || false)*/

// NOT
// console.log(!false);
// console.log(!true);

// Functions in Javascript
// function avg(a , b){
//        c = (a+b)/2;
//        return c;
// }
// c1 = avg(5,5);
// c2 = avg(45,35);
// console.log( "average of c1 is", c1 ,"average of c2 is", c2);

// Conditional in Javascript
// if ,if else,ifelse ladder
/*var a = 30 , b = 40;
if(a<b)
{
       console.log("a is greater than b"); //only if
}*/

/*if(a>b)
{
       console.log("a is greater than b");
}
else
{
       console.log("b is greater than a"); // if-else
}*/

// if-else Ladder
/*var age = 21;
if(age<=10)
{
       console.log("you are a kid your age is less than 10")
}
else if(age>=11 && age<=15)
{
       console.log("you are not a kid you are growing now your age is now 15");
}
else if(age>=16 && age<=20)
{
       console.log("you grown up now dont behave like a kid you are now 20");
}
else
{
       console.log("you are now gentelman");
}
console.log("end of ladder");*/

/*var a = ["yash","rithik","karthik","sahadev"];
// console.log(a);

for(i=0;i<a.length;i++)
{
       console.log(a[i]);
}*/
/*
a.forEach(element => {
       console.log(element);
});
*/


/*let j=3;

while(j<a.length)
{
       console.log(a[j]);
       j++;
}*/

/*
do{
       console.log(a[j]);
       j++;
}while(j<a.length);*/

/* // continue and break statements
for(i=0;i<a.length;i++)
{
       if(i==2)
       {
              // break;
              continue;
       }
       console.log(a[i]);

}*/

// Arrays Methods in JS
/*
let arr = ["Yash",9,true,null,undefined];
// console.log(arr.length);
// arr.pop(); // to remove element from array lastelement by default 
// arr.push("karan");// to add element in array add in last ny default
// arr.shift();//to remove first element of array
// arr.unshift("RAM");//to add element in first of array
console.log(arr.length);
console.log(arr);*/

// Strings Methods in Js
/*
let string1 = "am is ram bhakt jai shree ram";
// console.log(string1.length);// to find a length of JS
// console.log(string1.indexOf("ram"));to find a string in JS from first
// console.log(string1.lastIndexOf("ram"));// to find a string in JS from last
//  console.log(string1.slice(0,5));// slice methods in JS
d = string1.replace("am","Hanuman")
console.log(string1);
console.log(d);*/

// Dates in JS
/*
let todaysDate = new Date();
console.log(todaysDate);
console.log(todaysDate.getTime());
console.log(todaysDate.getFullYear());
console.log(todaysDate.getMonth());
console.log(todaysDate.getDate());
console.log(todaysDate.getHours());
console.log(todaysDate.getMinutes());
console.log(todaysDate.getSeconds());*/

// DOM[Document Object Model] in JS

// alert("Sabhi bhaiyo Ko Ram Ram \nChalo phir shuru kartha hai Javascript ka safar");
// console.log("Jai sri Ram!");
// window.console.log("console is a part of window and it is created by default in every browser");
// console.dir(document);
// console.log(document.body);
// console.log(document.body.childNodes[1]);
// console.dir(document.head);
// let a = document.getElementById("firstcontainer");
// console.dir(a);
// let b= document.getElementById("thirdcontainer");
// console.dir(b);
// let c = document.getElementsByClassName("container");
// console.dir(c);
// let d= document.getElementsByTagName("p");
// console.dir(d);
// let fstele = document.querySelector(".container");
// console.dir(fstele);
// let allele = document.querySelectorAll("p");
// console.dir(allele);
// let ele = document.querySelector("#click");
// console.dir(ele);
// let cns = document.querySelector("p");
// console.dir(cns);
// let a = document.querySelector("#thirdcontainer");
// thirdcontainer.innertext= "Jai bajrang bali";
// console.dir(a);
// let ele = document.querySelector("div");
// console.dir(ele);
// let a = document.querySelector("h1");
// console.dir(a);

// let heading = document.querySelector("h2");
// console.dir(heading);
// let a = document.querySelectorAll(".box");
// console.dir(a);
// // a[0].innerText="Box-1";
// // a[1].innerText="Box-2";
// // a[2].innerText="Box-3";
// let vab = 1;
// for(varr of a){
//        varr.innerText = `New unique value of Box-${vab++}`;
// }

// let Class= div[0].getAttribute("class");
// console.log(Class);

// let Class1= div[1].getAttribute("class");
// console.log(Class1);

// let Id = div[0].getAttribute("id");
// console.log(Id);

// let name = div[1].getAttribute("name");
// console.log(name);

// let name1 = div[1].setAttribute("name", "the Second one");
// console.log(name1);

// let class2 = div[0].setAttribute("class", "the first one");
// // console.log(class2);

let div= document.querySelectorAll("div");
console.log(div);

let Class = div[0];
Class.style.backgroundColor="aqua";
Class.style.fontSize="20px";
Class.innerText= "Hare ram hare ram, ram ram hare hare";

let class1 = div[1];
class1.style.backgroundColor="purple";
class1.style.color="white";
class1.style.fontSize="20px";
class1.innerText="Hare krishn hare krishn, krishn krishn hare hare"