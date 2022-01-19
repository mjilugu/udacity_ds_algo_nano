# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        # curr = self.root

        # curr.handler = handler
        self.root.insert(path, handler)

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr = self.root

        for segment in path:
            if segment not in curr.children:
                return None 
            curr = curr.children[segment]

        return curr.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, handler = None):
        # Insert the node as before
        if len(path) == 0:
            return
        if len(path) == 1:
            self.children[path[0]] = RouteTrieNode(handler)
            return
            
        self.children[path[0]] = RouteTrieNode()
        self.children[path[0]].insert(path[1:], handler)


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_handler = root_handler 
        self.not_found_handler = not_found_handler
        self.routes = RouteTrie(root_handler)

    def add_handler(self, path_str, handler):
        # Add a handler for a path
        # You will need to split the path and pass the path parts
        # as a list to the RouteTrie
        path = self.split_path(path_str)
        self.routes.insert(path, handler)

    def lookup(self, path_str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = self.split_path(path_str)
        handler = self.routes.find(path)

        return handler if handler else self.not_found_handler


    def split_path(self, path_str):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path = path_str.split('/')

        path = [ item for item in path if len(item) ]

        return path


## Main

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/super/long/path/that/keeps/going/and/going","long path handler") # add another route

# some lookups with the expected output
print(f'\nTest1: router.lookup("/")')
#'root handler'
print(router.lookup("/")) # should print 'root handler'

print(f'\nTest2: router.lookup("/home")')
#'not found handler'
print(router.lookup("/home")) # should print 'not found handler'

print(f'\nTest3: router.lookup("/home/about")')
#'about handler'
print(router.lookup("/home/about")) # should print 'about handler'

print(f'\nTest4: router.lookup("/home/about/")')
#'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'

print(f'\nTest5: router.lookup("/home/about/me")')
#'not found handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'

print(f'\nTest6: router.lookup("/home/about/me/")')
#'not found handler'
print(router.lookup("/home/about/me/")) # should print 'not found handler'

print(f'\nTest7: router.lookup("")')  # Empty string path
#'root handler'
print(router.lookup("")) # should print 'root handler'

print(f'\nTest8: router.lookup("/super/long/path/that/keeps/going/and/going")')  # Long path
#'long path handler'
print(router.lookup("/super/long/path/that/keeps/going/and/going")) # should print 'long path handler'

