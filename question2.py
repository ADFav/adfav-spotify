def decodeString(s):
    class bracketStack:
        def __init__(self):
            self.strings = [""]
            self.reps = []
            
        def appendPhrase(self,phrase):
            self.strings[-1] += phrase
        
        def newPhrase(self,num):
            self.reps.append(num)
            self.strings.append("")
        
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
            bs.decodeLatestPhrase()
        else:
            bs.appendPhrase(num + s[i])
            num = ""
        i += 1
    return bs.strings[-1]
    
# print "4[ab] ==> abababab"
# print decodeString("4[ab]") == "abababab"
# print "****"
# print "2[b3[a]] ==> baaabaaa"
# print decodeString("2[b3[a]]") == "baaabaaa"
