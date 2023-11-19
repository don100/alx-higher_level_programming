#!/usr/bin/node
exports.esrever = function (list) {
  const listEsrever = [];
  for (const i of list) {
    listEsrever.unshift(i);
  }
  return listEsrever;
};
