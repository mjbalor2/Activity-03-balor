import mj_stat as mj
import mary_ev as mr

counter = 1
while counter == 1:
    print ("\n[1] Stat Calculator")
    print ("[2] EV Calculator")
    num0 = int(input("Choose number: "))

    BAS = int (input("\nBase STAT:"))
    LVL = int (input("LEVEL:"))
    EV = int (input("EVHP:"))
    IV = int (input("IVHP:"))
    STAT = int(input("Desired increase in stat:"))

    if num0 == 1:
        print ("\nHP = ", mj.maryjo.hpcal(BAS,IV,EV,LVL))
        print ("ATTACK = ", mj.maryjo.otherstat(BAS,IV,EV,LVL))
        print ("DEFENSE = ", mj.maryjo.otherstat(BAS,IV,EV,LVL))
        print ("SUPER ATTACK = ", mj.maryjo.otherstat(BAS,IV,EV,LVL))
        print ("SUPER DEFENSE = ", mj.maryjo.otherstat(BAS,IV,EV,LVL))
        print ("SPEED = ", mj.maryjo.otherstat(BAS,IV,EV,LVL))
        print ("\nThe needed Evs to increase stat is ", mr.mary.evneed(STAT,BAS,IV,EV,LVL))
    
    elif num0 == 2:
        print ("\n[1] Single stat")
        print ("[2] All stat")
        num1 = int (input("Choose a number:"))

        if num1 == 1:
            print ("\n[1] ATTACK")
            print ("[2] DEFENSE")
            print ("[3] SUPER ATTACK")
            print ("[4] SUPER.DEFENSE")
            print ("[5] SPEED=")
            print ("[6] HP")
            num20= int (input ("Choose Stat:"))

            if num20 == 1 or 2 or 3 or 4 or 5:
                print ("\nThe Stat is", mj.maryjo.otherstat(BAS,IV,EV,LVL))
            elif num20 == 6:
                print ("\nHP = ", mj.aime.hpcal(BAS,IV,EV,LVL))

        elif num1 == 2:
            print ("\nHP =", mj.maryjo.hpcal(BAS,IV,EV,LVL))
            print ("ATTACK =", mj.maryjo.otherstat(BAS,IV,EV,LVL))
            print ("DEFENSE =", mj.maryjo.otherstat(BAS,IV,EV,LVL))
            print ("SUPER. ATTACK =", mj.maryjo.otherstat(BAS,IV,EV,LVL))
            print ("SUPER DEFENSE=", mj.maryjo.otherstat(BAS,IV,EV,LVL))
            print ("SPEED", mj.maryjo.otherstat(BAS,IV,EV,LVL))
    
    print ("\n[1] Perform another calculation")
    print ("[2] End the program")
    num3 = int (input("choose a number:"))
    if num3 ==2:
        break
    elif num3 == 1:
        continue
