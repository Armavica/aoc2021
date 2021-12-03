.PHONY: today

TODAY := $(shell date +%d)

today:
	python -m $(TODAY) $(TODAY)/input
