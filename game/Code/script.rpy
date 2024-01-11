
default CA = 0

label start:
    jump intro
    jump train_1
    label first:
         menu:
            "I should rest":
                jump rest
            #"I should call her":
            #    jump callHer
    scene train_1 
    pause 4.0

   


        