import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync("inputs.txt", "utf8")
    .split("\n")
    .map(row => row.split('').map(value => parseInt(value)))
    // .map(item => parseInt(item, 10));
    // .map(item => item.trim());
};

class Node {
  constructor(data) {
    this.data = data
    this.edges = {};
  }
}

class Graph {

  constructor() {
    this.nodes = {};
    this.edges = {};
  }

  addNode(data) {
    this.nodes[data] = new Node(data)
  }

  addDirectedEdge(nodeA, nodeB, distance) {
    this.nodes[nodeA].edges[nodeB] = distance;
  }

  djikstraAlgorithm(startNode) {
    const prev = {};
    const distances = {};
    const queue = [{data: startNode, priority: 0}];

    for (const node in this.nodes) {
      distances[node] = Infinity;
    }
    distances[startNode] = 0;

    while (queue.length > 0) {
      // console.log(queue);
      const thisItem = queue.pop();
      const currData = thisItem.data;
      const weight = thisItem.priority;
      // const {currData, weight} = queue.pop();
      const currNode = this.nodes[currData];
      // console.log('test', this.nodes, currData, currNode)
      for (const neighbor in currNode.edges) {
        const alt = distances[currData] + currNode.edges[neighbor]
        if (alt < distances[neighbor]) {
          distances[neighbor] = alt;
          prev[neighbor] = currData;
          queue.push({data: neighbor, priority: distances[neighbor]})
        }
      }
      queue.sort((a, b) => {
        if (a.priority > b.priority) return -1;
        if (a.priority < b.priority) return 1;
        return 0
      });
    }
    return distances;
 }

};

const tileMap = (inputs) => {
  const tiled = [];
  for (let y=0; y<inputs.length; y++) {
    for (let z=0; z<5; z++) tiled[y+(inputs.length*z)] = [];
    for (let x=0; x<inputs[y].length; x++) {
      for (let i=0; i<5; i++) {
        for (let j=0; j<5; j++) {
          let value = inputs[y][x] + i + j;
          if (value > 9) value -= 9;
          tiled[y+(inputs.length*i)][x+(inputs[0].length*j)] = value;
        }
      }
    }
  }
  return tiled;
};


const part1 = (path) => {
  const inputs = processInputs(path);
  // console.log(inputs);
  const graph = new Graph;
  inputs.forEach((row, y) => row.forEach((col, x) => graph.addNode(`${x},${y}`)))
  for (let y=0; y<inputs.length; y++) {
    for (let x=0; x<inputs[y].length; x++) {
      if (x > 0) graph.addDirectedEdge(`${x},${y}`, `${x-1},${y}`, inputs[y][x-1]);
      if (y > 0) graph.addDirectedEdge(`${x},${y}`, `${x},${y-1}`, inputs[y-1][x]);
      if (x < inputs[y].length-1) graph.addDirectedEdge(`${x},${y}`, `${x+1},${y}`, inputs[y][x+1]);
      if (y < inputs.length-1) graph.addDirectedEdge(`${x},${y}`, `${x},${y+1}`, inputs[y+1][x]);
    }
  }
  // console.log(graph);
  const distances = graph.djikstraAlgorithm('0,0')
  console.log(distances[`${inputs[0].length-1},${inputs.length-1}`]);
};

const part2 = (path) => {
  const inputs = processInputs(path);
  const tiledInputs = tileMap(inputs);
  // console.log(inputs);
  const graph = new Graph;
  tiledInputs.forEach((row, y) => row.forEach((col, x) => graph.addNode(`${x},${y}`)))
  for (let y=0; y<tiledInputs.length; y++) {
    for (let x=0; x<tiledInputs[y].length; x++) {
      if (x > 0) graph.addDirectedEdge(`${x},${y}`, `${x-1},${y}`, tiledInputs[y][x-1]);
      if (y > 0) graph.addDirectedEdge(`${x},${y}`, `${x},${y-1}`, tiledInputs[y-1][x]);
      if (x < tiledInputs[y].length-1) graph.addDirectedEdge(`${x},${y}`, `${x+1},${y}`, tiledInputs[y][x+1]);
      if (y < tiledInputs.length-1) graph.addDirectedEdge(`${x},${y}`, `${x},${y+1}`, tiledInputs[y+1][x]);
    }
  }
  // console.log(graph);
  const distances = graph.djikstraAlgorithm('0,0')
  // console.log(tiledInputs)
  // console.log(tiledInputs.length)
  console.log(distances[`${tiledInputs[0].length-1},${tiledInputs.length-1}`]);
};

console.log(part1());
console.log(part2());

export { part1, part2 };