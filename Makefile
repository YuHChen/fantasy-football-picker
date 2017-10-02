TEST_DIRS = \
	test.data.fetch

.PHONY: all tests

all:	tests

tests:
	$(foreach dir, $(TEST_DIRS), python3 -m unittest discover $(dir))
