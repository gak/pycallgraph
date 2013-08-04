tests:
	py.test --cov coveralls --cov-report term-missing --cov=pycallgraph \
		--cov-config test/.coveragerc --pep8 \
		--ignore=pycallgraph/memory_profiler.py \
		test pycallgraph

doc:
	make -C docs html
	docs/update_readme.py
