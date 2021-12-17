import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  // return fs
  //   .readFileSync(path, "utf8")
  //   .split("\n")
  //   // .map(item => parseInt(item, 10));
  //   // .map(item => item.trim());
  return {x: [96, 125], y: [-144, -98]};
  return {x: [20, 30], y: [-10, -5]};
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
  console.log(inputs);

  const minX = quadratic(0.5, 0.5, -1 * inputs.x[0])
  const maxX = inputs.x[1];
  const maxY = inputs.y[0];
  console.log(minX, maxX)
  for (let velX=minX; velX<=maxX; velX++) {
    const maxXSteps = countMaxSteps(velX, inputs.x[1]);
    console.log('Steps for vel', velX,':', countMaxSteps(velX, inputs.x[1]));
    for (let velY=Math.abs(maxY); velY>0; velY--) {
      console.log(maxXSteps);
      if (maxXSteps === Infinity) {
        console.log('test');
        let thisVelY = -1 * velY;
        let thisY = 0;
        while (thisY > inputs.y[0]) {
          if (thisY >= inputs.y[0] && thisY <= inputs.y[1]) return (velY * (velY + 1)) / 2;
          thisY += thisVelY;
          thisVelY--;
        }
      } else {

      }
    }
  }

};

const part2 = (path) => {
  const inputs = processInputs(path);
  // console.log(inputs);

  const minX = quadratic(0.5, 0.5, -1 * inputs.x[0])
  const maxX = inputs.x[1];
  const maxY = inputs.y[0];
  const velocities = [];
  // console.log(minX, maxX)
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
  // for (let velX=minX; velX<=maxX; velX++) {
  //   const maxXSteps = countMaxSteps(velX, inputs.x[1]);
  //   // console.log('Steps for vel', velX,':', countMaxSteps(velX, inputs.x[1]));
  //   for (let velY=Math.abs(maxY); velY>=inputs.y[0]; velY--) {
  //     // console.log(maxXSteps);
  //     if (maxXSteps === Infinity && velY >= 0) {
  //       // console.log('test');
  //       let thisVelY = -1 * velY;
  //       let thisY = 0;
  //       while (thisY > inputs.y[0]) {
  //         if (thisY >= inputs.y[0] && thisY <= inputs.y[1]) {
  //           if (!velocities.includes(`${velX},${velY}`)) velocities.push(`${velX},${velY}`);
  //           // break;
  //         };
  //         thisY += thisVelY;
  //         thisVelY--;
  //       }
  //     } else {
  //       let thisVelX = velX;
  //       let thisVelY = velY;
  //       let x = 0;
  //       let y = 0;
  //       while (x <= inputs.x[1] && y >= inputs.y[0]) {
  //         x += thisVelX;
  //         y += thisVelY--;
  //         if (thisVelX > 0) thisVelX--;
  //         if (thisVelX < 0) thisVelX++;
  //         if (x >= inputs.x[0] && x <= inputs.x[1] && y >= inputs.y[0] && y <= inputs.y[1]) {
  //           if (!velocities.includes(`${velX},${velY}`)) velocities.push(`${velX},${velY}`);
  //           // break;
  //         }
  //       }
  //     }
  //   }
  // }
  console.log(velocities);
  // console.log(velocities.map(pair => `${pair[0]},${pair[1]}`).sort());
  // console.log(velocities.map(pair => `${pair[0]},${pair[1]}`).sort().join(' ') === exampleResults.split(' ').sort().join(' '))
  return velocities.length;
};

const exampleResults = '23,-10 25,-9 27,-5 29,-6 22,-6 21,-7 9,0 27,-7 24,-5 25,-7 26,-6 25,-5 6,8 11,-2 20,-5 29,-10 6,3 28,-7 8,0 30,-6 29,-8 20,-10 6,7 6,4 6,1 14,-4 21,-6 26,-10 7,-1 7,7 8,-1 21,-9 6,2 20,-7 30,-10 14,-3 20,-8 13,-2 7,3 28,-8 29,-9 15,-3 22,-5 26,-8 25,-8 25,-6 15,-4 9,-2 15,-2 12,-2 28,-9 12,-3 24,-6 23,-7 25,-10 7,8 11,-3 26,-7 7,1 23,-9 6,0 22,-10 27,-6 8,1 22,-8 13,-4 7,6 28,-6 11,-4 12,-4 26,-9 7,4 24,-10 23,-8 30,-8 7,0 9,-1 10,-1 26,-5 22,-9 6,5 7,5 23,-6 28,-10 10,-2 11,-1 20,-9 14,-2 29,-7 13,-3 23,-5 24,-8 27,-9 30,-7 28,-5 21,-10 7,9 6,6 21,-5 27,-10 7,2 30,-9 21,-8 22,-7 24,-9 20,-6 6,9 29,-5 8,-2 27,-8 30,-5 24,-7';
// console.log(part1());
console.log(part2());

export { part1, part2 };


// console.log(exampleResults.split(' ').sort())

// attempted: 2369, 2371, 2451, 2532