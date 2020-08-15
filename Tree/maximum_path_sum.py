def findMaxUtil(root):
    # Base Case
    if root is None:
        return 0

        # l and r store maximum path sum going through left
    # and right child of root respetively
    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)

    # Max path for parent call of root. This path
    # must include at most one child of root
    max_single = max(max(l, r) + root.data, root.data)

    # Max top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
    max_top = max(max_single, l + r + root.data)

    # Static variable to store the changes
    # Store the maximum result
    findMaxUtil.res = max(findMaxUtil.res, max_top)

    return max_single


# Return maximum path sum in tree with given root
def findMaxSum(root):
    # Initialize result
    findMaxUtil.res = float("-inf")

    # Compute and return result
    findMaxUtil(root)
    return findMaxUtil.res


# User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''




# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by Suman Rana
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        root = buildTree(input())
        print(findMaxSum(root))

# } Driver Code Ends