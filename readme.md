# Adding a remote

You can add a second remote for backup purposes.
Test both.

## Getting started

* Add your SSH keys to GitHub
* Create a repository (you can keep all the defaults)

## Instructions

Replace the URLs below with your GitLab and GitHub urls, respectively.

add remote:

```git remote add backup https://github.com/dabenedetto-unh/cs-518-labs.git```

push to remote:

```git push backup```

set so that a push will automatically go to both:

```git remote set-url --add --push origin https://github.com/dabenedetto-unh/cs-518-labs.git```

## Etc.

list remotes:

```git remote -v```

if the only push url for origin is your github url, you'll have to add the gitlab url back:

```git remote set-url --add --push origin git@gitlab.cs.unh.edu:cs518-public/spring-2026/labs-ai-first.git```