ifeq ($(VERBOSE),1)
LATEX_OPTS=
else
LATEX_OPTS=-interaction=batchmode
endif

LATEX=xelatex $(LATEX_OPTS)
PYTHON=python

print.pdf: print.tex pages.tex
	$(LATEX) $<

# The shell stuff here is a hack to determine the number of pages in badges.pdf
pages.tex: print.py badges.pdf
	$(PYTHON) $< $(shell cat badges.log | sed -n '/^Output written on badges/p' | sed 's/Output written on badges.pdf (\([0-9]\+\) pages)./\1/' ) > $@

# Make the badges. One page per badge
badges.pdf : badges.tex
	$(LATEX) $<

.PHONY: clean
clean:
	rm -f *.aux *.pdf *.log pages.tex
