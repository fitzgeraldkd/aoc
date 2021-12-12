const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split("\n").map(row => row.split('-'))
  // .map(item => parseInt(item, 10));
  // .map(item => item.trim());

console.log(inputs);

const createMap = (paths) => {
  const map = {};
  for (const path of paths) {
    if (path[0] in map) {
      map[path[0]].push(path[1]);
    } else {
      map[path[0]] = [path[1]];
    }

    if (path[1] in map) {
      map[path[1]].push(path[0]);
    } else {
      map[path[1]] = [path[0]];
    }
  } 
  return map;
};

const part1 = (inputs) => {
  const map = createMap(inputs);
  console.log(map);
  const queue = map.start.map(point => ['start', point]);
  // const queue = [['start']];
  // console.log(queue);
  const completed = [];

  while (queue.length > 0) {
    // console.log(completed.length);
    // console.log('queue:',queue);
    // console.log('completed:',completed);
    const thisPath = queue.pop();
    // console.log(thisPath);
    // console.log(thisPath.at(-1))
    // console.log(map[thisPath.at(-1)])
    map[thisPath.at(-1)].forEach(newPoint => {
      // console.log(newPoint, thisPath);
      // console.log()

      if (!(thisPath.includes(newPoint) && newPoint === newPoint.toLowerCase())) {
        if (newPoint === 'end') {
          completed.push([...thisPath, newPoint]);
        } else {
          queue.push([...thisPath, newPoint])
        }
      }

      // if (thisPath.at(-1) === 'end' || (thisPath.includes(newPoint) && newPoint === newPoint.toLowerCase())) {
      //   if (newPoint !== 'start' && !completed.some(completePath => completePath.join('-') === thisPath.join('-'))) {
      //     completed.push([...thisPath]);
      //   }
      // } else {
      //   // console.log(newPoint, thisPath);
      //   queue.push([...thisPath, newPoint])
      // }
    });
  }
  // console.log(completed);
  const fullPaths = completed.filter(path => (
    path[0] === 'start' && path.at(-1) === 'end'
  ))
  // console.log(fullPaths)
  // const oneSmallCavePaths = fullPaths.filter(path => (
  //   path.reduce((prev, curr) => {
  //     if (curr !== 'start' && curr !== 'end' && curr === curr.toLowerCase()) {
  //       prev++;
  //     }
  //     return prev;
  //   }, 0) <= 1
  // ))
  return fullPaths.length;
};

// const results1 = part1(inputs);

// console.log(results1);

const getRevisitedTwice = (path) => {
  let points = {};
  for (const point of path) {
    if (point in points && point === point.toLowerCase()) {
      return point;
    } else {
      points[point] = 1;
    }
  }
};

const part2 = (inputs) => {
  const map = createMap(inputs);
  console.log(map);
  const queue = map.start.map(point => ['start', point]);
  // const queue = [['start']];
  // console.log(queue);
  const completed = [];

  while (queue.length > 0) {
    const thisPath = queue.pop();
    const revistedSmallCave = getRevisitedTwice(thisPath);
    map[thisPath.at(-1)].forEach(newPoint => {
      if (newPoint !== 'start' && !(revistedSmallCave && thisPath.includes(newPoint) && newPoint === newPoint.toLowerCase())) {
        if (newPoint === 'end') {
          completed.push([...thisPath, newPoint]);
        } else {
          queue.push([...thisPath, newPoint])
        }
      }
    });
  }
  console.log(completed);
  const fullPaths = completed.filter(path => (
    path[0] === 'start' && path.at(-1) === 'end'
  ))
  return fullPaths.length;

};

const results2 = part2(inputs);

console.log(results2);