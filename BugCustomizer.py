bugs = ['beetle.png', 'cricket.png', 'ladybug.png', 'grasshopper.png']

tints = ['#FFFFFF', #white/default tint
         '#FF9595', #red
         '#ACFFB1', #green
         '#7BA7FF', #blue
         '#FF85EA'] #purple

patterns = ['#FFFFFF', #white/default tint
         '#763232', #red
         '#2C551D', #green
         '#346588', #blue
         '#763883'] #purple

accesscol = ['#FFFFFF', #white/default tint
         '#EE6C6C', #red
         '#96FE47', #green
         '#61ABFF', #blue
         '#FF52FC'] #purple

misccol = ['#FFFFFF', #white/default tint
         '#EE6C6C', #red
         '#96FE47', #green
         '#61ABFF', #blue
         '#FF52FC'] #purple

mode = 'bugchoose'

perk = 'none'


tintcolor = patterns[0]

accesscolor = accesscol[0]

misccolor = misccol[0]

#stats
stats = ['bstats.png', 'cstats.png', 'lbstats.png', 'ghstats.png']


#basebug
basebody = ['bbody.png', 'cbody.png', 'lbbody.png', 'ghbody.png']
basehead = ['bhead.png', 'chead.png', 'lbhead.png', 'ghhead.png']
baselegs = ['blegs.png', 'clegs.png', 'lblegs.png', 'ghlegs.png']
baseneck = ['bneck.png', 'cneck.png', 'lbneck.png', 'ghneck.png']
basewings = ['bwings.png', 'cwings.png', 'lbwings.png', 'ghwings.png']

#eyes
beyes = ['beyes0.png','beyes1.png', 'beyes2.png', 'beyes3.png', 'beyes4.png']
cricketeyes = ['ceyes0.png','ceyes1.png', 'ceyes2.png', 'ceyes3.png', 'ceyes4.png']
gheyes = ['gheyes0.png','gheyes1.png', 'gheyes2.png', 'gheyes3.png', 'gheyes4.png']
lbeyes = ['lbeyes0.png','lbeyes1.png', 'lbeyes2.png', 'lbeyes3.png', 'lbeyes4.png']

#patterns
bpattern = ['bpattern0.png', 'bpattern.png']
ghpattern = ['ghpattern0.png', 'ghpattern.png']
cpattern = ['cpattern0.png', 'cpattern.png']
lbpattern = ['lbpattern0.png', 'lbpattern.png']

#accessories
baccess = ['baccess0.png', 'baccess1.png', 'baccess2.png', 'baccess3.png', 'baccess4.png']
ghaccess = ['ghaccess0.png','ghaccess1.png', 'ghaccess2.png', 'ghaccess3.png', 'ghaccess4.png']
caccess = ['caccess0.png','caccess1.png', 'caccess2.png', 'caccess3.png', 'caccess4.png']
lbaccess = ['lbaccess0.png','lbaccess1.png', 'lbaccess2.png', 'lbaccess3.png', 'lbaccess4.png']

#misc
bmisc = ['bmisc0.png', 'bmisc1.png', 'bmisc2.png', 'bmisc3.png']
ghmisc = ['ghmisc0.png', 'ghmisc1.png', 'ghmisc2.png', 'ghmisc3.png']
cmisc = ['cmisc0.png', 'cmisc1.png', 'cmisc2.png', 'cmisc3.png']
lbmisc = ['lbmisc0.png', 'lbmisc1.png', 'lbmisc2.png', 'lbmisc3.png']

stat = 0
access = 0
misc = 0
pattern = 0
headcolor = 0
legcolor = 0
wingcolor = 0
bodycolor = 0
neckcolor = 0
bug = 0
parts = 0
eyes = 0

options = 80


def setup():
    size(1000,1000)
    background('#FFFFFF')
    mode = 'bugchoose'
    

