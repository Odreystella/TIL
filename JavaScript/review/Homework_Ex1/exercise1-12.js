//12. 삼각형 출력하기 - pattern 2

var line = 5;
var sumStar = '';

for (var i = line; i > 0; i--) {
    for (j = 1; j < 6 - i; j++) {
        sumStar += ' ';        
    }
    for (var k = 0; k < i; k++) {
        sumStar += '*';
    }
    sumStar += '\n';
}
console.log(sumStar);