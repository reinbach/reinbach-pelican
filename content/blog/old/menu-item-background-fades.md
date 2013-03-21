Title: menu item background fades
Date: 2009-09-30
Tags: css, html
Slug: menu-item-background-fades
Author: Greg Reinbach

A project I am working on required that the menu item's background fade when the user mouses over it and this is my hack in achieving it.

I must admit this is not the prettiest as there is some duplication of information, buy as with most projects there was a time crunch and this is what I came up with in the allocated time.

First you have your usual menu code:

	<ul>
		<li>
			<a href="">
				<span class="in">Home</span>
				<span class="out">Home</span>
			</a>
		</li>
		<li>
			<a href="">
				<span class="in">About</span>
				<span class="out">About</span>
			</a>
		</li>
		<li>
			<a href="">
				<span class="in">Contact</span>
				<span class="out">Contact</span>
			</a>
		</li>
	</ul>

Here you notice that I have placed 2 span tags with in the link tags, this is where it is not pretty with the duplication of the link text.

To this we add the necessary styling:

	ul {
		padding: 0;
		background: url('./images/background_menu.jpg') repeat-x scroll 0 0;
		height: 40px;
		position: relative;
	}

	ul li {
		float: left;
		list-style: none;
		padding: 0;
		margin: 0;
		line-height: 40px;
		position: relative;
	}

	ul li a {
		width: 100px;
		float: left;
		display: block;
		text-align: center;
	}

	ul li span.out {
		position: absolute;
		top: 0;
		left: 0;
		display: none;
		background: url('./images/background_menu_active.jpg') repeat-x scroll 0 0;
		width: 100px;
		float: left;
	}

The position elements are what are critical in having this work correctly. So make sure you get those done properly.

Finally. to make it all work you have the javascript which makes use of jQuery:

	$(document).ready(function()
	{
		$('ul li a').hover(
			function()
			{
				$(this).find("span.in").each(function(){ $(this).fadeOut('slow')});
				$(this).find("span.out").each(function(){ $(this).fadeIn('slow')});
			},
			function()
			{
				$(this).find("span.in").each(function(){ $(this).fadeIn('slow')});
				$(this).find("span.out").each(function(){ $(this).fadeOut('slow')});
			}
		);
	});

That's it.
