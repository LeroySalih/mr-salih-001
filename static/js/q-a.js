class SimplifySum {

  constructor() {
    this.x2 =  [5 -getRandomInt(10), 5 - getRandomInt(10), 5 - getRandomInt(10)]
    this.x1 = [5 -getRandomInt(10), 5 - getRandomInt(10), 5 - getRandomInt(10)]
    this.x0 = [5 -getRandomInt(10), 5 - getRandomInt(10), 5 - getRandomInt(10)]
  }
  
  questionText () {
    let str = ''
    str += `${xIndex (this.x2[0], 2, true) } ` + `${xIndex (this.x1[0], 1, false) } ` + `${xIndex (this.x0[0], 0, false) } `
    str += `${xIndex (this.x2[1], 2, false) } ` + `${xIndex (this.x1[1], 1, false) } ` + `${xIndex (this.x0[1], 0, false) } `
    str += `${xIndex (this.x2[2], 2, false) } ` + `${xIndex (this.x1[2], 1, false) } ` + `${xIndex (this.x0[2], 0, false) }`
    console.log('question text')
    return str;
  }

  checkAnswer (a) {
    console.log(a[0], sum(this.x2), a[0] == sum(this.x2));
    return (a[0] == sum(this.x2) && a[1] == sum(this.x1) && a[2] == sum(this.x0) )
  }
}

// ax + b = c
class SolveEquation1 {

  constructor() {
    this.x =  5 -getRandomIntBetween(-9, 9)
    this.a =  5 -getRandomIntBetween(-9, 9)
    this.b =  5 -getRandomIntBetween(-9, 9)
    this.c =  (this.a * this.x) + this.b
  }
  
  questionText () {
    let str = ''
    str += `${xIndex (this.a, 1, true) } ` + `${xIndex (this.b, 0, false) } = ${(this.a * this.x) + this.b}` 
   
    return str;
  }

  checkAnswer (a) {
    console.log(`${this.x}, ${a}`)
    return (a == this.x )
  }


}

// b - 3x = c
class SolveEquation2 {

  constructor() {
    this.x =  5 -getRandomIntBetween(-9, 9)
    this.a =  5 -getRandomIntBetween(-9, 9)
    this.b =  5 -getRandomIntBetween(-9, 9)
    this.c =  this.b - (this.a * this.x)
  }
  
  questionText () {
    let str = ''
    str += `${xIndex (this.b, 0, true) } - ${xIndex (this.a, 1, false) } ` + ` = ${this.b} - ${(this.a * this.x)}` 
   
    return str;
  }

  checkAnswer (a) {
    console.log(`${this.x}, ${a}`)
    return (a == this.x )
  }


}

class QuestionTypes {
  constructor() {
    this.SIMPLIFY_SUM = 0
    this.SOLVE_LINEAR_1 = 1
    this.SOLVE_LINEAR_2 = 2
  }
}

let QUESTION_TYPES = new QuestionTypes(); //new QuestionTypes();

function sum(x) {
  return x.reduce((total, num) => {return total + num}, 0)
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function getRandomIntBetween(min, max) {
  return (Math.floor(getRandomInt(max - min) - ((max + min) / 2)));
}

// Reduce a fraction by finding the Greatest Common Divisor and dividing by it.
// taken from https://stackoverflow.com/a/4652513/1007028
function reduce(numerator,denominator){
  var gcd = function gcd(a,b){
    return b ? gcd(b, a%b) : a;
  };
  gcd = gcd(numerator,denominator);
  return [numerator/gcd, denominator/gcd];
}


function sign(val, isFirst) {
  if (val == '') return ''
  return (val > -1 && !isFirst) ? '+' + val  : val
}

function xIndex(c, e, isFirst) {
  
  if (c == '')  return ''
  if (c == 0) return ''
  if (e == 0) return sign(c, isFirst)
  if (e == 1 && c == 1 && isFirst) return `x`
  if (e == 1 && c == 1 && !isFirst) return `+x`
  if (e == 1 && c == -1 ) return `-x`
  if (e == 1  ) return `${sign(c, isFirst)}x`

  if (c == 1  ) return `x^${e}`
  if (c == -1  ) return `-x^${e}`
  

  return `${sign(c, isFirst)}x^${e}`
}




function generateQuestion(type) {
  
  switch (type) {
    case QUESTION_TYPES.SOLVE_LINEAR_1 : return new SolveEquation1();
    case QUESTION_TYPES.SOLVE_LINEAR_2 : return new SolveEquation2();
    case QUESTION_TYPES.SIMPLIFY_SUM : return new SimplifySum();
    default: return null;
  }
}






