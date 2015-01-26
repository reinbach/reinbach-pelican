Title: Golang Web Apps
Date: 2014-04-05
Tags: golang
Slug: golang-webapps-1
Author: Greg Reinbach

This is a short simple guide about using golang for web application development.

The idea is that we start with the straight golang net/http package and slowly develop a more complex web application each time as our needs grow. Adding a component, or functionality to the system to solve the identified need.

All code can be found at [https://github.com/reinbach/golang-webapp-guide](https://github.com/reinbach/golang-webapp-guide)


Basics
-------

Firstly we start with the absolute basics. Which is to handle a request and return a response.

    #!golang
    package main

    import (
        "io"
        "log"
        "net/http"
    )

    func Home(w http.ResponseWriter, req *http.Request) {
        io.WriteString(w, "Hello World!")
    }

    func main() {
        http.HandleFunc("/", Home)
        err := http.ListenAndServe(":8000", nil)
        if err != nil {
        	log.Fatal("ListenAndServe: ", err)
        }
    }

Save the above to a file (eg: `server.go`) and then you can run it with the following;

    go run server.go

And pointing our browser at `http://localhost:8000` you will get the following response;

    Hello World!

Awesome, we have a web application! Sadly it only returns string responses, and we want more. We want to return HTML, so it looks like a proper website.


HTML
----

To convert to HTML responses we replace the "io" package with the "html/template" package. We also want more than 1 page in our website. So we create a function to render the HTML templates, to keep things a little DRY, update the `Home` function, and add an `About` page. Now our `server.go` file looks like the following.


    #!golang
    package main

    import (
        "fmt"
        "html/template"
        "log"
        "net/http"
    )

    func Home(w http.ResponseWriter, req *http.Request) {
        render(w, "index.html")
    }

    func About(w http.ResponseWriter, req *http.Request) {
        render(w, "about.html")
    }

    func render(w http.ResponseWriter, tmpl string) {
        tmpl = fmt.Sprintf("templates/%s", tmpl)
        t, err := template.ParseFiles(tmpl)
        if err != nil {
        	log.Print("template parsing error: ", err)
        }
        err = t.Execute(w, "")
        if err != nil {
        	log.Print("template executing error: ", err)
        }
    }

    func main() {
        http.HandleFunc("/", Home)
        http.HandleFunc("/about/", About)
        err := http.ListenAndServe(":8000", nil)
        if err != nil {
        	log.Fatal("ListenAndServe: ", err)
        }
    }


Don't forget we need to add the `index.html` and `about.html` file. In the same directory as the `server.go` file create a `templates` directory and in that directory place the `index.html` and `about.html` files. So we have the following file layout.

    .
    ├── server.go
    └── templates
        ├── about.html
        └── index.html


So we have HTML pages, but they are lacking. We need to add some CSS to give our website some pop. Let's make use of [Bootstrap](http://getbootstrap.com/), it's a fantastic base to build a website on. At the same time let's make our templates a little DRYier by using a `base.html` file and the individual pages having just the content applicable to them.


STATIC
------

To serve our static content we can make use of `http.ServeContent` to do all the work for us. The nice thing about this, is that it handles the setting of the Content-Type for us. [See the docs for more information](http://golang.org/pkg/net/http/#ServeContent).


    #!golang
    func StaticHandler(w http.ResponseWriter, req *http.Request) {
        static_file := req.URL.Path[len(STATIC_URL):]
        if len(static_file) != 0 {
        	f, err := http.Dir(STATIC_ROOT).Open(static_file)
        	if err == nil {
        		content := io.ReadSeeker(f)
        		http.ServeContent(w, req, static_file, time.Now(), content)
        		return
        	}
        }
        http.NotFound(w, req)
    }


We also now have a `base.html` which is used in each response, so we tweak the render function to parse the `base.html` and pass in the `Context` to the template.


    #!golang
    func render(w http.ResponseWriter, tmpl string, context Context) {
        context.Static = STATIC_URL
        tmpl_list := []string{"templates/base.html",
        	fmt.Sprintf("templates/%s.html", tmpl)}
        t, err := template.ParseFiles(tmpl_list...)
        if err != nil {
        	log.Print("template parsing error: ", err)
        }
        err = t.Execute(w, context)
        if err != nil {
        	log.Print("template executing error: ", err)
        }
    }


With those changes we now have the following for our `server.go` file;

    #!golang
    package main

    import (
        "fmt"
        "html/template"
        "io"
        "log"
        "net/http"
        "time"
    )

    const STATIC_URL string = "/static/"
    const STATIC_ROOT string = "static/"

    type Context struct {
        Title  string
        Static string
    }

    func Home(w http.ResponseWriter, req *http.Request) {
        context := Context{Title: "Welcome!"}
        render(w, "index", context)
    }

    func About(w http.ResponseWriter, req *http.Request) {
        context := Context{Title: "About"}
        render(w, "about", context)
    }

    func render(w http.ResponseWriter, tmpl string, context Context) {
        context.Static = STATIC_URL
        tmpl_list := []string{"templates/base.html",
        	fmt.Sprintf("templates/%s.html", tmpl)}
        t, err := template.ParseFiles(tmpl_list...)
        if err != nil {
        	log.Print("template parsing error: ", err)
        }
        err = t.Execute(w, context)
        if err != nil {
        	log.Print("template executing error: ", err)
        }
    }

    func StaticHandler(w http.ResponseWriter, req *http.Request) {
        static_file := req.URL.Path[len(STATIC_URL):]
        if len(static_file) != 0 {
        	f, err := http.Dir(STATIC_ROOT).Open(static_file)
        	if err == nil {
        		content := io.ReadSeeker(f)
        		http.ServeContent(w, req, static_file, time.Now(), content)
        		return
        	}
        }
        http.NotFound(w, req)
    }

    func main() {
        http.HandleFunc("/", Home)
        http.HandleFunc("/about/", About)
        http.HandleFunc(STATIC_URL, StaticHandler)
        err := http.ListenAndServe(":8000", nil)
        if err != nil {
        	log.Fatal("ListenAndServe: ", err)
        }
    }


And our `index.html` file looks like;


    {{ define "content" }}
      <div class="page-header">
        <h1>{{ .Title }}</h1>
      </div>
      <p>We have a HTML web page, woot!</p>
    {{ end }}


The `about.html` will look very similar, but with content changed.

And our `base.html` file looks like;


    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Golang WebApp</title>
        <link rel="stylesheet" href="{{ .Static }}css/bootstrap.min.css" type="text/css">
        <link rel="shortcut icon" href="{{ .Static }}img/favicon.ico">
      </head>
      <body>
        <nav class="navbar navbar-default" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <a class="navbar-brand" href="/">Golang WebApp</a>
            </div>
            <div class="collapse navbar-collapse">
              <ul class="nav navbar-nav">
                <li><a href="/about/">About</a></li>
              </ul>
            </div>
          </div>
        </nav>
        <div class="container">
          {{ template "content" . }}
        </div>
      </body>
    </html>


We have set our static path as a constant in the `server.go` and are passing it to the `base.html` template via the context. This allows us to change the path/location of the static content in one location. Don't forget to download [Bootstrap](http://getbootstrap.com/) and place the files in the `static/` directory. Which should result in the following file layout;


    .
    ├── server.go
    ├── static
    │   ├── css
    │   │   ├── bootstrap.min.css
    │   │   └── ...
    │   ├── fonts
    │   │   └── ...
    │   ├── img
    │   │   └── favicon.ico
    │   └── js
    │       └── ...
    └── templates
        ├── about.html
        ├── base.html
        └── index.html


Nice, now we have the basis for a decent website that can be styled to our heart's content. At this point we have the basis for a static website.
