A Proof Of Concept Uploader
===========================

Had this crazy idea the other day to make an improved file uploader using just a localhost
little webserver that websites can check to see if it exists.  If it does they can punch
people over to their uploader, and then it'll let them pick a local file and push it to
an S3 bucket.

This a total hack to just see if it works.  That means if you want to use it you have to
do some hacking on this little bit of code and do some yak shaving.  Don't ask me for 
help because I sort of don't care about it, it's just a random idea I cranked out.

I have it on good authority, after showing this to a friend, that at least one company
almost has this feature, but they're too stupid to realize they could solve the "upload problem".
Let's hope they read this, and then get their head out of their ass to make it a reality.

But, with that being said, I came up with this independently and then was told they had it.


Trying It Out
=============

I've opened up a bucket on S3 so people can try it out.  If it gets abused
I'm going to close it up.  Oh, I'm sure it'll last a day but here's how to try
it.

1. git clone https://github.com/zedshaw/poc-uploader.git
2. cd poc-uploader
3. pip install lpthw.web boto
4. python app.py
5. Go to http://zedshaw.com/uploader.html
6. Do what it says, maybe it'll work.

If it blows up then you have to setup your own S3 because I disabled it.


Setting It Up Yourself
======================

I'm assuming you can get the code with git.  After you do that do this:

1. Get an Amazon S3 account.
2. Create a bucket where you want the test files to go.
3. Change the permissions on the bucket so that it is Upload/Delete and List accessible
    to everyone.  Yes, this sucks but it's just a test. Talk to the boto guys
    about why they try to list a bucket and explode violently when they can't.
4. Open the app.py file and change the `bucket_name` variable to use the name
    of your bucket.

Now that you've got that working, do this:

1. python app.py
2. http://zedshaw.com/uploader.html
3. Go through it again.
4. File should be in *your* S3 account, even though you were on my site.


Trying It On Your Site
======================

Put the file templates/receiver.html on your site and just hit it with a
browser.


Is It Secure?
=============

What? Heellllsssss no, not right now.  It should be alright since the
browser can't touch what's inside the iframe, but you never know what
some jackass can figure out or what all browsers allow.

I would recommend in the future that this locally running server use 
some Desktop notifications and confirmations to make sure that rogue
sites can't force uploads.

I'd also say that having an uploader like this is only half of 
solving the "upload problem" on the web.  If you can combine this
with the following features you'll have something:

1. Chunking the files into 4M pieces and storing them in the bucket
    as a bunch of chunks. Then sending a metadata to the target site
    so they know how to rebuild it.
2. Adding encryption on the uploaded file chunks.
3. Solid status notifications from the uploader to the site on progress.
4. Making it work reliably with crap internet that goes down.  If you
    have 4M chunking, good encryption on each chunk, and a way to check
    what's been uploaded, then you've got the basis of reliable async
    uploads.
5. Doing all this crap for target sites so they just get pure uploads with
    nothing to worry about.


Why Don't You Do It?
====================

I just did, now I'm bored.  I'd rather write books and play guitar than
try to figure out how to scale an uploader service.


What's The License?
===================

It's copyright, by me.  You can't use this code in jack shit, but you
can steal the idea all you want.  Hurry though because Apple might
patent it and sue you.



