def sortByStrings(s,t):
    # First, count how many times each letter occurs in s
    s_counts = {}
    for char in s:
        if char not in s_counts:
            s_counts[char] = 0
        s_counts[char] += 1
    
    #Iterate over letters in t, append letters in s to result
    result = ""
    for char in t:
        if char in s_counts:
            for _ in range(s_counts[char]):
                result += char
    return result

# print("weather, therapyw ==> theeraw")
# print sortByStrings("weather","therapyw") == "theeraw"
# print("****")
# print("good, odg ==> oodg")
# print sortByStrings("good","odg") == "oodg"