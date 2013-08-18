all: deps tests doc

deps:
	pip install -r requirements/development.txt
	pip install -r requirements/documentation.txt

tests:
	py.test \
		--cov coveralls \
		--cov-report term-missing \
		--cov=pycallgraph \
		--cov-config test/.coveragerc \
		--pep8 \
		--ignore=pycallgraph/memory_profiler.py \
		test pycallgraph examples
		flake8 --exclude=__init__.py,memory_profiler.py pycallgraph
		flake8 --ignore=F403 test
		flake8 examples

doc:
	make -C docs html man
	cp docs/_build/man/pycallgraph.1 man/
	docs/update_readme.py

2to3:
	for a in pycallgraph test examples scripts; do 2to3 -wn $$a; done

