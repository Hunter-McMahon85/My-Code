#
# CIS330: Lab 3
#
# Makefile to build libraries and test applications.
#

CC=gcc
AR=ar

CFLAGS=-g -fPIC -O2 -I./include -L./lib
LIBS=-llab4 -lm

all: lab4 lab4_dyn 


obj:
	mkdir -p obj

lib:
	mkdir -p lib

obj/stats.o: src/stats.c include/stats.h obj
	$(CC) $(CFLAGS) -c -o $@ $<

obj/ohno.o: src/ohno.c include/ohno.h obj
	$(CC) $(CFLAGS) -c -o $@ $<

lib/liblab4.a: obj/stats.o obj/ohno.o lib
	$(AR) rc lib/liblab4.a obj/stats.o obj/ohno.o

lab4: src/lab4.c lib/liblab4.a
	$(CC) $(CFLAGS) -o $@ $< $(LIBS)

lib/liblab4.so: obj/stats.o obj/ohno.o
	$(cc) -shared -o $@ $^

lab4_dyn: src/lab4.c lib/liblab4.so
	export LD_LIBRARY_PATH=./lib:LD_LIBRARY_PATH
	$(CC) $(CFLAGS) -o $@ $^ -lm

clean:
	rm lab4 lib/liblab4.a lib/liblab4.so lab4_dyn obj/ohno.o obj/stats.o
	rmdir obj
	rmdir lib

