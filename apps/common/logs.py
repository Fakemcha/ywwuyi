def write_test_log(content, filedir=r"/home/mqmmw/mqmmw/logs/", filename=r"test.log"):
    filepath = filedir + filename
    try:
        with open(filepath, "a+") as f:
            f.write(str(content) + "\n")
    except Exception as e:
        print(str(e))
        with open(filepath, "a+") as f:
            f.write(str(e))
            f.write("\n")