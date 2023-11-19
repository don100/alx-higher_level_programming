#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;
  for (const i of list) {
    if (i === searchElement) {
      nbOccurences += 1;
    }
  }
  return nbOccurences;
};
