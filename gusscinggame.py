sc_word="anik"
g_c=0;
g_l=3;
out_of_g =False
g_w= ""

while g_w != sc_word and not(out_of_g):
    if g_c < g_l :
        g_w=input("Enter Word:")
        g_c+=1
    else:
        out_of_g = True

if out_of_g:
    print("Out of Guesses, You Lose!")
else:
    print("You Win")