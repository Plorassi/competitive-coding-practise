class Logger:

    def __init__(self):
        self.map = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.map:
            if self.map[message] + 10 <= timestamp:
                self.map[message] = timestamp
                return True
            else:
                return False
        else:
            self.map[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
