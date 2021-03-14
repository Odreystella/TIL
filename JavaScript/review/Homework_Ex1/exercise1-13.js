//13. 삼각형 출력하기 - pattern 3

var line = 5;
var sumStar = '';

for (var i = line; i > 0; i--) {
    for (var j = 0; j < i; j++) {
        sumStar += '*';
    }
    sumStar += '\n';
}
console.log(sumStar);