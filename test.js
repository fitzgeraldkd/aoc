import { part1 as day13part1, part2 as day13part2 } from './13-transparent-origami/13-transparent-origami.js';

const puzzles = [
  {
    day: 13,
    title: 'Transparent Origami', 
    inputs: "./13-transparent-origami/inputs.txt", 
    parts: [
      {func: day13part1, solution: 708},
      {func: day13part2, solution: "#### ###  #    #  # ###  ###  #### #  #\n#    #  # #    #  # #  # #  # #    #  #\n###  ###  #    #  # ###  #  # ###  ####\n#    #  # #    #  # #  # ###  #    #  #\n#    #  # #    #  # #  # # #  #    #  #\n#### ###  ####  ##  ###  #  # #    #  #"}
    ]
  }
];

for (const puzzle of puzzles) {
  console.log(`Day ${puzzle.day} - ${puzzle.title}`);
  for (let i=0; i<puzzle.parts.length; i++) {
    const startTime = performance.now();
    const solution = puzzle.parts[i].func(puzzle.inputs);
    const endTime = performance.now();
    const runTime = ((endTime - startTime) / 1000).toFixed(4);
    const pass = solution===puzzle.parts[i].solution;
    console.log(`  Part ${i+1} (${pass ? 'PASS' : 'FAIL'}, ${runTime} sec):`);
    console.log(solution);
    console.log();
  }
}