#Define the different Modes
def modechoose():
    global mode
    
    if 70 < mouse_y < 125 and mouse_x < 140:
        mode = 'bugchoose'
        print(mode)
        
    if 135 < mouse_y < 180 and mouse_x < 140:
        mode = 'color'
        print(mode)
        
    if 190 < mouse_y < 225 and mouse_x < 140:
        mode = 'headcolor'
        print(mode)
        
    if 230 < mouse_y < 265 and mouse_x < 140:
        mode = 'neckcolor'
        print(mode)
        
    if 268 < mouse_y < 305 and mouse_x < 140:
        mode = 'bodycolor'
        print(mode)
    
    if 310 < mouse_y < 345 and mouse_x < 140:
        mode = 'wingcolor'
        print(mode)
        
    if 350 < mouse_y < 375 and mouse_x < 140:
        mode = 'legcolor'
        print(mode)
        
    if 455 < mouse_y < 505 and mouse_x < 140:
        mode = 'eyeselect'
        print(mode)
        
    if 390 < mouse_y < 440 and mouse_x < 140:
        #mode = 'pattern'
        #secondmode = 'patternchoose'
        mode = 'pattern'
        #print(secondmode)
        print(mode)
        
    if 520 < mouse_y < 577 and mouse_x < 140:
        mode = 'access'
        print(mode)
        
    if 580 < mouse_y < 650 and mouse_x < 140:
        mode = 'misc'
        print(mode)
  #Reset button
    if 927 < mouse_y < 1000 and mouse_x < 140:
        reset()
    
def draw():
    print(mouse_x, mouse_y)
    
    global mode, tintcolor, patterns, misccol, misccolor, accesscol, accesscolor, stat, perk
    

