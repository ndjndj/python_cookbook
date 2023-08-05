import sys

def open_text(file_name):
    lines = []
    try:
        with open(file_name, mode="r") as f:
            tmp_lines = f.readlines()
            lines = list(tmp_lines)
        
    except Exception as e:
        exc_type, _, exc_tb = sys.exc_info()
        print("(E open_text error) %s %s: %s" % (exc_tb.tb_lineno, exc_type, e))

    return lines

if __name__ == "__main__":
    open_text("test.text")
