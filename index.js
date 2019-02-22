function setup() {
  createCanvas(400, 400)
  background(0);
}

var x = 0
function draw() {
  background(0);
  strokeWeight (10);
  stroke(255)
  point (x, 100)

  x += 1
  x = x % width
}