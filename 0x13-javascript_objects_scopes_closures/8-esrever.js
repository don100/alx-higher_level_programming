#!/usr/bin/node
exports.esrever = function (list) {
  const listEsrever = [];
  for (const i in list) {
    listEsrever.unshift(i);
  }
  return listEsrever;
};
