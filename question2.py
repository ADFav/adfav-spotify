def decodeString(s):
    
    # Datastructure to process all different phrases in the string
    class bracketStack:
        def __init__(self):
            self.strings = [""]
            self.reps = []
        
        # Concatenates phrases together    
        def appendPhrase(self,phrase):
            self.strings[-1] += phrase
        
        # Moves counters and phrases down the line, so it can work on the new phrase
        def newPhrase(self,num):
            self.reps.append(num)
            self.strings.append("")
        
        # Repeats a phrase a given number of times, and concatenates it to the latest phrase
        def decodeLatestPhrase(self):
            phrase = self.strings.pop(-1)
            reps = self.reps.pop(-1)
            for _ in range(reps):
                self.strings[-1] += phrase
            
    bs = bracketStack()
    i = 0
    num = ""
    phrase = ""
    result = ""
    while i < len(s):
        while s[i] in "0123456789":
            num += s[i]
            i += 1
        if s[i] == "[":
            bs.newPhrase(int(num))
            phrase = ""
            num = ""
        elif s[i] == "]":
            if len(bs.strings) == 1:
                raise Exception("ImproperlyPlacedRightBracket")
            bs.decodeLatestPhrase()
        else:
            bs.appendPhrase(num + s[i])
            num = ""
        i += 1
    if len(bs.strings) != 1:
        raise Exception("UnbalancedNumberOfBrackets")
    return bs.strings[0]
    
# print "4[ab] ==> abababab"
# print decodeString("4[ab]") == "abababab"
# print "****"
# print "2[b3[a]] ==> baaabaaa"
# print decodeString("2[b3[a]]") == "baaabaaa"
