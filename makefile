.PHONY: input today

TOKEN := $(shell cat token)

TODAY := $(shell TZ='America/New_York' date +%d)
TODAY_NO_0 := $(shell TZ='America/New_York' date +%-d)
YEAR := $(shell TZ='America/New_York' date +%Y)

today: $(TODAY)/input
	python -m $(TODAY) $(TODAY)/input

input: $(TODAY)/input
	head $(TODAY)/input

$(TODAY)/input: token
	curl --silent --cookie session=$(TOKEN) https://adventofcode.com/$(YEAR)/day/$(TODAY_NO_0)/input -o $(TODAY)/input
