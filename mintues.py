seconds = int(raw_input("Provide seconds and will convert in Hours, Mintues and Seconds:"))
mint_h=seconds/3600
if mint_h > 0 :
		seconds = seconds - mint_h * 3600
mint_m=seconds/60
mint_s=seconds%60
print
print str(mint_h) + " Hour " + str(mint_m) + " Mintue " + str(mint_s) + " Seconds "
