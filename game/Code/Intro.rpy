label intro:
    scene black
    G "Initiate quamtum field temporisation."
    Q "All variables are stable."
    Q "Launch the walking sequence of the subject."
    scene Q2
    Q "Viable. All vitals are in check."
    G "Good. Inject the adreno solution and keep checking the vitals."
    Q "..."
    Q "The subject is responsive ma'am."
    G "Excellent, I'll take it from there."
    scene Q3
    pause 0.5
    G "Salutation subject."
    G "I'm aware you will not remember this conversation, at least not in a way that matters."
    G "But I think you deserve encouragement. So I will be brief."
    G "Good luck. Be brave, be loyal, and be unforgiving."
    G "All glory to QMES."
    E "*in unison* ALL GLORY TO QMES"
    scene Q4

    menu:
        "Enter JNS":
            jump JNS


    label JNS:
        scene black
        K "*You feel like your bond with this world is unbreakable*"
        K "*Memories of your previous life wither away.*"
        K "*Memories of a new life flow through your mind*"
        pause 1.0
        jump train_1

    