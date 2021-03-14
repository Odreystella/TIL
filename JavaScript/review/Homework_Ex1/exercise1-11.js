//11. 삼각형 출력하기 - pattern 1

var line = 5;
var sumStar = '';

for (var i = 0; i < line; i++) {
    for (var j = 0; j <= i; j++) {
        sumStar += '*';
    }
    sumStar += ('\n');
}
console.log(sumStar);
