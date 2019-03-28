import winsound

def done():
    for freq in [600, 900, 1000, 900, 1200]:
        winsound.Beep(freq, 140)

done()
