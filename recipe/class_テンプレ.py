class SimpleClass:
    id = ""
    name = ""
    file = ""

    def __init__(self):
        self.id = "id"
        self.name = "name"
        self.file = "test.txt"

    def open_text(self):
        lines = []
        try:
            with open(self.file, mode="r") as f:
                tmp_lines = f.read().splitlines()
                lines = list(tmp_lines)
            
        except Exception as e:
            exc_type, _, exc_tb = sys.exc_info()
            print("(E open_text error) %s %s: %s" % (exc_tb.tb_lineno, exc_type, e))

        return lines
