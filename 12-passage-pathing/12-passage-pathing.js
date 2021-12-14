import fs from 'fs';

const processInputs = (path='inputs.txt') => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n")
    .map(row => row.split('-'));
};

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

const part1 = (path) => {
  const inputs = processInputs(path);
  const map = createMap(inputs);
  const queue = map.start.map(point => ['start', point]);
  const completed = [];

  while (queue.length > 0) {
    const thisPath = queue.pop();
    map[thisPath.at(-1)].forEach(newPoint => {
      if (!(thisPath.includes(newPoint) && newPoint === newPoint.toLowerCase())) {
        if (newPoint === 'end') {
          completed.push([...thisPath, newPoint]);
        } else {
          queue.push([...thisPath, newPoint])
        }
      }
    });
  }
  const fullPaths = completed.filter(path => (
    path[0] === 'start' && path.at(-1) === 'end'
  ))
  return fullPaths.length;
};

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

const part2 = (path) => {
  const inputs = processInputs(path);
  const map = createMap(inputs);
  const queue = map.start.map(point => ['start', point]);
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
  const fullPaths = completed.filter(path => (
    path[0] === 'start' && path.at(-1) === 'end'
  ))
  return fullPaths.length;

};

export { part1, part2 };