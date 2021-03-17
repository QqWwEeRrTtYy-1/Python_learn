import re
file_content = open("text.txt", "r")
text = file_content.read()
file_content.close()

new_file = open("new_text.txt", "w")
ready_text = ' '.join(re.findall(r"\w+", text)).lower()
new_file.write(ready_text)
