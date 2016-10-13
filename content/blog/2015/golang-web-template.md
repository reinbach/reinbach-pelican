Title: Golang - Web - Templating
Date: 2015-04-04
Tags: golang
Slug: golang-web-templating
Author: Greg Reinbach

Full templating functionality in our website. We want to be able to pass in data to the templates and determine which templates are to be used when generating our response.

This is a continuation of the [Golang Web Apps](/golang-webapps-1.html) and the source code can be found at [https://github.com/reinbach/golang-webapp-guide](https://github.com/reinbach/golang-webapp-guide).

To better organize the code we move all the templating functionality, the templates, and the static files into a separate directory. Which now gives us the following file layout.

    .
    ├── server.go
    └── template
        ├── constants.go
        ├── context.go
        ├── html
        │   └── ...
        ├── render.go
        └── static
            └── ...


The render functioned is tweaked in a couple of ways;

   * A context parameter (data for the template) is passed to the render function
   * A list of templates is now expected instead of a single template.


The `UpdateTemplateList` function is used to prepend the full path to the templates.

    #!python
    func UpdateTemplateList(tmpls []string) []string {
         d := GetAbsDir("template", TEMPLATE_DIR)
         for i, v := range tmpls {
             tmpls[i] = filepath.Join(d, v)
         }
         return tmpls
     }

And for that we made use of a constant, and so went a step further and moved all our constants into a sepatate `constants` file, which now has the following;

    const (
          STATIC_URL     string = "/static/"
          STATIC_ROOT    string = "static/"
          TEMPLATE_DIR   string = "html/"
          PARENT_PACKAGE string = "template"
     )

If we wanted to rename the directories, we would need to just update this file.

With those above changes we now changed our `home` and `about` functions to the following;

    func Home(c web.C, w http.ResponseWriter, r *http.Request) {
         ctx := template.NewContext()
         ctx.Add("HomePage", true)
         template.Render(c, w, r, append(templates, "home.html"), ctx)
    }

    func About(c web.C, w http.ResponseWriter, r *http.Request) {
         ctx := template.NewContext()
         ctx.Add("AboutPage", true)
         template.Render(c, w, r, append(templates, "about.html"), ctx)
    }

Lastly we also make use of [goji](https://goji.io/) to handle routing and middleware extensibility for us. This requires a small changes to our `main` function in the `server.go` file. We simple swap out most of the `http.HandleFunc` calls with `goji.Get` and use `goji.Serve()` instead of the `http.ListenAndServe(":8000", nil)` So the `main` function looks like;

    func main() {
        http.HandleFunc(template.STATIC_URL, template.StaticHandler)
        goji.Get("/", Home)
        goji.Get("/about", About)
        goji.NotFound(NotFound)

        goji.Serve()
    }


As you may have noticed we also added a `NotFound` to catch any addresses that we cannot resolve.

    func NotFound(c web.C, w http.ResponseWriter, r *http.Request) {
        template.Render(c, w, r, append(templates, "404.html"),
            template.NewContext())
    }

And now we have a separate module that handles the template rendering and serving of static files for us.
