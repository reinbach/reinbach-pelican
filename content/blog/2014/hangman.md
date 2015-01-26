Title: Hangman
Date: 2014-01-01
Tags: games, python, algorithms
Slug: hangman
Author: Greg Reinbach

Onto the next stage of game development, developing a Hangman game.

Actually Hangman can be developed instead of a text adventure game if text adventure games are not your thing. As with a text adventure game, Hangman is very much straight programming, and nothing fancy.

The one interesting thing I did in my version of the Hangman game was to make use of the algorithm R(3.4.2) (Waterman's "Reservoir Algorithm") from Knuth's "The Art of Computer Programming" (simplified version). I used it to generate my random word.

    #!python
    def get_random_word():
        # using algorithm R(3.4.2) (Waterman's "Reservoir Algorithm")
        # from Knuth's "The Art of Computer Programming" (simplified version)
        #
        # get random word from word file
        # - ignore words that are less than 3 chars
        with open(WORD_FILE, "r") as fp:
            line = next(fp)
            for num, aline in enumerate(fp):
                if len(aline) <= 2 or random.randrange(num + 2):
                    continue
                line = aline
            return line.strip()


Source: [StackOverflow](http://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python)

I grabbed a list of words from [FreeBSD](http://www.freebsd.org/cgi/cvsweb.cgi/src/share/dict/web2?rev=1.12;content-type=text%2Fplain). This list of words is a text file with a word per line. So to select a random word I need to select a random line. With that in mind I used the above algorithm to randomly select a line from the word file, thus giving me my random word.

The rest of the program is pretty straight forward.

Source is at [https://github.com/reinbach/hangman](https://github.com/reinbach/hangman)

Onto the next step...