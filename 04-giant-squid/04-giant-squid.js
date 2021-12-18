import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n\n")
    // .map((item, index) => (
    //   index === 0 ? item.split(',') : item.split("\n").map(row => (
    //     row.trim().replaceAll(/\s+/g, ' ').split(' ')
    //   ))
    // ));
    .map((item, index) => {
      if (index === 0) {
        return item.split(',');
      } else {
        const board = {};
        item.split("\n").forEach((row, y) => (
          row.trim().replaceAll(/\s+/g, ' ').split(' ').forEach((value, x) => (
            board[value] = {x, y}
          ))
        ));
        return board;
      }
    });
};

// const fs = require('fs');
// const inputs = fs
//   .readFileSync("inputs.txt", "utf8")
//   .split("\n")
//   // .map(item => parseInt(item, 10));
//   .map(item => item.trim());

// // console.log(inputs);



const part1 = (path) => {
  const [toDraw, boards] = processInputs(path);
  const drawn = [];
  console.log(toDraw);
  console.log(boards);
  while (toDraw.length > 0) {
    drawn.push(toDraw.shift());

  }
};

const part2 = (path) => {
  const [toDraw, boards] = processInputs(path);
};

const part1old = (path) => {
  const inputs = processInputs(path);
  const toDraw = inputs.shift().split(',').map(value => parseInt(value));
  inputs.shift();
  const boards = [];
  let newBoard = [];
  for (let i=0; i<inputs.length; i++) {
    if (newBoard.length === 5) {
      inputs.shift();
      boards.push(newBoard);
      newBoard = [];
    } else {
      newBoard.push(inputs.shift().replaceAll(/\s+/g, ' ').split(' ').map(value => parseInt(value)));
    }
  }
  // console.log(boards);
  // return boards;
  // console.log(toDraw);
  const drawn = [];
  let successBoard;
  while (toDraw.length > 0) {
    drawn.push(toDraw.shift());
    // console.log(drawn);
    for (const board of boards) {
      let boardCheck = [];
      for (const row of board) {
        boardCheck.push(row.map(value => drawn.includes(value)))
      }
      // console.log(boardCheck)
      // console.log(boardCheck);

      let successA = true;
      let successB = true;
      for (let y=0; y<boardCheck.length; y++) {
        successA = true;
        successB = true;
        for (let x=0; x<boardCheck[y].length; x++) {
          // console.log(boardCheck);
          if (!boardCheck[x][y]) successA = false;
          if (!boardCheck[y][x]) successB = false;
        }
        if (successA || successB) break;
      }
      let successC = true;
      let successD = true;
      for (let x=0; x<boardCheck.length; x++) {
        if (!boardCheck[x][x]) successC = false;
        if (!boardCheck[boardCheck.length - 1 - x][x]) successD = false;
      }
      // console.log(successA || successB || successC || successD)
      if (successA || successB ) {
        successBoard = board;
        // console.log(successBoard)
        let score = 0;
        successBoard.forEach((row) => {
          row.forEach(value => {
            if (!drawn.includes(value)) score += value;
          })
        })
        return score * drawn.pop();
        break;
      };
    }
  }
  return successBoard
};

// console.log(part1(inputs));
// const success = 

const part2old = (path) => {
  const inputs = processInputs(path);
  const toDraw = inputs.shift().split(',').map(value => parseInt(value));
  inputs.shift();
  const boards = [];
  let newBoard = [];
  for (let i=0; i<inputs.length; i++) {
    if (newBoard.length === 5) {
      inputs.shift();
      boards.push(newBoard);
      newBoard = [];
    } else {
      newBoard.push(inputs.shift().replaceAll(/\s+/g, ' ').split(' ').map(value => parseInt(value)));
    }
  }
  // console.log(boards);
  // return boards;
  // console.log(toDraw);
  const drawn = [];
  let wonBoards = [];
  let successBoard;
  let winningDraw;
  while (toDraw.length > 0) {
    drawn.push(toDraw.shift());
    // console.log(drawn);
    for (const board of boards) {
      if (wonBoards.includes(board)) continue;
      let boardCheck = [];
      for (const row of board) {
        boardCheck.push(row.map(value => drawn.includes(value)))
      }
      // console.log(boardCheck)
      // console.log(boardCheck);

      let successA = true;
      let successB = true;
      for (let y=0; y<boardCheck.length; y++) {
        successA = true;
        successB = true;
        for (let x=0; x<boardCheck[y].length; x++) {
          // console.log(boardCheck);
          if (!boardCheck[x][y]) successA = false;
          if (!boardCheck[y][x]) successB = false;
        }
        if (successA || successB) break;
      }
      let successC = true;
      let successD = true;
      for (let x=0; x<boardCheck.length; x++) {
        if (!boardCheck[x][x]) successC = false;
        if (!boardCheck[boardCheck.length - 1 - x][x]) successD = false;
      }
      // console.log(successA || successB || successC || successD)
      if (successA || successB ) {
        successBoard = board;
        wonBoards.push(board);
        winningDraw = [...drawn];
        // console.log(successBoard)
        // break;
      };
    }
  }
  // console.log(successBoard);
  // console.log(winningDraw);
  let score = 0;
  successBoard.forEach((row) => {
    row.forEach(value => {
      if (!winningDraw.includes(value)) score += value;
    })
  })
  return score * winningDraw.at(-1);
};

// console.log(part2(inputs));

export { part1, part2 };