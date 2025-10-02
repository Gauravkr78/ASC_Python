from pyexpat import features

band={
    "vocal":"Plant",
    "guitar":"Page"
}
band2=dict(vocal="Plant",guitar="Page")
print(band)
print(band2)

print(type(band))
print(type(band2))


print(band["vocal"])
print(band.keys())
print(band.values())
print(band.items())


print("verify")
print("vocal" in band)

band["vocal"]="Coverdale"
print(band)


print("Remove")
print(band.pop("guitar"))
print(band)


orig={'a':1,'b':2}
ref=orig.copy()
print(orig)
print(ref)
ref['c']=3
print(ref)
print(orig)