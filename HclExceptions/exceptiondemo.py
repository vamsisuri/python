class Hcl_list-exceptions(exception):
    def __init__(self,mes):
        self.message=mes
        super().__init__(self.message)

