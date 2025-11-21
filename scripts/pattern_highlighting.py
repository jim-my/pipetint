from pipetint import colored

text = "The quick brown fox jumps over the lazy dog"
highlighted = colored(text).highlight(r"(quick)|(fox)|(lazy)", ["red", "blue", "green"])
print(highlighted)
