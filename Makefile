TEST_DIRS = \
	test.config \
	test.data.fetch \
	test.data.transform

.PHONY: all run unittests

all:	unittests run

run:
	@echo -n "[run]: "
	python3 main.py --log=debug
	@echo ""

unittests:	$(TEST_DIRS)
	@echo "Unit tests: SUCCESS"

test%:
	@echo -n "[unittest]: "
	python3 -m unittest discover $@
	@echo ""
