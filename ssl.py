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

#일본어통번역학과 201700801 김우영
#(head)를 1번 노드에 출력시키기에는 실패했으나, 이외에는 정상작동함
	def traverse_all(self):
		current_node = self.head.next
		while current_node is not None:
			print(f"({current_node.data}) -> ", end="")
			current_node = current_node.next
		print("null")



#일본어통번역학과 201700801 김우영
#정상작동
	def insert_at(self, position, new_data):
		if position <= 0:
			print("Error: position이 0보다 커야합니다.")
			return

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

#일본어통번역학과 201700801 김우영
#정상작동

	def remove(self, key):
			# 데이터가 없는 경우 삭제할 노드도 없기 때문에 None 리턴
			if self.num_of_data == 0:
				print(f"* 해당하는 원소가 없습니다.")
				return None

			# 노드의 위치 번호를 저장할 변수 position 초기화
			position = 1

			# 현재 위치를 head로 설정
			current_node = self.head

			# 삭제할 노드가 맨 앞의 노드인 경우
			if current_node.data == key:
				self.head = current_node.next
				self.num_of_data -= 1
				print(f"* {position}번째 원소({key})를 삭제합니다.")
				return

			# 맨 앞이 아닌 경우 노드를 하나씩 순회하며 삭제할 노드를 찾음
			while current_node.next is not None:
				# 현재 노드의 다음 노드가 삭제할 노드인 경우
				if current_node.next.data == key:
					# 삭제할 노드가 tail인 경우
					if current_node.next is self.tail:
						self.tail = current_node

					# 삭제할 노드가 중간에 있는 경우
					current_node.next = current_node.next.next
					self.num_of_data -= 1
					print(f"* {position}번째 원소({key})를 삭제합니다.")
					return
				else:
					position += 1
					current_node = current_node.next

			# 삭제할 노드가 없는 경우
			print(f"* 해당하는 원소가 없습니다.")

		
linked_list = LinkedList()
linked_list.append(100)
linked_list.append(72)
linked_list.append(325)

linked_list.traverse_all()

linked_list.insert_at(2, 150)
linked_list.traverse_all()

linked_list.insert_at(5, 1000)
linked_list.traverse_all()

linked_list.insert_at(0, 0)
linked_list.traverse_all()

linked_list.remove(100)
linked_list.traverse_all() 

linked_list.remove(800) # 해당하는 원소가 없습니다.
linked_list.traverse_all()
