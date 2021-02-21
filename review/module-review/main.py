#from fibo import text
from fibo import binet as b
from fibo import rec as r
#from fibo import binet, rec
#from fibo import *

#하나의 패키지 안에서 여러개의 모듈을 불러낼 수 있음


#text= 'hello'
#print(text)

#result = binet.get_fibo(5)
result = b.get_fibo(5)
print('result with binet:', result)

#result = rec.get_fibo(6)
result = r.get_fibo(6)
print('result with rec:', result)
