import boto
import os
import sys
from boto.s3.key import Key
import web

urls = (
  '/', 'Index',
  '/upload', 'Upload',
    '/push', 'Push'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

# this is apparently broken in latest boto HEAD because they
# like breaking things.
bucket_name = "zedshaw.uploadertest"
CONN = boto.connect_s3(anon=True)
BUCKET = CONN.get_bucket(bucket_name)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def upload_file(bucket, base, thename):
    thefile = "%s/%s" % (base, thename)

    k = bucket.get_key(thename)

    if k and k.exists():
        print "Already uploaded %s" % thefile
    else:
        print 'Uploading %s to Amazon S3 bucket %s' % \
           (thefile, bucket_name)
        k = Key(bucket)
        k.key = thename
        k.set_contents_from_filename(thefile,
                cb=percent_cb, num_cb=10)
        k.set_acl("public-read")
        k.set_metadata("Content-Type", "application/ogg")

    return thename

class Index(object):
    def GET(self):
        params = web.input(site=None)
        return render.index(site=params.site)

class Upload(object):
    def GET(self):
        params = web.input(site = None)
        uploads = os.listdir("uploads")
        return render.upload(site=params.site, uploads=uploads)

class Push(object):
    def GET(self):
        params = web.input(site = None, target = None)
        if not params.target:
            return "Get it right."
        else:
            upload_file(BUCKET, "uploads", params.target) 
            return render.doingit(site = params.site, target = params.target)


if __name__ == "__main__":
    app.run()
