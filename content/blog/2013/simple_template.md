Title: html/templates parsing multiple files
Date: 2013-12-27
Tags: golang
Slug: html-templates-parsing-multiple-files
Author: Greg Reinbach

Working with Django templating engine or Jinja2 you have the ability to inherit/extend templates. which I find very helpful in keeping things DRY. Now working on a golang app I wanted something similar and this is how I ended up doing it using the base packages.

I'm sticking with the base packages for my first few apps, so I can actually learn them. When starting out with Python, I used Django mainly and I feel that was not the correct thing to do, as Django black boxed a lot of functionality and it took a while to get a deeper understanding.

Anyway back to golang and templating. Here I'm making use of the [html/template](http://golang.org/pkg/html/template/) package.

Create the `base` file;

    #!html
    <html>
      <body>
        <h1>{{ template "title" }}</h1>

        {{ template "content" }}
      </body>
    </html>

So here we are expecting a couple of overrides, `title` and `content` which the templates that extend this `base` file need to provide. A sample file extending this `base`;

    #!html
    {{ define "title" }}About{{ end }}

    {{ define "content" }}
      <p>About us page now</p>
    {{ end }}

In this file you can see that we define the `title` and `content` information, which is used/needed by the `base` file.

Now we can parse these files with the html/template package and the final result will be the combination of these 2 files.

    t, err := template.ParseFiles("base.html", "index.html")

The order of the files provided in this call is important. You will always want the `base.html` file to be the first file in the list, otherwise you will end up with a blank result.

A complete sample go file that does this;

    #!golang
    package main

    import (
        "flag"
        "fmt"
        "html/template"
        "os"
    )

    var (
        file string
    )

    func init() {
        flag.StringVar(&file, "file", "index.html", "template file")
        flag.Parse()
    }

    func main() {
        t, err := template.ParseFiles("base.html", file)
        if err != nil {
        	fmt.Println("template parse error: ", err)
        	return
        }
        err = t.Execute(os.Stdout, "")
        if err != nil {
        	fmt.Println("template executing error: ", err)
        	return
        }
    }


Make use the html files are in the same dir as the above file, you can then run it and see the results;

    $ go run main.go

    <html>
      <body>
        <h1>Home</h1>


      <p>We are at the home page</p>

      </body>
    </html>

Or pass in the file option to use a the `about.html` file

    $ go run main.go -file=about.html

    <html>
      <body>
        <h1>About</h1>


      <p>About us page now</p>

      </body>
    </html>

Take the above with a grain of salt. I'm just starting out with golang and this is just the solution I came up with that works well for me at the moment. Also note that html/template is an extension of [text/template](http://golang.org/pkg/text/template/), so this should be applicable there as well, so not just limited to html.