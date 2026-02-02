# Adding a Remote

You can add a second remote for backup purposes.
Testing that it works with VSCode.

## Instructions

add remote:

```git remote add backup https://github.com/dabenedetto-unh/cs-518-labs.git```

push to remote:

```git push backup```

set so that a push will automatically go to both:

```git remote set-url --add --push origin https://github.com/dabenedetto-unh/cs-518-labs.git```

## etc.

list remotes:

```git remote -v```