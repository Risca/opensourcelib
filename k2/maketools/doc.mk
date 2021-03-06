DOCS :=

.PHONY: doc html pdf
doc:
html:
pdf:

# 1 - directory in doc
define MACRO_DOC_TARGETS
DOCS += doc/build/$(1)/html/index.html doc/build/$(1)/pdf/$(1).pdf

$(eval __$(1)_docs := $(shell find doc/$(1) -type f))
html: $(1)_html
pdf: $(1)_pdf
$(1): $(1)_html $(1)_pdf
doc: $(1)
$(1)_html: doc/build/$(1)/html/index.html
doc/build/$(1)/html/index.html: SHELL := $(NODE_local_SHELL)
doc/build/$(1)/html/index.html: .SHELLFLAGS := $(NODE_local_SHELLFLAGS)
doc/build/$(1)/html/index.html: ./docker/markers/docker_node_local_venv.marker $(__$(1)_docs) k2/version.py $(PY_SOURCES)
	@sphinx-build -E -a -b html doc/$(1) doc/build/$(1)/html
	@touch doc/build/$(1)/index.html
$(1)_pdf: doc/build/$(1)/pdf/$(1).pdf
doc/build/$(1)/pdf/$(1).pdf: SHELL := $(NODE_local_SHELL)
doc/build/$(1)/pdf/$(1).pdf: .SHELLFLAGS := $(NODE_local_SHELLFLAGS)
doc/build/$(1)/pdf/$(1).pdf: ./docker/markers/docker_node_local_venv.marker $(__$(1)_docs) k2/version.py $(PY_SOURCES)
	@sphinx-build -E -a -b latex doc/$(1) doc/build/$(1)/pdf
	@cd doc/build/$(1)/pdf && make BASH_ENV=BASH_ENV PDFLATEX="pdflatex -interaction=batchmode" all-pdf
ifeq ($(1),user_guide)
endif

endef

$(eval $(call MACRO_DOC_TARGETS,dev_guide))

DOCS += doc/build/user_guide/html/index.html doc/build/user_guide/pdf/user_guide.pdf

html: user_guide_html
pdf: user_guide_pdf
user_guide: user_guide_html user_guide_pdf
doc: user_guide
user_guide_html: doc/build/user_guide/html/index.html
doc/build/user_guide/html/index.html: SHELL := $(NODE_local_SHELL)
doc/build/user_guide/html/index.html: .SHELLFLAGS := $(NODE_local_SHELLFLAGS)
doc/build/user_guide/html/index.html: ./docker/markers/docker_node_local_venv.marker k2/version.py $(PY_SOURCES) $(RST_SOURCES)
	@sphinx-build -E -a -b html doc/build/user_guide/generated doc/build/user_guide/html
	@touch doc/build/user_guide/index.html
user_guide_pdf: doc/build/user_guide/pdf/user_guide.pdf
doc/build/user_guide/pdf/user_guide.pdf: SHELL := $(NODE_local_SHELL)
doc/build/user_guide/pdf/user_guide.pdf: .SHELLFLAGS := $(NODE_local_SHELLFLAGS)
doc/build/user_guide/pdf/user_guide.pdf: ./docker/markers/docker_node_local_venv.marker k2/version.py $(PY_SOURCES) $(RST_SOURCES)
	@sphinx-build -E -a -b latex doc/build/user_guide/generated doc/build/user_guide/pdf
	@cd doc/build/user_guide/pdf && make BASH_ENV=BASH_ENV PDFLATEX="pdflatex -interaction=batchmode" all-pdf
ifeq (user_guide,user_guide)
doc/build/user_guide/html/index.html: doc/build/user_guide/generated/result
doc/build/user_guide/pdf/user_guide.pdf: doc/build/user_guide/generated/result

doc/build/user_guide/generated/result: SHELL := $(NODE_local_SHELL)
doc/build/user_guide/generated/result: .SHELLFLAGS := $(NODE_local_SHELLFLAGS)
doc/build/user_guide/generated/result: ./docker/markers/docker_node_local_venv.marker $(PY_SOURCES) $(RST_SOURCES)
	rm -rf doc/build/user_guide/generated/
	zk2 docgen --doc-dir doc/build/user_guide/generated/

endif

doc/build/dev_guide/html/index.html: | doc/build/user_guide/html/index.html

.PHONY: cleandoc
cleandoc:
	rm -rf doc/build/
