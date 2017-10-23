TEST_DIR = test

.PHONY: all run unittests

all:	unittests run

run:
	@echo -n "[run]: "
	python3 main.py --log=debug
	@echo ""

unittests:
	@echo -n "[unittest]: "
	python3 -m unittest discover $(TEST_DIR)
	@echo ""
