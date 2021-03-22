//15. 삼각형 출력하기 - pattern 5

var line = 5;
var sumStar = '';

for (var i = 0; i < 5; i++) {
  for (var j = 1; j < line - i; j++ ) {
    sumStar += ' ';
  }
  for (var k = 0; k <= i; k++) {
    sumStar += '*';
  }
  for (var l = 0; l < i; l++) {
    sumStar += '*';        
  } 
  sumStar += '\n';
}
console.log(sumStar);