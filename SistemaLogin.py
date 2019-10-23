# Dicionario para UserId e Passwords
pwds = {"admin":"admin", "rambo":"rambo", "root":"root"}
maxlogin = 3 #maximo de tentativas
cont = 0

while cont < maxlogin:
	cont = cont + 1
	userid = input("UserID: ")
	password = input("Password: ")

	if userid in pwds:
		if password == pwds[userid]:
			print('Login feito com Sucesso!')
			break
		else:
			print('Errou a senha meu amigo!')
	else:
		print('Esse UserId não existe!')