.PHONY: clean data

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python
CONFIG_FILE=configs.ini
CONFIG_KEY_NAME=required_python

#################################################################################
# BLOCK TO TEST PYTHON INSTALLATION                                             #
#################################################################################

# Test if python is installed

ifeq (,$(shell python3 --version))
$(error "Python is not installed!")
endif


#################################################################################
# COMMANDS                                                                      #
#################################################################################

install:
	$(PYTHON_INTERPRETER) -m pip install -e .

# Verify Python Version
check_installed_python:
	$(eval INSTALLED := $(shell $(PYTHON_INTERPRETER) --version | tr -cd '[[:digit:][:punct:]]'))
	$(eval REQUIRED := $(shell [ -f $(CONFIG_FILE) ] && cat $(CONFIG_FILE) | grep -w $(CONFIG_KEY_NAME) | cut -f2 -d "="))

	@if [ -z "$(REQUIRED)" ] | [ $(shell echo -n "$(REQUIRED)" | wc -c ) -lt 3 ]; then \
		echo "Missing configurarion file or key"; \
		return 1; \
	fi

	@if { echo "$(REQUIRED)" ; echo "$(INSTALLED)"; } | sort --version-sort --check=quiet; then \
		echo "Python interpreter is up to date: required Python '$(REQUIRED)' found Python '$(INSTALLED)'"; \
	else \
		echo "Python version error: required Python '$(REQUIRED)' found Python '$(INSTALLED)'" ; \
		exit 1; \
	fi

# Install pip-compile

install-pip-tools: check_installed_python
	$(PYTHON_INTERPRETER) -m pip install pip-tools

# Compile Python Dependencies files

pip-compile: install-pip-tools
	pip-compile --no-emit-index-url requirements.in
	pip-compile --no-emit-index-url requirements-dev.in

pip-downgrade:
	$(PYTHON_INTERPRETER) -m pip install pip==21.3.1

## Install Python Dependencies & Install pre-commit hooks
requirements: pip-downgrade pip-compile check_installed_python
	$(PYTHON_INTERPRETER) -m pip install -r requirements-dev.txt --use-deprecated=legacy-resolver &&\
	pre-commit install
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt --use-deprecated=legacy-resolver

## Synchronize the Python Dependencies & Virtual Env
sync-env: pip-compile
	pip-sync requirements.txt requirements-dev.txt

#################################################################################

## Download Dataset
get_data: requirements
	$(PYTHON_INTERPRETER) download_dataset.py

## Make Dataset
data: get_data
	$(PYTHON_INTERPRETER) src/data/make_dataset.py data/raw data/processed

#################################################################################

## Delete all compiled Python files
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".tox" -exec rm -rf "{}" \;
	@find . -type d -name ".pytest_cache" -exec rm -rf "{}" \;

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################



#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
