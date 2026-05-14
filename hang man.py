import random

words = ["apple", "test", "for", "banana"]
chos = random.choice(words)
bisplay = ["_"] * len(chos)
zz = 6 # عدد المحاولات

hang1=("""
      +---+
      |   
      |   
      |  
      |  
    =========
    """)
hang2=("""
      +---+
      |   |
      |   
      |  
      |  
    =========
    """)
hang3=("""
      +---+
      |   |
      |   o
      |  
      |  
    =========
    """)
havg4=("""
      +---+
      |   |
      |   o
      |  /
      |  
    =========
    """)
hang5=("""
      +---+
      |   |
      |   o
      |  /|\\
      |  
    =========
    """)
hang6=("""
      +---+
      |   |
      |   o
      |  /|\\
      |  / 
    =========
    """)
hang7=("""
      +---+
      |   |
      |   o
      |  /|\\
      |  / \\
    =========
    """)
# الشرط هنا يقول: استمر "فقط" إذا لم تكتمل الكلمة "و" كانت الأرواح أكبر من صفر
while "".join(bisplay) != chos and zz > 0:
    if zz==6:
        print(hang1)
    elif zz==5:
        print(hang2)
    elif zz==4:
        print(hang3)
    elif zz==3:
        print(havg4)
    elif zz==2:
        print(hang5)
    elif zz==1:
        print(hang6)
    print(f"\nAttempts left: {zz}")
    print(f"Current word: {' '.join(bisplay)}")
    inp_guss = input("Guess a letter: ").lower()
    
    
    if inp_guss in chos:
        # إذا الحرف صح، نضعه في مكانه
        for i in range(len(chos)):
            if chos[i] == inp_guss:
                bisplay[i] = inp_guss
        print("Good job!")
    else:
        # إذا الحرف خطأ، ننقص محاولة واحدة
        zz -= 1
        print(f"Wrong! '{inp_guss}' is not in the word.")

# الآن، إذا خرجنا من الحلقة، نتحقق: هل خرجنا لأننا فزنا أم لأن الأرواح انتهت؟
if "".join(bisplay) == chos:
    print(f"\nCongratulations! The word was: {chos}")
    print("* YOU WON *")
else:
    print("\nGAME OVER")
    print(f"The word was: {chos}")
    print(hang7)
