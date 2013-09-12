all: deps tests doc

run_examples:
	cd examples/graphviz; ./all.py
	cd examples/gephi; ./all.py

deps:
	pip install -r requirements/development.txt
	pip install -r requirements/documentation.txt

tests:
	py.test \
		--pep8 \
		--ignore=pycallgraph/memory_profiler.py \
		test pycallgraph examples

	coverage run --source test,pycallgraph,scripts -m py.test
	coverage report -m

	flake8 --exclude=__init__.py,memory_profiler.py pycallgraph
	flake8 --ignore=F403 test
	flake8 examples

doc:
	make -C docs html man
	cp docs/_build/man/pycallgraph.1 man/
	docs/update_readme.py

2to3:
	for a in pycallgraph test examples scripts; do 2to3 -wn $$a; done

