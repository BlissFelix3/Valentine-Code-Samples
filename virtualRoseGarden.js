let x;
let y;
let petalLength;

function setup() {
  createCanvas(400, 400);
  x = width / 2;
  y = height / 2;
  petalLength = 100;
}
function draw() {
  background(255, 255, 255);
  fill(255, 0, 0);
  noStroke();
  for (let i = 0; i < 10; i++) {
    const angle = map(i, 0, 10, 0, TWO_PI);
    const petalX = x + petalLength * cos(angle);
    const petalY = y + petalLength * sin(angle);
    ellipse(petalX, petalY, 50, 80);
  }
}