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

function sum(x) {
  return x.reduce((total, num) => {return total + num}, 0)
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
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

var q
function generateQuestion() {
  
  q = new SimplifySum();

  katex.render(q.questionText(), question, {
    throwOnError: false
  });

  $("#x2").val('') 
  $("#x1").val('') 
  $("#x0").val('') 

  return q;
}

function updateAnswer() {
  let x2text = $("#x2").val()
  let x1text = $("#x1").val()
  let x0text = $("#x0").val()

  console.log(`${x2text}, ${x1text}, ${x0text}`)
  let str = `${xIndex (x2text, 2, true)} ${xIndex(x1text, 1, false)} ${xIndex(x0text, 0, false)}`
  katex.render(str, answer, {
    throwOnError: false
  });
}

function checkAnswers(a) {
  var a = []
  a = [parseInt($("#x2").val()) || 0, parseInt($("#x1").val()) || 0, parseInt($("#x0").val()) || 0]
  //console.log(a);
  if (q.checkAnswer(a)){
    $("#result").html("Correct")
    $("#result").removeClass('incorrect')
    $("#result").addClass('correct')

  } else {
    $("#result").html("Incorrect")
    $("#result").removeClass('correct')
    $("#result").addClass('incorrect')
  }
}

