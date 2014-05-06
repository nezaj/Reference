## Think Complexity
From the author's own words
> This book is about data structures and algorithms, intermediate programming in Python, computational modeling and the philosophy of science:

This repo contains my notes for the book and solutions to the exercises. See below on setting up a Python environment if you'd like to experiment with the exercises yourself.

* [Getting Started](#getting-started)
* [Chapters](#exercises)

### Getting Started
If you don't already have [pip][pip-docs], [virtualenv][venv-docs] and [virtualenvwrapper][venv-wrapper-docs], check out their documentation and install them.
```
sudo easy_install pip
sudo pip install virtualenv
sudo pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
```

Once you have cloned this repo and installed the packages above, use the Makefile to create a virtualenv to hold this project's dependencies. By default then virtualenv will be located in `~/.virtualenvs/think-complexity`. Activate the environment once setup is complete.
```
make virtualenv
workon think-complexity
```

If you ever need to upgrade or install packages which appeared since your last run, just run `make virtualenv` again.

You should be good to go!

### Chapters
* Graphs -- ([Code][Graphs-code]) ([Tests][Graphs-tests]) ([Notes][Graphs-notes])
* Analysis -- ([Code][Analysis-code]) ([Tests][Analysis-tests]) ([Notes][Analysis-notes])

[pip-docs]: http://pip.readthedocs.org/
[venv-docs]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
[venv-wrapper-docs]: http://virtualenvwrapper.readthedocs.org/en/latest/

[Graphs-code]: https://github.com/nezaj/Reference/tree/master/think_complexity/src/graphs
[Analysis-code]: https://github.com/nezaj/Reference/tree/master/think_complexity/src/analysis

[Graphs-tests]: https://github.com/nezaj/Reference/tree/master/think_complexity/src/tests/graphs
[Analysis-tests]: https://github.com/nezaj/Reference/tree/master/think_complexity/src/tests/analysis

[Graphs-notes]: https://github.com/nezaj/Reference/blob/master/think_complexity/notes/graphs_notes.md
[Analysis-notes]: https://github.com/nezaj/Reference/blob/master/think_complexity/notes/analysis_notes.md
