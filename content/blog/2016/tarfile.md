Title: TarFile Tip
Date: 2016-11-30
Tags: python3.5 tarfile
Slug: tarfile-tip
Author: Greg Reinbach

Working with tar files and attempting to create a py.test fixture of a tar file and I ran into an issue.

I'm using [TarFile](https://docs.python.org/3.5/library/tarfile.html) package on python 3.5

My initial fixture was setup as;

    @pytest.fixture
    def file_tar(tmpdir, tmpdir_factory):
        fn = tmpdir_factory.mktemp("tar").join("test.tar")
        tf = tarfile.TarFile(str(fn), "w")
        p1 = tmpdir.mkdir("src1").join("test1.txt")
        p1.write("text 1 content")
        tf.add(p1)
        p2 = tmpdir.mkdir("src2").join("test2.txt")
        p2.write("text 2 content")
        tf.add(str(p2))
        tf.close()
        return fn

But I ended up with an empty file in the tar'd file fixture, and that was causing issues when attempting to extract the contents of the tar'd file. As it is an empty file and results in the following error/exception `tarfile.ReadError: empty file`

Changing the fixture to the following, resolved the issue;

    @pytest.fixture
    def file_tar(tmpdir, tmpdir_factory):
        fn = tmpdir_factory.mktemp("tar").join("test.tar")
        p1 = tmpdir.mkdir("src1").join("test1.txt")
        p1.write("text 1 content")
        p2 = tmpdir.mkdir("src2").join("test2.txt")
        p2.write("text 2 content")
        with tarfile.open(str(fn), "w") as tf:
            tf.add(p1)
            tf.add(str(p2))
        return fn

I guess that is more pythonic as well.
