import * as fs from "fs";
const n: string = fs.readFileSync('/dev/stdin').toString();
console.log(`それはね ${n}`);
