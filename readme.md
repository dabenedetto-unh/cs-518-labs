# Adding a remote

You can add a second remote for backup purposes.

## Getting started

* Add your SSH keys to GitHub
* Create a repository (you can keep all the defaults)

## Instructions

add remote:

```git remote add backup https://github.com/dabenedetto-unh/cs-518-labs.git```

push to remote:

```git push backup```

set so that a push will automatically go to both:

```git remote set-url --add --push origin https://github.com/dabenedetto-unh/cs-518-labs.git```

## Etc.

list remotes:

```git remote -v```