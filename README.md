# andykee.com
andykee.com is a static site generated by [Pelican](https://github.com/getpelican/pelican).

## Installation
1. Clone this repo (preferably into a virtualenv)

2. `pip install -r requirements.txt`

That's it!

## Write content
* Articles go in `content`, images go in `content/img`, and other files go in `content/files`. 
* Images and files are included in an article with `![Tooltip]({filename}/img/image.jpg)`
* `blank.md` is a blank article template. It provides placeholders for commonly used article metadata.
* Articles can be saved as drafts by adding `Status: draft` to the metadata. These drafts are available at `localhost:8000/drafts` when running the development server. They are not otherwise published.
* Syntax highlighting is supported by including the three semicolons and  language identifier immediately above a block of code. I'm sure there are a ton of language identifiers. I use `bash`, `python`, `matlab`, and `tex`.
* LaTeX support is provided by MathJax. Wrap inline equations with `$` and full-line equations with `$$`.
* Slick gallery support coming soon

## Publish
Publish to AWS S3 bucket defined in `Makefile` by running:

    make s3_upload

Note that the AWS CLI needs to be configured before this will work. This is easily done by running `aws configure` after installing all requirements. 

See more [here](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

A development server can be run by

    make devserver

Stop the development server with

    ./develop_server.sh stop

