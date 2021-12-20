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

const addRow = (grid, top=true, value=0) => {
  const row = [];
  for (let i=0; i<grid[0].length; i++) {
    row.push(value);
  }
  return top ? [row, ...grid] : [...grid, row];
}

const addColumn = (grid, left=true, value=0) => {
  return grid.map(row => left ? [value, ...row] : [...row, value])
}

const getCluster = (grid, x, y, infinitePixels) => {
  if (x === 0) {
    grid = addColumn(grid, true, infinitePixels);
    x++;
  }
  if (x === grid[0].length-1) grid = addColumn(grid, false, infinitePixels);
  if (y === 0) {
    grid = addRow(grid, true, infinitePixels);
    y++;
  }
  if (y === grid.length-1) grid = addRow(grid, false, infinitePixels);

  let binary = '';
  [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]].forEach(pair => {
    binary += grid[y+pair[1]][x+pair[0]].toString();
  });
  return { grid, binary };
}

const enhance = (image, algorithm, infinitePixels) => {
  image = addColumn(image, true, infinitePixels);
  image = addColumn(image, true, infinitePixels);
  image = addColumn(image, false, infinitePixels);
  image = addColumn(image, false, infinitePixels);
  image = addRow(image, true, infinitePixels);
  image = addRow(image, true, infinitePixels);
  image = addRow(image, false, infinitePixels);
  image = addRow(image, false, infinitePixels);
  const result = image.map(_ => []);
  for (let x=0; x<image[0].length; x++) {
    for (let y=0; y<image.length; y++) {
      const { binary } = getCluster(image, x, y, infinitePixels);
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
  let infinitePixels = 0;

  image = enhance(image, algorithm, infinitePixels);
  if (algorithm[0] === '#') infinitePixels = infinitePixels === 0 ? 1 : 0;
  printImage(image);

  image = enhance(image, algorithm, infinitePixels);
  if (algorithm[0] === '#') infinitePixels = infinitePixels === 0 ? 1 : 0;
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