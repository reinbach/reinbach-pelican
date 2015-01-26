Title: sockJS Examples
Date: 2013-12-30
Tags: golang, sockjs
Slug: sockjs-example
Author: Greg Reinbach

Came across [sockjs for go](https://github.com/igm/sockjs-go/sockjs) and seeing that I had created some code examples using socket.io and python, I decided to do the same using golang of sockjs, as an excuse to play with it.

So far the examples are pretty simple.

But I got to play with tickers and goroutines in go, so that was nice. I actually used the net/http package for handling the requests and did a little template parsing. It is really nice to be able to use base packages to achieve all this. It makes go really nice to play with.

The examples can be found at [https://github.com/reinbach/sockjs-go-example](https://github.com/reinbach/sockjs-go-example)