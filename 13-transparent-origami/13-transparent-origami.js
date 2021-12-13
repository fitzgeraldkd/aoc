
import fs from 'fs';
// const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split("\n\n")
  .map((input, index) => {
    if (index === 0) {
      return input.split("\n").map(coord => coord.split(',').map(value => parseInt(value)))
    } else {
      return input.split("\n")
    }
  })
  // .map(item => parseInt(item, 10));
  // .map(item => item.trim());

// console.log(inputs);

const processInputs = () => {
  return fs.readFileSync("inputs.txt", "utf8")
  .split("\n\n")
  .map((input, index) => {
    if (index === 0) {
      return input.split("\n").map(coord => coord.split(',').map(value => parseInt(value)))
    } else {
      return input.split("\n")
    }
  });
}

const part1 = () => {
  const inputs = processInputs();
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

  let paper = [];
  for (const dot of inputs[0]) {
    paper.push(dot);
  }

  for (const foldAlong of inputs[1]) {
    paper = fold(paper, foldAlong)
    break;
  }

  return paper.length;
};

const results1 = part1(inputs);

console.log(results1);

const part2 = () => {
  const inputs = processInputs();
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
    const rows = [];
    for (const dot of paper) {
      if (rows[dot[1]]) {
        rows[dot[1]].push(dot[0])
      } else {
        rows[dot[1]] = [dot[0]]
      }
    }

    for (const row of rows) {
      const sorted = row.sort((a, b) => {
        if (a > b) return 1;
        if (a < b) return -1;
        return 0
      });
      let rowStr = '';
      while (sorted.length > 0) {
        if (sorted[0] === rowStr.length) {
          rowStr += '#';
          sorted.shift();
        } else {
          rowStr += '.';
        }
      }
      console.log(rowStr);
    }
  }

  let paper = [];
  for (const dot of inputs[0]) {
    paper.push(dot);
  }

  for (const foldAlong of inputs[1]) {
    paper = fold(paper, foldAlong)
  }

  console.log(paper);
  printPaper(paper);
  return paper.length;
};

const results2 = part2(inputs);

console.log(results2);

export { part1, part2 };