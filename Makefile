#!/usr/bin/env make
all: tests

tests:
	python3 -m venv .venv && \
	.venv/bin/pip3 install pylint requests && \
	.venv/bin/pylint --disable too-many-positional-arguments,line-too-long,too-many-branches,missing-function-docstring,consider-using-with,too-many-arguments --fail-under 9.7 distrib-dl && \
	./distrib-dl -c all
