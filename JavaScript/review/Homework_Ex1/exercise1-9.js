//9. 1부터 20미만의 정수 중에서 2또는 3의 배수인 수의 총합을 구하시오.

var sumNums = 0;

for (var i = 1; i < 20; i++) {
    if (i % 2 === 0 || i % 3 === 0) sumNums += i;
}
console.log(sumNums);