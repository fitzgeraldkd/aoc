import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n\n")
    .map((item, index) => {
      if (index === 0) {
        return item;
      } else {
        return item.replaceAll('.', '0').replaceAll('#', '1').split('\n').map(row => row.split('').map(val => parseInt(val, 10)));
      }
    })
    // .map(item => parseInt(item, 10));
    // .map(item => item.trim());
};

const addRow = (grid, top=true) => {
  const row = [];
  for (let i=0; i<grid[0].length; i++) {
    row.push(0);
  }
  return top ? [row, ...grid] : [...grid, row];
}

const addColumn = (grid, left=true) => {
  return grid.map(row => left ? [0, ...row] : [...row, 0])
}

const getCluster = (grid, x, y) => {
  if (x === 0) {
    grid = addColumn(grid);
    x++;
  }
  if (x === grid[0].length-1) grid = addColumn(grid, false);
  if (y === 0) {
    grid = addRow(grid);
    y++;
  }
  if (y === grid.length-1) grid = addRow(grid, false);

  let binary = '';
  [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]].forEach(pair => {
    binary += grid[y+pair[1]][x+pair[0]].toString();
  });
  return { grid, binary };
}

const enhance = (image, algorithm) => {
  image = addColumn(image);
  image = addColumn(image);
  image = addColumn(image, false);
  image = addColumn(image, false);
  image = addRow(image);
  image = addRow(image);
  image = addRow(image, false);
  image = addRow(image, false);
  const result = image.map(_ => []);
  for (let x=0; x<image[0].length; x++) {
    for (let y=0; y<image.length; y++) {
      const { binary } = getCluster(image, x, y);
      // console.log(binary);
      // console.log(parseInt(binary, 2));
      // console.log(result, y);
      result[y][x] = algorithm[parseInt(binary, 2)] === '#' ? 1 : 0;
    }
  }
  return result;
}

const countLight = (image) => {
  let total = 0;
  for (const row of image) {
    for (const val of row) {
      total += val;
    }
  }
  return total;
}

const printImage = (image) => {
  image.forEach(row => {
    console.log(row.join(''));
  })
}

const part1 = (path) => {
  const inputs = processInputs(path);
  // console.log(inputs);
  const algorithm = inputs[0];
  let image = inputs[1];
  image = addColumn(addColumn(addRow(addRow(image), false)), false);
  // console.log(image);
  // console.log(enhance(image, algorithm));
  image = enhance(image, algorithm);
  printImage(image);
  image = enhance(image, algorithm);
  printImage(image);
  return countLight(image);
};

const part2 = (path) => {
  const inputs = processInputs(path);

};

console.log(part1());
console.log(part2());

// console.log(getCluster(
//   [
//     [1,0,0,1,0],
//     [1,0,0,0,0],
//     [1,1,0,0,1],
//     [0,0,1,0,0],
//     [0,0,1,1,1]
//   ], 2, 2
// ))

export { part1, part2 };