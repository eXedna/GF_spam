var FB_PUBLIC_LOAD_DATA_ = [null,[null,[[79120055,"Имя?",null,0,[[1508740013,null,1]
]
]
,[908037449,"Тебе 2?",null,2,[[347858582,[["Да",null,null,null,0]
,["Нет",null,null,null,0]
]
,1,null,null,null,null,null,0]
]
]
,[213297711,"Почаму тебе 2?",null,1,[[297670832,null,1]
]
]
]
,null,null,null,[0,0]
,null,[1,"SHUT UP"]
,"Куку",48,[null,null,null,null,0]
,null,null,null,null,[2]
]
]

var ans_props = [];
var status = "FormatAnswer";
var id = 0;
var _ans = [];
                              
for (var i = 0; i < 3; i++) {
    id = FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][0];

    if ((FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][1] == null) && (FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][2] == 1)) {
        status = "Long answer";
        ans_props.push({"id":id, "status":status});
    }
    else {
        for (var k = 0; k < FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][1].length; k++) {
            _ans.push(FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][1][k][0]);
        }
        ans_props.push({"id" : id, "status" : _ans});
    }
}

console.log(ans_props)