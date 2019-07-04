json = {
	"one": 1,
	"two": [1,2],
	"three": [1,2,3],
	"four": [{"five": 5, "six": 6, "seven": 7}]
}

print(json['one'])
print(json['two'])
print(json['three'])
print(json['two'][0])
print(json['two'][1])
print(json['three'][0])
print(json['three'][1])
print(json['three'][2])

print(json['four'][0]['seven'])