#Switching between modes!
    if mode == 'bugchoose':
        background('#FFFFFF')
        tint(patterns[0])
        UI = load_image('UI/bugs.png')
        image(UI, 0, 0)
    
    elif mode == 'color':
        background('#FFFFFF')
        tint(patterns[0])
        colorUI = load_image('UI/color.png')
        image(colorUI, 0, 0)
        
    elif mode == 'bodycolor':
        background('#FFFFFF')
        tint(patterns[0])
        bodyUI = load_image('UI/colorbody.png')
        image(bodyUI, 0, 0)
        
    elif mode == 'headcolor':
        background('#FFFFFF')
        tint(patterns[0])
        headUI = load_image('UI/colorhead.png')
        image(headUI, 0, 0)
    
    elif mode == 'neckcolor':
        background('#FFFFFF')
        tint(patterns[0])
        neckUI = load_image('UI/colorneck.png')
        image(neckUI, 0, 0)
        
    elif mode == 'wingcolor':
        background('#FFFFFF')
        tint(patterns[0])
        wingUI = load_image('UI/colorwings.png')
        image(wingUI, 0, 0)
        
    elif mode == 'legcolor':
        background('#FFFFFF')
        tint(patterns[0])
        legUI = load_image('UI/colorlegs.png')
        image(legUI, 0, 0)
    
    elif mode == 'eyeselect':
        background('#FFFFFF')
        tint(patterns[0])
        eyeselectUI = load_image('UI/eyes.png')
        image(eyeselectUI, 0, 0)
    
    
    elif mode == 'pattern':
        background('#FFFFFF')
        tint(patterns[0])
        patternUI = load_image('UI/pattern.png')
        image(patternUI, 0, 0)
        
    elif mode == 'access':
        background('#FFFFFF')
        tint(patterns[0])
        accessUI = load_image('UI/acces.png')
        image(accessUI, 0, 0)
        
    elif mode == 'misc':
        background('#FFFFFF')
        tint(patterns[0])
        miscUI = load_image('UI/misc.png')
        image(miscUI, 0, 0)
        
    #Call the statements!
    bstats = load_image('Stats/' + stats[stat])
    image(bstats, 0, 0)
        
    #Call the bug parts!
    BaseHead = load_image('BaseHead/' + basehead[parts])
    tint(tints[headcolor])
    image(BaseHead, 0, 0)
    tint(tints[0])
    bhead = load_image('BaseHead/bhead.png')
    
    BaseBody = load_image('BaseBody/' + basebody[parts])
    tint(tints[bodycolor])
    image(BaseBody, 0, 0)
    tint(tints[0])
    bbody = load_image('BaseBody/bbody.png')
    
    BaseWings = load_image('BaseWings/' + basewings[parts])
    tint(tints[wingcolor])
    image(BaseWings, 0, 0)
    tint(tints[0])
    bwings = load_image('BaseWings/bwings.png')
    
    BaseLegs = load_image('BaseLegs/' + baselegs[parts])
    tint(tints[legcolor])
    image(BaseLegs, 0, 0)
    tint(tints[0])
    blegs = load_image('BaseLegs/blegs.png')
    
    BaseNeck = load_image('BaseNeck/' + baseneck[parts])
    tint(tints[neckcolor])
    image(BaseNeck, 0, 0)
    tint(tints[0])
    bneck = load_image('BaseNeck/bneck.png')
    
    #Call the patterns!
    if bug == 0: 
        tint(tintcolor)
        bpattern1 = load_image('bpattern/' + bpattern[pattern])
        image(bpattern1, 0, 0)
        
    if bug == 1:
        tint(tintcolor)
        cpattern1 = load_image('cpattern/' + cpattern[pattern])
        image(cpattern1, 0, 0)
    
        
    if bug == 2:
        tint(tintcolor)
        lbpattern1 = load_image('lbpattern/' + lbpattern[pattern])
        image(lbpattern1, 0, 0)
        
    if bug == 3:
        tint(tintcolor)
        ghpattern1 = load_image('ghpattern/' + ghpattern[pattern])
        image(ghpattern1, 0, 0)
    
    
    #Call the bugs!
    BugType = load_image('BugTypes/' + bugs[bug])
    image(BugType, 0, 0)
    
    
    
    #Call the eyes!
    if bug == 0: 
        tint(patterns[0])
        beye1 = load_image('beyes/' + beyes[eyes])
        image(beye1, 0, 0)
        
    elif bug == 1: 
        tint(patterns[0])
        ceye1 = load_image('cricketeyes/' + cricketeyes[eyes])
        image(ceye1, 0, 0)
        
    elif bug == 2:
        tint(patterns[0])
        lbeye1 = load_image('lbeyes/' + lbeyes[eyes])
        image(lbeye1, 0, 0)
        
    elif bug == 3:
        tint(patterns[0])
        gheye1 = load_image('gheyes/' + gheyes[eyes])
        image(gheye1, 0, 0)
        
    #Call the accessories!
    if bug == 0:
        tint(accesscolor)
        baccess1 = load_image('baccess/' + baccess[access])
        image(baccess1, 0, 0)
    
    if bug == 1:
        tint(accesscolor)
        caccess1 = load_image('caccess/' + caccess[access])
        image(caccess1, 0, 0)
        
    if bug == 2:
        tint(accesscolor)
        lbaccess1 = load_image('lbaccess/' + lbaccess[access])
        image(lbaccess1, 0, 0)
        
    if bug == 3:
        tint(accesscolor)
        ghaccess1 = load_image('ghaccess/' + ghaccess[access])
        image(ghaccess1, 0, 0)
        
    #Call the misc!
    if bug == 0:
        tint(misccolor)
        bmisc1 = load_image('bmisc/' + bmisc[misc])
        image(bmisc1, 0, 0)
    
    if bug == 1:
        tint(misccolor)
        cmisc1 = load_image('cmisc/' + cmisc[misc])
        image(cmisc1, 0, 0)
        
    if bug == 2:
        tint(misccolor)
        lbmisc1 = load_image('lbmisc/' + lbmisc[misc])
        image(lbmisc1, 0, 0)
        
    if bug == 3:
        tint(misccolor)
        ghmisc1 = load_image('ghmisc/' + ghmisc[misc])
        image(ghmisc1, 0, 0)
        
    #Selectbutton
    select = load_image('UI/select.png')
    image(select, 0, 0)
    
    #Calling Perks!
    if perk == 'devilish':
        devilishperk = load_image('Stats/devilish.png')
        image(devilishperk, 0, 0)
        
    if perk != 'devilish':
        transparent = load_image('lbaccess/lbaccess0.png')
        image(transparent, 0, 0)
        
    if perk == 'none':
        transparent = load_image('lbaccess/lbaccess0.png')
        image(transparent, 0, 0)
        
    if perk == 'neko':
        neko = load_image('Stats/neko.png')
        image(neko, 0, 0)
        
    if perk == 'smart':
        smartperk = load_image('Stats/smart.png')
        image(smartperk, 0, 0)
        
    if perk == 'dapper':
        enlightenedperk = load_image('Stats/dapper.png')
        image(enlightenedperk, 0,0)
        
    if perk == 'waifu':
        waifu = load_image('Stats/waifu.png')
        image(waifu, 0, 0)
        
    if perk == 'buffedwaifu':
        buffedwaifu = load_image('Stats/buffedwaifu.png')
        image(buffedwaifu, 0, 0)
  

