
# How to JIT: Building a simple JIT compiler for Python from first principles

## Intro

Speaker: Matt Page, software engineer @ instagram

Bootstrapping types from codebase at runtime "monkey" something library.


## Agenda

1. Intro
2. Overview
3. Runtime
4. Compiler


## Overview

### Motivation

Learning opportunity.

Start seeing opportunities where a JIT could apply

Large constant factor speedups with low effort. 

- PCRE regex library
- 

### What even is a JIT compiler?

> For our purposes: somethiung that translates python code to machine code in run time. 

- JIT = Just In Time


### Our focus: x86 machine code

Runtime: Memory allocator, FFI


### How might we implement a runtime?

World's simplest JIT compiler. Lets JIT a function that computes the meaning of life: 42

- what was our FFI piece? missed that.  TODO
- use `mmap` - allocate executable memory from OS. If for real: worry about limiting amount of memory we allocated and freeing it.
- we need to do instruction encoding, but this isn't our focus. We want to focus on python->assembly
  - use `PeachPy` python library. Originally for hand-tuned highly optimized computational kernels.


### This talk gets pretty deep into the weeds at this point

See presentation video for weeds.


### ctypes pythonapi

- CDLL example - see video/slides.


### Building a CFG from bytecode

- identify basic block boundaries
- build mapping from offset to basic block
- add edges


### There was a bit more, see video
