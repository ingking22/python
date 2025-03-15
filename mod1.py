val = 10
pi = 3.141592
def randint(x):
	return 3 * x + 5
class Calcalator:
    # 객체생성시에 자동으로 실행되는 메서드 : 생성자
	def __init__(self, first, second):    # 멤버 변수에 초기 값을 주기 위한 메서드 
		self.first = first
		self.second = second

	def add(self):
		self.result = self.first + self.second
		return self.result

calc = Calcalator(10, 30)