def key_pressed():
    global mode, tintcolor, patterns, accesscolor, accesscol, misccol, misccolor
    if mode == 'pattern' and key.isdigit():
        k = int(key) - 1
        
        if k <len(patterns):
            tintcolor = patterns[k]
            
    if mode == 'access' and key.isdigit():
        k = int(key) - 1
        
        if k <len(accesscol):
            accesscolor = accesscol[k]
            
    if mode == 'misc' and key.isdigit():
        k = int(key) - 1
        
        if k <len(misccol):
            misccolor = misccol[k]
 
    
def mouse_clicked():
    
    #Choosing the different options and changing between them! Including setting perk type
    modechoose()
    
    global bodycolor, bug, parts, mode, colors, headcolor, legcolor, neckcolor, wingcolor, eyes, pattern, access, misc, stat, perk
    
    if mouse_x > 900 and mode == 'bugchoose':
        bug += 1
        stat += 1
        parts += 1
    
    elif mouse_x > 900 and mode == 'headcolor':
        headcolor += 1
        
    elif mouse_x > 900 and mode == 'bodycolor':
        bodycolor += 1
        
    elif mouse_x > 900 and mode == 'neckcolor':
        neckcolor += 1
        
    elif mouse_x > 900 and mode == 'legcolor':
        legcolor += 1
        
    elif mouse_x > 900 and mode == 'wingcolor':
        wingcolor += 1
        
    elif mouse_x > 900 and mode == 'eyeselect':
        eyes += 1
        if eyes == 4:
            perk = 'waifu'
            print(perk)
        if eyes != 4:
            perk = 'none'
        
    elif mouse_x > 900 and mode == 'pattern':
        pattern += 1
        
    elif mouse_x > 900 and mode == 'access':
        access += 1
        if access == 2 or access == 3:
            perk = 'smart'
            print(perk)
        if access != 2 and access !=3:
            perk = 'none'
            print(perk)
        
    elif mouse_x > 900 and mode == 'misc':
        misc += 1
        if misc == 2:
            perk = 'devilish'
            print(perk)
        if misc == 3:
            perk = 'neko'
            print(perk)
        
    
    if misc == 3 and access == 3:
        perk = 'none'
        print(perk)
        
    if access == 2 and misc == 1:
        perk = 'dapper'
        print(perk)
    
    if access == 3 and misc == 1:
        perk = 'dapper'
        print(perk)
    
    if eyes == 4 and access == 1:
        perk = 'buffedwaifu'
        print(perk)
    
    if eyes == 4 and access == 4:
        perk = 'buffedwaifu'
        print(perk)
        
    if eyes == 4 and access == 1 and misc == 1:
        perk = 'none'
        print(perk)
        
    if eyes == 4 and access == 1 and misc == 2:
        perk = 'none'
        print(perk)
        
    if eyes == 4 and access == 4 and misc == 1:
        perk = 'none'
        print(perk)
        
    if eyes == 4 and access == 4 and misc == 2:
        perk = 'none'
        print(perk)
        
    if eyes == 4 and access == 4 and misc == 3:
        perk = 'none'
        print(perk)
        
    if eyes == 4 and access == 1 and misc == 2:
        perk = 'none'
        print(perk)
        
    if eyes == 4 and access == 1 and misc == 3:
        perk = 'none'
        print(perk)

#Reset if over limit
        
    if access > 4:
        access = 0
        
    if misc > 3:
        misc = 0
        
    if pattern > 1:
        pattern = 0
    
    if eyes > 4:
        eyes = 0
        
    if wingcolor > 4:
        wingcolor = 0
        
    if neckcolor > 4:
        neckcolor = 0
    
    if legcolor > 4:
        legcolor = 0

    if headcolor > 4:
        headcolor = 0
    
    if bodycolor > 4:
        bodycolor = 0
        
    if bug > 3:
        bug = 0
        
    if stat > 3:
        stat = 0
        
    if parts > 3:
        parts = 0
        

def reset():
    global bodycolor, bug, parts, mode, colors, headcolor, legcolor, neckcolor, wingcolor, eyes, pattern, access, misc, stat, perk, tintcolor
    
    #Reset mode
    mode = 'bugchoose'
    perk = 'none'
    #Reset bug
    bug = 0
    parts = 0
    pattern = 0
    
    #Reset color
    headcolor = 0
    legcolor = 0
    neckcolor = 0
    wingcolor = 0
    bodycolor = 0
    
    #Reset tint
    tintcolor = patterns[0]
    tint(patterns[0])
    #Reset eyes
    eyes = 0
    
    #Reset misc and access
    access = 0
    misc = 0
    
    