def del_sp_ap(txt):
	"""
	parameteres : txt of type string;
	returns     : another string with any " " or "'" removed;
	"""
	if not txt:
		return ''
	if txt[0] == ' ' or txt[0] =="'":
		return del_sp_ap(txt[1:])
	else:
		return txt[0] + str(del_sp_ap(txt[1:]))

print(del_sp_ap("T' u' sk"));