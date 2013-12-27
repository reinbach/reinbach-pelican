Title: Benchmark Golang, C, and Python
Date: 2013-12-26
Tags: golang, python, c
Slug: benchmark
Author: Greg Reinbach

I was wondering how performant Golang is, so I decided to put together a little benchmarking example for myself.

So I started with Python, which is what I know best and created the following simple script;

    #!/usr/bin/env python

    def fac(n):
        if n == 0:
            return 1
        return n * fac(n - 1)

    if __name__ == "__main__":
        t = 0
        for j in range(100000):
            for i in range(8):
                t += fac(i)
        print("total: {0}".format(t))


The reason for the `total` output, was to have a check to ensure that I was getting the same results in each of the scripts. To make sure that they are doing the same amount of work.

Running the script gives us the following execution time;

    $ time ./factorial.py

    total: 591400000

    real    0m1.055s
    user    0m1.053s
    sys     0m0.000s

So I am getting about 1s in total execution time. Not bad.

Now the same code sample in C, to see what the time execution would be;

    #!c
    #include <stdio.h>

    int fac(int);

    int fac(int n) {
      if (n == 0) {
        return 1;
      }
      return n * fac(n - 1);
    }

    main() {
      int i, j;
      int t = 0;

      for (j = 0; j < 100000; j++) {
        for (i = 0; i <= 7; i++) {
          t += fac(i);
        }
      }

      printf("total: %d\n", t);
    }

Compile and execute the above snippet of code;

    $ gcc factorial.c -o factorial
    $ time ./factorial

    total: 591400000

    real    0m0.029s
    user    0m0.027s
    sys     0m0.000

Ok, that's quite an improvement. This is C, so we do expect there to be a great improvement.

Finally we create our code sample in Go;

    #!go
    package main

    import "fmt"

    func fact(n int) int {
        if n == 0 {
            return 1
        }
        return n * fact(n-1)
    }

    func main() {
        t := 0
        for j := 0; j < 100000; j++ {
            for i := range []int{1, 2, 3, 4, 5, 6, 7, 8} {
                t += fact(i)
            }
        }
        fmt.Println("total: ", t)
    }

Then build and run the code sample and we get the following;

    $ go build factorial.go
    $ time ./factorial

    total:  591400000

    real    0m0.026s
    user    0m0.020s
    sys     0m0.003s

So, that's pretty much the same as C, which is excellent. The best part of it all, is that it is actually fun to code in Go compared to C. Python was always an attraction for me as the language is a breeze to work with and enjoyable programming with it. Go is also a nice language to work with and it's really fast to boot. So I'm very excited about the language.
