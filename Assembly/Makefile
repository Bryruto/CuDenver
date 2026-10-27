# MASM + Irvine32
SRC ?= hw4/PA4.asm

DIR  := $(dir $(SRC))
NAME := $(basename $(notdir $(SRC)))

ASM  := $(HOME)/.wine/drive_c/masm32/bin/ml.exe
LINK := $(HOME)/.wine/drive_c/masm32/bin/link.exe
LIB  := $(shell winepath -w "$(CURDIR)/lib")

.PHONY: all run debug clean

all:
	cd "$(DIR)" && wine "$(ASM)" /c /coff /Zi "/I$(LIB)" "$(NAME).asm"
	cd "$(DIR)" && wine "$(LINK)" /SUBSYSTEM:CONSOLE /ENTRY:main "/LIBPATH:$(LIB)" /OUT:"$(NAME).exe" "$(NAME).obj" Irvine32.lib kernel32.lib user32.lib

run: all
	wine "./$(DIR)$(NAME).exe"

debug: all
	@winedbg --gdb --no-start --port 2345 "./$(DIR)$(NAME).exe" > .winedbg.log 2>&1 & \
	pid=$$!; \
	trap 'kill $$pid 2>/dev/null || true' EXIT; \
	sleep 3; \
	nvim "$(SRC)" "+lua vim.schedule(function() require('dap').continue() end)"

clean:
	rm -f "$(DIR)$(NAME).obj" "$(DIR)$(NAME).exe"
