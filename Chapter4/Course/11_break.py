for i in range(1,5):
    print(f"Today is day {i}, Ready to confess my love....")
    if input(f"Si vous ete Mei, faites-moi savoir si vous me rejetez explicitement "
             f"(0 pour regarder et observer à nouveau,"
             f"1 inapproprié pour rejeter):") == '1':
        print("Xiao Mei m'a rejeter, je ne poursuivrai plus Xiao Mei,")
        break
    print("j'envoie des fleurs à Xiao Mei")
    print()
