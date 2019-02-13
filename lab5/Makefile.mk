all: static_block dynamic_block

dynamic_block: program.o shared_lib.so
	cc program.o shared_lib.so -o dynamic -Wl,-rpath='$$ORIGIN'

static_block: program.c block.o
	cc program.c block.o -o static_block

shared_lib.so: block.o
	cc -shared -o shared_lib.so block.o

program.o: program.c
	cc -fPIC -c program.c -o program.o
	
block.o: source/block.c
	cc -fPIC -c source/block.c -o block.o