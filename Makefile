# Makefile

SHELL := /usr/bin/env bash
GENERATED_DIR := vegaapiclient/generated

.PHONY: default
default:
	@echo "Please select a target:"
	@echo "- preproto:    Copy *.proto from protos repository."
	@echo "- proto:       Run buf to auto-generate API client."

.PHONY: black
black:
	@black .

.PHONY: blackcheck
blackcheck:
	@black --check .

.PHONY: buf-build
buf-build:
	@buf build

.PHONY: buf-generate
buf-generate: buf-build
	@if ! command -v grpc_python_plugin 1>/dev/null ; then \
		echo "Not found/executable: grpc_python_plugin" ; \
		echo "See https://github.com/grpc/grpc/blob/master/BUILDING.md#building-with-cmake" ; \
		exit 1 ; \
	fi
	@rm -rf $(GENERATED_DIR)
	@mkdir -p $(GENERATED_DIR)
	@buf generate

.PHONY: check_dist
check_dist:
	@bash check_dist.sh

.PHONY: clean
clean:
	@rm -rf "$(GENERATED_DIR)" build

.PHONY: coverage
coverage:
	@if test -z "$$CORE_GRPC_NODE" ; then echo "Please set CORE_GRPC_NODE (e.g. node.xx.vega.zzz:1111)." ; exit 1 ; fi
	@if test -z "$$DATA_GRPC_NODE" ; then echo "Please set DATA_GRPC_NODE (e.g. node.xx.vega.zzz:1111)." ; exit 1 ; fi
	@if test -z "$$WALLETSERVER" ; then echo "Please set WALLETSERVER (e.g. https://wallet.xx.vega.zzz)." ; exit 1 ; fi
	@rm -rf .coverage.d
	@pipenv --bare install # 1>/dev/null 2>&1
	@pipenv run pip install -e .
	@find . -name __pycache__ | xargs -r rm -rf
	@find . -name  '*.pyc' -o -name '*.so' | xargs -r rm -rf
	@pipenv run pytest --cov-config=.coveragerc --cov=vegaapiclient --cov-report=term --cov-report=html:.coverage.d tests/

.PHONY: dist
dist:
	@if test -z "$$TWINE_USERNAME" -o -z "$$TWINE_PASSWORD" ; then \
		echo "Please set TWINE_USERNAME and TWINE_PASSWORD." ; \
		exit 1 ; \
	fi
	@rm -rf build dist && mkdir build dist
	@python3 setup.py sdist bdist_wheel
	@twine upload dist/*

.PHONY: dist_test
dist_test:
	@if test -z "$$TWINE_USERNAME" -o -z "$$TWINE_PASSWORD" ; then \
		echo "Please set TWINE_USERNAME and TWINE_PASSWORD." ; \
		exit 1 ; \
	fi
	@rm -rf build dist && mkdir build dist
	@python3 setup.py sdist bdist_wheel
	@twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: flake8
flake8:
	@flake8

.PHONY: preproto
preproto:
	@if test -z "$(VEGAPROTOS)" ; then echo "Please set VEGAPROTOS" ; exit 1 ; fi
	@rm -rf sources && cp -a $(VEGAPROTOS)/sources ./
	@rm -rf third_party && cp -a $(VEGAPROTOS)/third_party ./
	@(cd "$(VEGAPROTOS)" && git describe --tags) >sources/from.txt

.PHONY: proto
proto: buf-generate
	@env GENERATED_DIR="$(GENERATED_DIR)" ./post-generate.sh

.PHONY: pylint
pylint:
	@pipenv --bare install
	@pipenv run pip install -e .
	@pipenv run pylint --ignore=generated vegaapiclient

.PHONY: spellcheck
spellcheck:
	@venv="/tmp/venv-$$USER-vega-api-pyspelling" && \
	if ! test -d "$$venv" ; then \
		virtualenv "$$venv" || exit 1 ; \
	fi && \
	source "$$venv/bin/activate" && \
	pip install -q --upgrade pyspelling && \
	pyspelling -c spellcheck.yaml && \
	deactivate

.PHONY: test
test:
	@if test -z "$$CORE_GRPC_NODE" ; then echo "Please set CORE_GRPC_NODE (e.g. node.xx.vega.zzz:1111)." ; exit 1 ; fi
	@if test -z "$$DATA_GRPC_NODE" ; then echo "Please set DATA_GRPC_NODE (e.g. node.xx.vega.zzz:1111)." ; exit 1 ; fi
	@if test -z "$$WALLETSERVER" ; then echo "Please set WALLETSERVER (e.g. https://wallet.xx.vega.zzz)." ; exit 1 ; fi
	@pipenv --bare install # 1>/dev/null 2>&1
	@pipenv run pip install -e .
	@env PYTHONPATH=. pipenv run pytest tests/

# .PHONY: mypy
# mypy:
# 	@venv="/tmp/venv-$$USER-vega-api-mypy" && \
# 	if ! test -d "$$venv" ; then \
# 		virtualenv "$$venv" || exit 1 ; \
# 	fi && \
# 	source "$$venv/bin/activate" && \
# 	pip install -r mypy-requirements.txt && \
# 	echo "Running mypy in grpc/clients/python" && \
# 	pushd grpc/clients/python 1>/dev/null && \
# 	env MYPYPATH=. mypy --ignore-missing-imports . | grep -vE '(^Found|/generated/|: note: )' ; \
# 	code="$$?" ; test "$$code" -ne 0 && \
# 	popd 1>/dev/null && \
# 	for d in graphql/examples/python grpc/examples/python rest/examples/python ; do \
# 		echo "Running mypy in $$d" && \
# 		pushd "$$d" 1>/dev/null && \
# 		env MYPYPATH=. mypy --ignore-missing-imports . && \
# 		popd 1>/dev/null || exit 1 ; \
# 	done && \
# 	deactivate
