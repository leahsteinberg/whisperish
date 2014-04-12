#Whisperish
Aren't the weird emails you send your friends and lovers the best writing there is? Intense email correspondences are a language of their own. Whisperish makes gibberish of that language.

####How it works
Grabs all emails between two designated people off of gmail. Cleans up the emails and analyzes each set of emails, assigning to each word the words that come after it and their respective frequency. Builds a Markov Chain model of these words and randomly walks through it, building up plausible but nonsensical sentences that sound like you *might* have written them. Returns a dialogue between the two email-writers. Reads like a horrible play, but also sort of great.

####How to use it 
Right now, clone the repository, make a file called password.py that defines: "email_address" (your email address), "correspondence" (the email of the person you've been writing back and forth with) and "password" (your password). (yeahhh... that's why this isn't on the internet and doesn't exactly scream scalability...). First, make sure you have subdirectory called "texts" in this directory. To run it, type python whisperish.py.
