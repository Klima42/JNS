label Nina:
    scene train_2 
    K "I have to tell her !"
    K "There's no time to lose !"
    scene train_4
    scene train_3
    K "..."
    K "Nina, listen to me !"
    S "You arrived yet ?"
    K "I told you to listen !"
    S "Wow, rude but okay"
    K "I'm being serious alright."
    S "Alright alright, I'm listening."
    K "I don't want to, freak you out, but Alice your friend, is in danger, she is gonna die if we don't do something."
    pause 0.5
    S "... is that it ?"
    K "what-"
    S "I mean, it's kind of ... surprising that you found out but like, I know that, that's kinda the whole point."
    K "Nina, I'm NOT joking !!"
    S "yeah yeah I know, you'll get used to it, trust me.
                We'll meet on lane 12 alright ?"
    K "..."
    K "This is weird, this dosn't feel real."
    pause 1.0
    S "Haha yeah I guess, finally a different run right ?"
    K "A different ... What ?"
    S "You'll see, I'm soo glad that you're back by the way, see you there"
    K "Huh"
    pause 1.0
    scene quai with fade
    K "~A few moments later~"
    S "Hey !"
    show Nsp
    S "You remember everything, right ?"
    K "Yeah ... But you  too ?"
    scene gare
    show NN
    S "Hmph, of course I always do."
    K "So, I feel like you actually understand what's going on, right ?"
    S "Well... We're, ...stuck, time loop."
    K "~you feel sizzy, this isn't right"
    R "Y̷o̵u̵'̶r̸e̶ ̵s̵o̸ ̶f̴u̶c̵k̴i̴n̶g̴ ̷s̴l̵o̶w̶"
    R "L̴e̶a̸v̴e̶ ̵m̴y̷ ̷b̷o̸d̷y̴,̷ ̸y̸o̷u̵ ̴w̵a̵s̸t̵e̵ ̵o̶f̸ ̷a̸i̴r̷,̵ ̵j̶u̴s̴t̸ ̵d̸i̷e̵ ̷a̵l̶r̴e̴a̸d̷y̷.̴"
    pause 0.5
    S "Hey, you're alright ?"
    K "Yeah yeah, this is just... A lot to take at once, the voice, the 'time loop', what I saw earlier."
    S "I know, sorry it's just, the firt time ever someone remembers anything so, I don't even know where to start !"
    hide NN 
    show  NS
    S "I'll tell you more once we're home okay ?"
    K "I still have a question though."
    S "Hm ?"
    menu:
        "What's a 'run' ?":
            jump rune
        "Can we save Alice ?":
            jump saveA
        "Why are we stuck ?":
            jump stuck

    return
        