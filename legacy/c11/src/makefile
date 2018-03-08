# Makefile for all CLRS ANSI-C code.

IDIR =../include
CC=gcc
CFLAGS=-I$(IDIR) -std=c11

ODIR=obj
LDIR =../lib

LIBS=-lm

# List all header files here:
_DEPS = search.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

# List all search object files here:
_SEARCH_OBJ = searchmain.o search.o
SEARCH_OBJ = $(patsubst %,$(ODIR)/%,$(_SEARCH_OBJ))

# List all sort object files here:
_SORT_OBJ = sortmain.o sort.o
SORT_OBJ = $(patsubst %,$(ODIR)/%,$(_SORT_OBJ))

$(ODIR)/%.o: %.c $(DEPS)
		$(CC) -c -o $@ $< $(CFLAGS)


all: search.out sort.out

search.out: $(SEARCH_OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

sort.out: $(SORT_OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)


.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(IDIR)/*~ 
