# {
# Driver Code Starts
# Initial Template for Python 3

class Node:
    data = 0
    left = None
    right = None


def createNewNode(value):
    temp = Node()
    temp.data = value
    temp.left = None
    temp.right = None
    return temp


def newNode(root, data):
    if (root is None):
        root = createNewNode(data)
    elif (data < root.data):
        root.left = newNode(root.left, data);
    else:
        root.right = newNode(root.right, data)

    return root


# } Driver Code Ends

# User function Template for python3

##Complete this function
def inOrder(root):
    if root is None:
        return
    ##Your code here
    ##Inorder traversal is Left, node, right


# {
# Driver Code Starts.


def main():
    testcases = int(input())
    while (testcases > 0):
        root = None
        sizeOfArray = int(input())
        arr = [int(x) for x in input().strip().split()]
        for i in arr:
            root = newNode(root, i)

        inOrder(root)
        print()

        testcases -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends