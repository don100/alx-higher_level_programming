#!/usr/bin/node
exports.esrever = function (list) {
  listEsrever = [];
  for (let i of list) {
    listEsrever.unshift(i);
  }
  return listEsrever;
};
