import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return {x: [96, 125], y: [-144, -98]};
  // return {x: [20, 30], y: [-10, -5]};
};

const quadratic = (a, b, c) => {
  return Math.ceil(Math.max(
    (-1 * b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a),
    (-1 * b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  ));
};

const countMaxSteps = (velX, targetX) => {
  let steps = 0;
  let x = 0;
  while (x < targetX) {
    x += velX;
    velX--;
    steps++;
    if (velX === 0) return Infinity;
  }
  return steps;
}

const part1 = (path) => {
  const inputs = processInputs(path);
  const minX = quadratic(0.5, 0.5, -1 * inputs.x[0])
  const maxX = inputs.x[1];
  const maxY = inputs.y[0];
  for (let velX=minX; velX<=maxX; velX++) {
    const maxXSteps = countMaxSteps(velX, inputs.x[1]);
    for (let velY=Math.abs(maxY); velY>0; velY--) {
      if (maxXSteps === Infinity) {
        let thisVelY = -1 * velY;
        let thisY = 0;
        while (thisY > inputs.y[0]) {
          if (thisY >= inputs.y[0] && thisY <= inputs.y[1]) return (velY * (velY + 1)) / 2;
          thisY += thisVelY;
          thisVelY--;
        }
      } else {
        // This else block will need to be built out for some other inputs to work
      }
    }
  }

};

const part2 = (path) => {
  const inputs = processInputs(path);
  const minX = quadratic(0.5, 0.5, -1 * inputs.x[0])
  const maxX = inputs.x[1];
  const maxY = inputs.y[0];
  const velocities = [];
  for (let velX=minX; velX<=maxX; velX++) {
    for (let velY=Math.abs(maxY); velY>=inputs.y[0]; velY--) {    
        let thisVelX = velX;
        let thisVelY = velY;
        let x = 0;
        let y = 0;
        while (x <= inputs.x[1] && y >= inputs.y[0]) {
          x += thisVelX;
          y += thisVelY;
          if (thisVelX > 0) thisVelX--;
          if (thisVelX < 0) thisVelX++;
          thisVelY--;
          if (x >= inputs.x[0] 
            && x <= inputs.x[1] 
            && y >= inputs.y[0] 
            && y <= inputs.y[1]) {
              velocities.push(`${velX},${velY}`);
              break;
          }

        }
    }
  }
  return velocities.length;
};

export { part1, part2 };
