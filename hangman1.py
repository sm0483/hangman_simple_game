import random
#opening file
file=open("/home/user/Desktop/simple_hangman/data_han.text","r")
ls=[]
for word in file:
    if "-" in word.strip():
        continue
    else:
        ls.append(word.lower().strip())
#hungman procedure

system_guess=random.choice(ls)
print(system_guess)
#print(system_guess)
def hungman():
    count=0
    y_set=set()
    out=None
    while count!=len(system_guess)+1 and system_guess!=out:
        count+=1
        y_guess=input(f"enter your first letter{count}/{len(system_guess)+1}: ")
        y_set.add(y_guess)
        if y_guess in system_guess:
            print("yep")
        else:
            print("no")    
        inter_ls=[letter if letter in y_set else "-" for letter in system_guess]
        out="".join(inter_ls)
        global ls1
        ls1=[letter for letter in out if letter!="-"]
        print(out)
        #print(inter_ls)
    #print(ls1)
 
hungman()

#result procedure
def score(inp):
    print(f"{inp*10}/{len(system_guess)*10}")

    if inp==len(system_guess):
        return("you win")
        return (f"{inp*10}/{len(system_guess)*10}")
    else:
        return (f"your score is {inp*10}")
        return (f"{inp*10}/{len(system_guess)*10}")


final_result=score(len(ls1))
print(final_result)   