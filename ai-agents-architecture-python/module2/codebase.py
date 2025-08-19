class ReverseAction:
    def __init__(self, execute_func, reverse_func):
        self.execution_record = None
        self.execute = execute_func
        self.reverse = reverse_func
        
        # In python, we use *to unpack list and ** to unpack a dict
    def run(self, **args):
        result = self.execute(**args)
        self.execution_record = {
            "args": args,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }

    def undo(self):
        if not self.execution_record:
            # A ValueError is a built-in Python exception that occurs when a function receives an argument of the correct type but an inappropriate value.
            raise ValueError('No action to reverse')
        else:
            self.reverse(self.execution_record)
            
