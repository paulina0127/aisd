from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


class LinkedList:
    head: Node

    def __init__(self) -> None:
        self.head = None

    def push(self, value: Any) -> None:
        new = Node(value)

        if self.head == None:     # lista jest pusta
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def append(self, value: Any) -> None:
        new = Node(value)

        if self.head == None:     # lista jest pusta
            self.head = new
        else:
            last = self.head
            while (last.next != None):
                last = last.next
            last.next = new

    def node(self, at: int) -> Node:
        current = self.head
        cnt = 0

        if at == 0:
            return current
        else:
            while (cnt != at):
                if current == None:     # węzeł nie istnieje
                    return None
                current = current.next
                cnt += 1
            return current

    def insert(self, value: Any, after: Node) -> None:
        if after == None and len(list_) == 0:     # lista jest pusta
            self.head = Node(value)
        elif after == None:     # węzeł nie istnieje, ale lista nie jest pusta
            self.append(value)
        else:
            old = after.next
            new = Node(value)
            after.next = new
            new.next = old

    def pop(self) -> Any:
        if self.head == None:     # lista jest pusta
            return None
        else:
            first = self.head.value
            self.head = self.head.next
            return first

    def remove_last(self) -> Any:
        nd_last = self.head

        if self.head == None:     # lista jest pusta
            return None
        elif nd_last.next == None:     # tylko jeden węzeł
            last = nd_last.value
            nd_last.value = None
            return last
        elif nd_last.next.next == None:     # tylko dwa węzły
            last = nd_last.next.value
            nd_last.next = None
            return last
        else:
            while nd_last.next.next != None:
                nd_last = nd_last.next
            last = nd_last.next.value
            nd_last.next = None
            return last

    def remove(self, after: Node) -> Any:
        if after == None or after.next == None:     # węzeł nie istnieje / jest ostatni
            return
        else:
            after.next = after.next.next
            return

    def __str__(self) -> str:
        lista = str(self.head.value)
        check = self.head.next
        while check != None:
            lista += " -> "
            lista += str(check.value)
            check = check.next
        return lista

    def __len__(self) -> int:
        cnt = 0
        check = self.head
        while check != None:
            cnt += 1
            check = check.next
        return cnt


class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        return self._storage.remove_last()

    def __str__(self) -> str:
        lista = ""
        temp = []
        cnt = len(self._storage)

        while cnt != 0:
            element = self._storage.pop()
            temp.append(element)
            cnt -= 1

        temp.reverse()
        for i in temp:
            self._storage.push(i)
            lista += str(i)
            lista += "\n"

        return lista

    def __len__(self) -> int:
        cnt = 0
        check = self._storage.head
        while check != None:
            cnt += 1
            check = check.next
        return cnt


class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __str__(self) -> str:
        lista = str(self._storage.head.value)
        check = self._storage.head.next
        while check != None:
            lista += ", "
            lista += str(check.value)
            check = check.next
        return lista

    def __len__(self) -> int:
        cnt = 0
        check = self._storage.head
        while check != None:
            cnt += 1
            check = check.next
        return cnt


## LISTA ##
list_ = LinkedList()
assert list_.head == None

# dodanie nowego węzła na początku listy
list_.push(1)
list_.push(0)

# testowanie print i len
print("Lista:", list_)
print("Długość listy:", len(list_))
assert str(list_) == '0 -> 1'

# dodanie nowego węzła na końcu listy
list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'

# zwrócenie węzła na określonej pozycji
print("Węzeł na 2 pozycji:", list_.node(at=1).value)

# dodanie nowego wezła za danym węzłem
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

# usunięcie pierwszego węzła
first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element

# usunięcie ostatniego węzła
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

# usunięcie węzła za danym węzłem
second_node = list_.node(at=1)
list_.remove(second_node)
assert str(list_) == '1 -> 5'

## STOS ##
stack = Stack()
assert len(stack) == 0

# dodanie nowego elementu na szczycie stosu
stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3

# testowanie print
print("Stos:")
print(stack)

# usunięcie elementu ze szczytu stosu
top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2

## KOLEJKA ##
queue = Queue()
assert len(queue) == 0

# dodanie nowego elementu na końcu kolejki
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

# testowanie print
print("Kolejka:", queue)
assert str(queue) == 'klient1, klient2, klient3'

# usunięcie pierwszego elementu w kolejce
client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2