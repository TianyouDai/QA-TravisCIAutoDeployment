# QA-TravisCIAutoDeployment

This project demonstrates how to use python and Travis CI to verify a the correct answer to a programing challenge and auto-deploy a generated index file to Github pages when tests pass successfully.

When a commit is pushed to master, TravisCI spins up a build machine and runs the command pytest. Pytest discovers tests (methods that begin with `test_`) and when all the tests pass successfully the `index.html` is deployed by TravisCI to gh-pages.

# On a Successful Test

A successful test will cause [this site](https://TianyouDai.github.io/QA-TravisCIAutoDeployment) to update with a new token matching the one on the gh-pages branch.
