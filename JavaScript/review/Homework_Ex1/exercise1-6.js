//6. while문을 사용하여 0부터 10미만의 정수 중에서 짝수만을 큰 수부터 출력하시오.

var i = 10;

while (i >= 0) {
    if (i % 2 === 1) {
        console.log(i);
    }       
    i--;
}