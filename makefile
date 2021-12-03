.PHONY: today

TODAY := $(shell TZ='America/New_York' date +%d)

today:
	python -m $(TODAY) $(TODAY)/input
