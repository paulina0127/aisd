from typing import Any, Callable, List

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self) -> bool:
        if self.left_child == None and self.right_child == None:
            return True
        return False

    def add_left_child(self, value: Any) -> None:
        if value == None:
            return
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        if value == None:
            return
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)

        visit(self, end=" ")

        if self.right_child != None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)

        if self.right_child != None:
            self.right_child.traverse_post_order(visit)

        visit(self, end=" ")

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self, end=" ")

        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)

        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)

    def show(self, poz: int = 0) -> None:
        if self.left_child != None:
            self.left_child.show(poz + 1)

        print(" " * 5 * poz + "->", self.value)

        if self.right_child != None:
            self.right_child.show(poz + 1)

    def __str__(self):
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value: Any) -> None:
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.root.left_child != None:
            self.root.left_child.traverse_in_order(visit)

        visit(self.root, end=" ")

        if self.root.right_child != None:
            self.root.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.root.left_child != None:
            self.root.left_child.traverse_post_order(visit)

        if self.root.right_child != None:
            self.root.right_child.traverse_post_order(visit)

        visit(self.root, end=" ")

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self.root, end=" ")

        if self.root.left_child != None:
            self.root.left_child.traverse_pre_order(visit)

        if self.root.right_child != None:
            self.root.right_child.traverse_pre_order(visit)

    def show(self) -> None:
        self.root.show()

    def right_line(self) -> List[BinaryNode]:
        right_line = []
        if self.root == None:
            return right_line

        list = []
        list.append(self.root)

        while len(list):
            n = len(list)
            for i in range(1, n + 1):
                temp = list[0]
                list.pop(0)

                if i == n:
                    right_line.append(temp)

                if temp.left_child != None:
                    list.append(temp.left_child)

                if temp.right_child != None:
                    list.append(temp.right_child)

        return right_line


## DRZEWO BINARNE ##
tree = BinaryTree(10)  # korze??
assert tree.root.value == 10

# dodanie w??z????w
tree.root.add_left_child(9)  # pierwszy poziom
tree.root.add_right_child(2)

tree.root.left_child.add_left_child(1)  # drugi poziom
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)

tree.root.left_child.right_child.add_right_child(5)  # trzeci poziom
tree.root.left_child.right_child.add_left_child(4)

# przej??cie poprzeczne od korzenia
#tree.traverse_in_order(print)
#print()

# przej??cie wsteczne od korzenia
#tree.traverse_post_order(print)
#print()

# przej??cie wzd??u??ne od korzenia
#tree.traverse_pre_order(print)
#print()

# wy??wietlenie drzewa
#tree.show()

# prawy widok drzewa
#for i in tree.right_line():
#    print(i.value, end=" ")

## W??ZE?? DRZEWA BINARNEGO ##
# sprawdzenie czy w??ze?? jest li??ciem
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False

assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

# przej??cie poprzeczne
#tree.root.left_child.traverse_in_order(print)
#print()

# przej??cie wsteczne
#tree.root.left_child.traverse_post_order(print)
#print()

# przej??cie wzd??u??ne
#tree.root.left_child.traverse_pre_order(print)
#print()