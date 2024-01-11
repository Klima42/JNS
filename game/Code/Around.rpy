label around:
    scene Bot
    K "You start looking around, you appear to be in some sort of lab, the white tiles are reflecting the huge portal in front of you."
    K "You don't have any feeling of touch on your body, but you're able to move, your limbs are robotic."
    K "As you try to inhale, you realize you don't even need to breath, it appears your whole body is mechanic."
    K "*steps approaching*"
    show ys at anim2
    G "Welcome back agent, this sure was eventful wasn't it ?"
    K "*You try to speak, but you're no able to emit any sound*"
    G "Whoops ! My bad !"
    K "*she plugs your arm to the screen on your left*"
    M "Here, do you remember how to use this ? just think a sentence and it'll appear on the screen okay ?"
    menu:
        "I 'm an agent ?":
            jump agent
        "Who are you ?":
            jump areYou
        "I think I remember you":
            jump you

    