TEST_DIRS = \
	test.config \
	test.data.fetch

.PHONY: all run tests

all:	tests run

run:
	@echo -n "[run]: "
	python3 main.py --log=debug
	@echo ""

tests:
	@echo -n "[tests]: "
	$(foreach dir, $(TEST_DIRS), python3 -m unittest discover $(dir);)
	@echo ""
