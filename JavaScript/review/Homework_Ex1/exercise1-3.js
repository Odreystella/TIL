//3. for문을 사용하여 0부터 10미만의 정수 중에서 짝수 만을 작은 수부터 문자열로 출력하시오

var stringEven = '';

for (var i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        stringEven += i;
    }
}
console.log(stringEven);