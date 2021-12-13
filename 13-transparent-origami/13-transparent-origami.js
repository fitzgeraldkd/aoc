import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs.readFileSync(path, "utf8")
  .split("\n\n")
  .map((input, index) => {
    if (index === 0) {
      return input.split("\n").map(coord => coord.split(',').map(value => parseInt(value)))
    } else {
      return input.split("\n")
    }
  });
};

const fold = (paper, foldAlong) => {
  const vert = foldAlong.includes('y=');
  const axis = parseInt(foldAlong.split('=')[1]);
  let newPaper = [];
  if (vert) {
    // fold up
    for (const dot of paper) {
      if (dot[1] > axis) {
        newPaper.push([dot[0], 2 * axis - dot[1]]);
      } else {
        newPaper.push(dot);
      }
    }
  } else {
    // fold left
    for (const dot of paper) {
      if (dot[0] > axis) {
        newPaper.push([2 * axis - dot[0], dot[1]]);
      } else {
        newPaper.push(dot);
      }
    }
  }
  newPaper = newPaper
    .map(coord => `${coord[0]},${coord[1]}`)
    .filter((v, i, a) => a.indexOf(v) === i)
    .map(coord => coord.split(',').map(value => parseInt(value)))
  return newPaper;
};

const printPaper = (paper) => {
  const printed = [];
  for (const dot of paper) {
    if (!printed[dot[1]]) {
      printed[dot[1]] = [];
    }
    printed[dot[1]][dot[0]] = '#'
  }
  printed.forEach(row => {
    for (let i=0; i<row.length; i++) {
      if (!row[i]) row[i] = ' '
    }
  });
  return printed.map(row => row.join('')).join("\n")
}

const part1 = (path) => {
  const inputs = processInputs(path);
  return fold([...inputs[0]], inputs[1][0]).length;
};

const part2 = (path) => {
  const inputs = processInputs(path);
  let paper = [...inputs[0]];

  for (const foldAlong of inputs[1]) {
    paper = fold(paper, foldAlong)
  }

  return printPaper(paper);
};

export { part1, part2 };