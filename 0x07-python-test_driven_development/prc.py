"""
def add_integer(a, b=98):
	if a is type(float):
		a = int(a)
	if b is type(float):
		b = int(b)
	if isinstance(a, int):
		if isinstance(b, int):
			return a + b
		else:
			raise TypeError("b must be an integer")
	else:
		raise TypeError("a must be an integer")
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
def matrix_divided(matrix, div):
	#msg ="matrix must be a matrix (list of lists) of integers floats"
	for i in matrix:
		if not type(i) == list:
			raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
		for j in i:
			if type(j) not in [int, float]:
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	leng = len(matrix[0])
	for i in matrix:
		if len(i) != leng:
			raise TypeError("Each row of the matrix must have the same size")
	if not isinstance(div, (float, int)):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")
	new = [list(map(lambda x: round(x / 2, 2), i)) for i in matrix]
	return new
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
def say_my_name(first_name, last_name=""):
	if not type(first_name) == str or not type(last_name) == str:
		raise TypeError("first_name must be a string or last_name must be a string")
	else:
		print("my name is {} {}".format(first_name, last_name))
say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
def print_square(size):
	if isinstance(size, int):
		if size >= 0:
			for i in range(size):
				[print('#', end='') for i in range(size)]
				print()
		else:
			raise ValueError("size must be >= 0")
	else:
			raise TypeError("size must be an integer")
print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")
def text_indentation(text):
	leng = len(text)
	i = 0
	while i < leng:
		print(text[i], end='')
		if text[i] in [':', '.', '?']:
			print('\n')
			if i + 1 == leng:
				break
			if i < leng and text[i + 1] == ' ':
				i += 1
		i += 1		
text_indentation(\"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres\""")
def max_integer(list=[]):
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
"""
def matrix_mul(m_a, m_b):

	if m_a == [[]]:
		raise ValueError("m_a can't be empty")
	if m_b == [[]]:
		raise ValueError("m_b can't be empty")

	if not type(m_a) == list:
		raise TypeError("m_a must be a list")
	if not type (m_b) == list:
		raise TypeError("m_b must be a list") 

	for i in m_a:
		if not type(i) == list:
			raise TypeError("m_a must be a list")
		if len(i) == 0:
			raise ValueError("m_a can't be empty")
		if len(i) != len(m_a[0]):
			raise TypeError("each row of m_a must be of the same size")
		for j in i:
			if type(j) not in [int, float]:
				raise TypeError("m_a should contain only integers or floats")
		
	for i in m_b:
		if not type(i) == list:
			raise TypeError("m_b must be a list")
		if len(i) == 0:
			raise ValueError("m_b can't be empty")
		if len(i) != len(m_b[0]):
			raise TypeError("each row of m_b must be of the same size")
		for j in i:
			if type(j) not in [int, float]:
				raise TypeError("m_b should contain only integers or floats")

	if len(m_a[0]) != len(m_b):
		raise ValueError("m_a and m_b can't be multiplied")


matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
matrix_mul([[1, 2]], [[3, 4], [5, 6]])
matrix_mul([[1, 2], [9, 9]], [[3, 4]])

#print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
#print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))






