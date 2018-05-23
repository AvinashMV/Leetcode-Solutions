class ReverseSentence:

    def Rev(self,str):
        strlist= str.split(" ")
        strlist_rev=strlist[::-1]  # to reverse a list.
        strlist_rev_rev=[i[::-1] for i in strlist_rev] # to reverse each word in the list.
        str_rev=" ".join(strlist_rev_rev)
        print(str_rev)

if __name__=="__main__":
    obj=ReverseSentence()
    str="This life sucks"
    obj.Rev(str)