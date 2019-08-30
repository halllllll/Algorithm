define("a", ["require", "exports", "fs"], function (require, exports, fs) {
    "use strict";
    exports.__esModule = true;
    var n = fs.readFileSync('/dev/stdin').toString();
    console.log("\u305D\u308C\u306F\u306D " + n);
});
