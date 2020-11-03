const {dop, Getter} = require("./dop.js");

FB_PUBLIC_LOAD_DATA_ = Getter();

var answers = [];

FB_PUBLIC_LOAD_DATA_[1][1].forEach((element) => {
    var temp = [];
    try {
      element[4][0][1].forEach((ans) => {
        temp.push(ans[0]);
      });
    } catch {
    }   
    answers.push({
      'id': element[4][0][0],
      'value': temp
    });
  });

for (var i = 0; i < answers.length; i++) {
    if (answers[i]['value'].length == 0) {
        answers[i]['value'] = "LongAnswer";
    };
}

console.log(answers);