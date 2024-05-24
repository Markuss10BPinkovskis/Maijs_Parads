def lasit_printet(README):
    try:
        with open(README, 'r') as file:
            print(lasit_tgt)
    except FileNotFoundError:
        print(f"problēma'{README}' nav atrodams")
    except Exception as e:
        print(f"uzradās problēma: '{e}' ")

    lasit_printet = "README.txt"
    lasit_printet(lasit_tgt)