#!/usr/bin/node
exports.esrever = function (list) {
  const listEsrever = [];
  for (let i of list) {
    listEsrever.unshift(i);
  }
  return listEsrever;
};
