## Lab 0

* Find your group
* everyone:
    - generate SSH keys and add to Gitlab
* One team member (Owner)
    - creates project on Gitlab
        - uncheck "Initialize repository with a README"
    - initialize repo with directory structure below
        - follow the instructions under "Push an existing folder"
        - the existing_folder is project_root (below)
    - adds prof and TA (Maintainers)
    - adds team members (Developers)  
* everyone 
    - clone the group project
    - make some changes, stage, commit, push
    - trigger and resolve merge conflicts

## Repo structure

* project_root/
    * docs/
    * src/
        - user_service/
        - user_api/
        - <APP_NAME>/
        - requirements.txt
    * tests/
        - test_user_service/
        - test_user_api/
        - test_<APP_NAME>/
        - text_example.py
    * pyproject.toml

## Notes

* If possible, the project owner should be the person who is most familiar with Git.
* You can come up with your APP_NAME later, you don't need to create all of these directories now.
* requirements.txt and pyproject.toml are provided
* "tests" and all of its subdirectories should contain empty __init__.py files.