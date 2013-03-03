Title: jQuery slider
Date: 2009-02-10
Tags: javascript
Slug: jquery-slider
Author: Greg Reinbach

I thought about making use of the <a href="http://docs.jquery.com/UI/Slider">jQuery slider effect</a> for a project I am working on.

Let me just say that I felt like an idiot at first. All the necessary libs were installed and being called correctly, but nothing was coming up. After much head scratching, I finally realized that I needed to provide styling for the slider for it to show up.

So at the very least have something along these lines;

<code>
.ui-slider { 
&nbsp;   position: relative; 
&nbsp;   text-align: left; 
&nbsp;   border: 1px solid #ccc; 
&nbsp;   height: 5px;
}
.ui-slider .ui-slider-handle { 
&nbsp;   position: absolute; 
&nbsp;   z-index: 2; 
&nbsp;   width: 9px; 
&nbsp;   height: 9px; 
&nbsp;   cursor: default; 
&nbsp;   border: 1px solid #666;
}
.ui-slider .ui-slider-range { 
&nbsp;   position: absolute; 
&nbsp;   z-index: 1; 
&nbsp;   font-size: 1%; 
&nbsp;   display: block; 
&nbsp;   border: 0; 
}
</code>
