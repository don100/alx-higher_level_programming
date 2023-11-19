#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  let nb = number+=1;
  theFunction(nb);
};
