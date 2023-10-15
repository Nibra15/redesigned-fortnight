example = ")()())))))))))))"
index_open =example.rfind("(")
index_close = example.rfind(")")
print(index_close-index_open)