import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(len(['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']))
print(keyword.iskeyword('None'))
print(keyword.iskeyword('True'))
print(keyword.iskeyword('pass'))
print(keyword.iskeyword('return'))
print(keyword.iskeyword('assert'))
print(keyword.iskeyword('print'))
print(keyword.iskeyword('try'))


""" We cannot use keyword as variable or identifiers """
# None = 6
# True =4
# while = 5