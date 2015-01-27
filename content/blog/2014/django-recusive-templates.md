Title: Django - Recursive Templates
Date: 2014-12-23
Tags: django
Slug: django-recursive-templates
Author: Greg Reinbach


The scenario I had was that of a table showing a list of accounts and these accounts had subaccounts. I wanted a simple way to display these subaccounts, but indented slightly relative to their parent. And I did not know the number of levels involved.

The following is the way I went about solving this in this instance was to call django templates recursively.

Create a templatetag to handle the display of displaying indentation character the correct number of times;

    #!python
    from django import template
    from django.template.defaultfilters import stringfilter

    register = template.Library()


    @register.filter
    @stringfilter
    def repeat(value, arg):
        return value * int(arg)


Then in the templates, we have the initial code that calls the rows template;

    #!html
    <tbody>
      {% for account in object_list %}
        {% with depth=0 %}
          {% include "row.html" %}
        {% endwith %}
      {% endfor %}
    </tbody>


 and the row template calls itself when applicable;

    #!html
    <tr>
      <td>
        {{ "-"|repeat:depth }}
        {{ account.name }}
      </td>
    </tr>

    {% if account.is_category %}
      {% with depth=depth|add:"1" %}
        {% for account in account.subaccounts %}
          {% include "row.html" %}
        {% endfor %}
      {% endwith %}
    {% endif %}



####Caveats

 - Not a ridiculous number of accounts, less than 100
 - Do not expect a large number of levels, maybe 3 or 4 at most

I have not measured to see how crazy this may be in processing/resources as yet, but from everyday usage so far it has not been an issue. So if not experiencing any performance issues, I'm not going to waste time trying to find out if there are any.
