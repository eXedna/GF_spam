const fs = require("fs");

const {dop, Getter} = require("./dop.js");

FB_PUBLIC_LOAD_DATA_ = Getter();

let answers = [];

FB_PUBLIC_LOAD_DATA_[1][1].forEach((element) => {
    let temp = [];
    try {
      element[4][0][1].forEach((ans) => {
        temp.push(ans[0]);
      });
    } catch {
    }   
    try {
      answers.push({
        'quest' : element[1],
        'id': element[4][0][0],
        'value': temp
      });
  }
    catch {
      console.log("pass element");
    }
  });

  for (val of answers) {
    if (!Array.isArray(val.value) || !val.value.length) {
      if (val.value == null) {
        val.value = " ";
        continue;
      }
      val.value = "LongAnswer";
    } else {
      answers.push({ id: val.id + "_sentinel", value: null });
    }
  }

console.log(answers);

fs.writeFileSync("inf.txt", JSON.stringify(answers))