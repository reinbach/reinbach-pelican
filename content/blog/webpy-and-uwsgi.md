Title: web.py and uwsgi
Date: 2012-07-08
Tags: webpy, uwsgi, nginx, python
Slug: webpy-and-uwsgi
Author: Greg Reinbach

Setting up a site developed with web.py on my servers using nginx and uwsgi and kept running into a couple of issues with uwsgi not responding as expected.

The first issue was simple enough and uwsgi logs provided the needed information. Python imports were not finding the needed packages. I tweaked the code to update the python paths.

The second issue took me a moment to work out. I kept seeing the following error in the logs;

    "application" must be a callable object in file....

Now I know I was telling uwsgi via nginx conf file that the application callable object was "app". But I got stuck on thinking that nginx was expecting the callable object to be "application" so I changed the app around to use application, but obviously that did not work.

A little research showed that web.py needs to make use of the following for uwsgi to work;

    application = app.wsgifunc()

Tweaked that to be;

    app = app.wsgifunc()

And everything worked like a charm. The following is the wrapper I used on the application to handle the above issues.

    import sys
    import os 

    prev_sys_path = list(sys.path)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    new_sys_path = [p for p in sys.path if p not in prev_sys_path]
    for item in new_sys_path:
        sys.path.remove(item)
        sys.path[:0] = new_sys_path
    
    from code import app

    app = app.wsgifunc()

    if __name__ == '__main__':
        app.run()

The part "from code import app" is the part that pulls in the web.py application. This file is set as the app and as callable in nginx conf file.
