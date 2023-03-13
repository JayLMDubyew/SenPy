import random
import time


# some ideas taken from https://github.com/Schotsl/Uwuifier/blob/main/index.ts
def uwuIt(text_str) -> str:
    woo = "w"
    text_str = text_str.lower()
    uwud = text_str.replace('r', woo)
    uwud = uwud.replace('l', woo)
    uwud = uwud.replace('ove', "uv")
    uwud = uwud.replace('you', "yew")
    uwud = uwud.replace('ou', "ow")
    uwud = uwud.replace('u', "uw")
    uwud = uwud.replace('a', "aw")
    uwud = uwud.replace('oo', "ew")

    do_action = random.randint(0, 3)
    actions = ["*sweats*", "*screams*","*is kawaii desu*", "*squees*", "*cuddles*", "*boops ur snoot*", "*eats pocky*",
               "*nibbles konpeito*"]
    suffix = ["(´,,•ω•,,)♡", "( ๑>ᴗ<๑ )", "ʕっ• ᴥ • ʔっ", "( ◠‿◠✿)", "(˃ᆺ˂✿)", "(′ꈍωꈍ‵)", "♥(ˆωˆ`๑)", "(´∩｡• ᵕ •｡∩`) ♡",
              "(✿◠‿◠)", "(•̀ω•́ )", "(◕‿-)", "｡ ◕‿◕ ｡", "(ꈍᴗꈍ)", "uwu", "...s-senpai", "(´･ω･`)", "tee hee", "🥺👉👈"]
    if not do_action:
        uwud = f"{random.choice(actions)} " + uwud
    else:
        uwud = uwud + f" {random.choice(suffix)}"
    return (pinky(uwud))


def pinky(normal_string) -> str:
    return ("\033[95m {}\033[00m".format(normal_string))


def hewwo() -> None:
    head = """
██╗   ██╗███████╗██╗    ██╗    ███╗   ██╗ ██████╗ ████████╗██╗ ██████╗███████╗██████╗     ███████╗███████╗███╗   ██╗██████╗ ██╗   ██╗      ██████╗██╗  ██╗ █████╗ ███╗   ██╗██╗██╗    
╚██╗ ██╔╝██╔════╝██║    ██║    ████╗  ██║██╔═══██╗╚══██╔══╝██║██╔════╝██╔════╝██╔══██╗    ██╔════╝██╔════╝████╗  ██║██╔══██╗╚██╗ ██╔╝     ██╔════╝██║  ██║██╔══██╗████╗  ██║██║██║    
 ╚████╔╝ █████╗  ██║ █╗ ██║    ██╔██╗ ██║██║   ██║   ██║   ██║██║     █████╗  ██║  ██║    ███████╗█████╗  ██╔██╗ ██║██████╔╝ ╚████╔╝█████╗██║     ███████║███████║██╔██╗ ██║██║██║    
  ╚██╔╝  ██╔══╝  ██║███╗██║    ██║╚██╗██║██║   ██║   ██║   ██║██║     ██╔══╝  ██║  ██║    ╚════██║██╔══╝  ██║╚██╗██║██╔═══╝   ╚██╔╝ ╚════╝██║     ██╔══██║██╔══██║██║╚██╗██║╚═╝╚═╝    
   ██║   ███████╗╚███╔███╔╝    ██║ ╚████║╚██████╔╝   ██║   ██║╚██████╗███████╗██████╔╝    ███████║███████╗██║ ╚████║██║        ██║        ╚██████╗██║  ██║██║  ██║██║ ╚████║██╗██╗    
   ╚═╝   ╚══════╝ ╚══╝╚══╝     ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝╚══════╝╚═════╝     ╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝        ╚═╝         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝    
                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                     
  ___    _ .--.      .--.  ___    _  
.'   |  | ||  |_     |  |.'   |  | | 
|   .'  | || _( )_   |  ||   .'  | | 
.'  '_  | ||(_ o _)  |  |.'  '_  | | 
'   ( \.-.|| (_,_) \ |  |'   ( \.-.| 
' (`. _` /||  |/    \|  |' (`. _` /| 
| (_ (_) _)|  '  /\  `  || (_ (_) _) 
 \ /  . \ /|    /  \    | \ /  . \ / 
  ``-'`-'' `---'    `---`  ``-'`-''   mode \n\n"""

    print(pinky(head))

    time.sleep(.05)
    print(uwuIt("hello it's senpy"))
    time.sleep(.5)
    print(uwuIt("...did you miss me?"))
