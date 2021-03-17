import re
text = "Ex_ample-1@ex.com, example@mail.ru, example_11@mail.ru, @mail.ru, Hello@gmail.ru"

def check(email_adr):
	if re.findall(r"[A-Za-z\d]+@[A-Za-z\d]+\.[A-Za-z\d]+" , email_adr):
		return True
	else:
		return False

finish = check("Example1@ex.com, exa1mple@gg.com")
print(finish)