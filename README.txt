Problem:

You have two players, Bob and Alice, that take turns in rolling a fair k-sided die. Whoever rolls a
k first wins the game. The Python program should output the probability that Bob wins the 
game for k = 6 thru 99. That is, the output will be an array of probabili8es where index 0 is the 
probability when k = 6; index 1 when k = 7; etc.

---

Tested with Python 3.10.12 on Mint/Ubuntu jammy.

For your convenience, a Makefile is provided that sets up a venv, pip installs libs, and
will run various available functions:

To setup the venv, run the script, and run tests:
> make

To only run the script:
> make run
To only run tests:
> make run_tests

To run the Flask REST api server:
> make run_api
And the api tests (server doesn't need to be running):
> make run_api_tests

When task run_api is active, access running endpoint via: curl http://localhost:5000/getProbability
or passing k eg: curl -H "k: 6" http://localhost:5000/getProbability

---

A little extra fun because who doesn't like stats and data vis (especially in this job market!):
> make run_extras


