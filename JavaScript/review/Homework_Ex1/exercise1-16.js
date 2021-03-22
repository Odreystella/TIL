//16. 삼각형 출력하기 - pattern 6

var line = 5;
var sumStar = '';

for (var i = line; i > 0; i--) {
  for (j = 1; j < 6 - i; j++) {
    sumStar += ' ';        
  }
  for (var k = 0; k < i; k++) {
    sumStar += '*';
  }
  for (var l = 1; l < i; l++) {
    sumStar += '*';       
  }
  sumStar += '\n';
}
console.log(sumStar);