import sys

#読み込んだファイルを一行ずつのリストに変換
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

#改行コードを削除する
def open_text_split_lines(file_name):
    lines = []
    try:
        with open(file_name, mode="r") as f:
            tmp_lines = f.read().splitlines()
            lines = list(tmp_lines)
        
    except Exception as e:
        exc_type, _, exc_tb = sys.exc_info()
        print("(E open_text error) %s %s: %s" % (exc_tb.tb_lineno, exc_type, e))

    return lines


if __name__ == "__main__":
    open_text("test.text")
    open_text_split_lines(file_name)
