# partage.py
def partager_montant(montant, n):
	portion, reste = montant // n, montant % n
	portions = []
	for i in range(n):
		portions.append(portion)
		if reste > 0:
			portions[-1] += 1
			reste -= 1
	return portions


