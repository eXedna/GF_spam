var FB_PUBLIC_LOAD_DATA_ = [null,["Н.",[[963410975,"В каком вы классе:",null,3,[[447101162,[["8",null,null,null,0]
,["9",null,null,null,0]
,["10",null,null,null,0]
,["11",null,null,null,0]
]
,1,null,null,null,null,null,0]//[1][1][i][4][0][1] || [1][1][i][4][0][1][0][0]
]//[1][1][i][4][0][0]
]
,[2144473353,"1. Понятна ли вам система распределения по группам?",null,5,[[635193400,[["1"]
,["2"]
,["3"]
,["4"]
,["5"]
,["6"]
,["7"]
,["8"]
,["9"]
,["10"]
]
,1,["вообще непонятно","все понятно"]
]
]
]
,[1402835932,"2. Насколько удобно новое расписание?",null,5,[[1625556646,[["1"]
,["2"]
,["3"]
,["4"]
,["5"]
,["6"]
,["7"]
,["8"]
,["9"]
,["10"]
]
,1,["вообще неудобно","очень удобно"]
]
]
]
,[501208012,"3. Насколько комфортно учиться в новых группах? ",null,5,[[24742125,[["1"]
,["2"]
,["3"]
,["4"]
,["5"]
,["6"]
,["7"]
,["8"]
,["9"]
,["10"]
]
,1,["вообще некомфортно","очень комфортно"]
]
]
]
,[1804259344,"4. С какой скоростью вы и группа проходите материал?",null,5,[[731997419,[["1"]
,["2"]
,["3"]
,["4"]
,["5"]
,["6"]
,["7"]
,["8"]
,["9"]
,["10"]
]
,1,["очень медленно","очень быстро"]
]
]
]
,[607919092,"5. Насколько вы продуктивны при таком расписании?",null,5,[[877852689,[["1"]
,["2"]
,["3"]
,["4"]
,["5"]
,["6"]
,["7"]
,["8"]
,["9"]
,["10"]
]
,1,["вообще непродуктивен","очень продуктивен"]
]
]
]
,[1922464119,"6. Оцените дисциплину на уроках в новых группах",null,5,[[325369499,[["1"]
,["2"]
,["3"]
,["4"]
,["5"]
,["6"]
,["7"]
,["8"]
,["9"]
,["10"]
]
,1,["очень низкая","очень высокая"]
]
]
]
,[1235158557,"7. Насколько понятны объяснения преподавателей?",null,5,[[1508918824,[["1"]
,["2"]
,["3"]
,["4"]
,["5"]
,["6"]
,["7"]
,["8"]
,["9"]
,["10"]
]
,1,["абсолютно непонятны","все понятно"]
]
]
]
,[987367490,"8. Расписание по классам вам нравилось больше?",null,5,[[1003945292,[["1"]
,["2"]
,["3"]
,["4"]
,["5"]
]
,1,["совершенно не согласен","полностью согласен"]
]
]
]
,[226470489,"Какие проблемы были при расписании по классам?",null,1,[[1043893031,null,0]
]
]
,[887741073,"А как можно улучшить индивидуальное расписание?",null,1,[[806414291,null,0]
]
]
,[41066253,"Если у вас остались комментарии, пожелания, замечания и предложения, поделитесь с нами:",null,1,[[1293916860,null,0]
]
]
]
,["Спасибо, что поделились своим мнением!",1,0,0,0]
,null,[null,null,null,null,null,[null,null,null,[63,81,181,null,2]
,[197,203,233,null,1]
,0]
]
,[0,0]
,null,null,"Обратная связь по расписанию",48,[1,0,null,null,0]
,null,null,null,null,[2]
,[[1,1,1,1,1]
,1]
]
]



var ans_props = [];
var status = "FormatAnswer";
var id = 0;
var _ans = [];
                              
for (var i = 0; i < 12; i++) {
    id = FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][0];

    if (((FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][1] == null) && (FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][2] == 1)) || 
        ((FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][1] == null) && (FB_PUBLIC_LOAD_DATA_[1][1][i][4][0][2] == 0))) {
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

// for (var i = 0; i < FB_PUBLIC_LOAD_DATA_[1][1].length; i++) {
//     console.log(FB_PUBLIC_LOAD_DATA_[1][1][i])
// }

console.log(ans_props)