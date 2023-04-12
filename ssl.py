# Node 클래스 정의
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


# LinkedList 클래스 정의
class LinkedList:

	# 초기화 메소드
	def __init__(self):
		dummy = Node("dummy")
		self.head = dummy
		self.tail = dummy

		self.current = None
		self.before = None

		self.num_of_data = 0

	# append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
	def append(self, data):
		new_node = Node(data)
		self.tail.next = new_node
		self.tail = new_node

		self.num_of_data += 1

	# delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
	def delete(self):
		pop_data = self.current.data

		if self.current is self.tail:
			self.tail = self.before

			# 중요 : current가 next가 아닌 before로 변경된다.
			self.before.next = self.current.next
			self.current = self.before 

			self.num_of_data -= 1

			return pop_data

	# first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
	def first(self):
		# 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
		if self.num_of_data == 0: 
			return None

		self.before = self.head
		self.current = self.head.next

		return self.current.data

	# next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
	def next(self):
		if self.current.next == None:
			return None

		self.before = self.current
		self.current = self.current.next

		return self.current.data

	# size 메소드
	def size(self):
		return self.num_of_data 

    # traverse_all 메소드 (head부터 tail까지 각 노드의 data 출력)
	def traverse_all(self):
		current_node = self.head.next
		while current_node is not None:
			print(f"({current_node.data}) -> ", end="")
			current_node = current_node.next
		print("null")


    # insert_at 메소드 (position 위치에 new_data 노드 삽입)
	def insert_at(self, position, new_data):
        # position이 0 이하이면 error 문 출력 후 종료
		if position <= 0:
			print("Error: position이 0보다 커야합니다.")
			return

        # position이 리스트의 크기(원소 갯수)보다 크면 맨 마지막에 삽입
		if position > self.num_of_data:
			self.append(new_data)
			return

		new_node = Node(new_data)
		current_node = self.head.next
		before_node = self.head
		current_position = 1

		while current_position != position:
			before_node = current_node
			current_node = current_node.next
			current_position += 1

		new_node.next = current_node
		before_node.next = new_node

		self.num_of_data += 1

# remove 메소드 (delete - 주어진 key 값을 갖는 노드 삭제, 데이터 개수 변경)
	def remove(self, key):
        # 데이터가 없는 경우 삭제할 노드도 없기 때문에 None 리턴
		if self.num_of_data == 0:
			print("해당하는 원소가 없습니다.")
			return None

        # key 값과 일치하는 노드를 찾기 위해 first 메소드 호출
		self.first()

        # 삭제할 노드가 맨 앞의 노드인 경우 (before와 head 변경)
		if self.current.data == key:
			self.head = self.head.next
			self.current = self.head
			self.before = self.head
			self.num_of_data -= 1

		else:
			while self.current.next:
                # 삭제할 노드 발견
				if self.current.next.data == key:
                    # 삭제할 노드가 tail인 경우 (tail과 before 변경)
					if self.current.next is self.tail:
						self.tail = self.current

					self.current.next = self.current.next.next
					self.num_of_data -= 1

				else:
					self.current = self.current.next
					continue
		
		print(f"* {key}번째 원소(key)를 삭제합니다.")