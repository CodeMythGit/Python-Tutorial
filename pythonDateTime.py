import datetime

ct = datetime.datetime.now()
print(ct)

#datetime constructor YYYY,MM,DD
x = datetime.datetime(1947,8,15)
print(x)

#strftime - 
#%a - Sun %A - Sunday
#%b - Aug %B - August
print(x.strftime("%a"))
print(x.strftime("%A"))

print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%Y"))



