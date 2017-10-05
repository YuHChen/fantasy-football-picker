TEST_DIRS = \
	test.data.fetch

.PHONY: all run tests

all:	tests run

run:
	@echo -n "[run]: "
	python3 main.py --log=debug

tests:
	@echo -n "[tests]: "
	$(foreach dir, $(TEST_DIRS), python3 -m unittest discover $(dir))
