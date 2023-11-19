#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
let nbOccurences = 0;
for (let i of list) {
    if (i === searchElement) {
        nbOccurences += 1;
    }
}
return nbOccurences;
};
