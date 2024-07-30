# 1472. Design Browser History

# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

# Example:

# Input:
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

# Output:
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

# Explanation:
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage] # list to store the history of urls (homepage being the default)
        self.current_index = 0 # pointer to current position indicating homepage is current page
        self.length = 1 # length of current history as there is only one page: homepage
        

    def visit(self, url: str) -> None:
        # when we visit the new URL truncate the forward history
        # A -> B -> C -> D and suppose we go back to B and then we go to a new page E and then back to B 
        # so the current index would be set to B and then we would directly go to E truncating C and D
        self.history = self.history[:self.current_index + 1] # this ensures that the new path is taken from the current index
        # add new url to the end of the history
        self.history.append(url)
        # move the current index to new url
        self.current_index += 1
        # update the length 
        self.length = len(self.history)
        

    def back(self, steps: int) -> str:
        # move back in the history but obviously not beyond the start
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]
        

    def forward(self, steps: int) -> str:
        # move forward but not beyond the most recent url
        self.current_index = min(self.length - 1, self.current_index + steps)
        return self.history[self.current_index]
