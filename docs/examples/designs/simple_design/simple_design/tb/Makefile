#!/bin/bash 
# Makefile 
SIM ?= icarus 
TOPLEVEL_LANG ?= verilog 
VERILOG_SOURCES += /home/daquintero/phd/piel/docs/examples/designs/simple_design/simple_design/src/adder.sv 
VERILOG_SOURCES += /home/daquintero/phd/piel/docs/examples/designs/simple_design/simple_design/src/adder.vhdl 
TOPLEVEL := adder 
MODULE := test_adder 
include $(shell cocotb-config --makefiles)/Makefile.sim