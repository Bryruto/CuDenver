# MASM + Irvine32
SRC ?= pa5/pa5.asm

DIR  := $(dir $(SRC))
NAME := $(basename $(notdir $(SRC)))
EXE  := $(basename $(SRC)).exe

# Detect Windows or Linux
ifeq ($(OS),Windows_NT)
    MASM_BIN ?= C:\Program Files\Microsoft Visual Studio\18\Community\VC\Tools\MSVC\14.52.36726\bin\Hostx64\x86
    ASM  := $(subst /,\,$(MASM_BIN)/ml.exe)
    LINK := $(subst /,\,$(MASM_BIN)/link.exe)
    LIB  := $(subst /,\,$(CURDIR)/lib)
    CD   := cd /d "$(subst /,\,$(patsubst %/,%,$(DIR)))"
    RUN  := "$(NAME).exe"
else
    MASM_BIN ?= $(HOME)/.wine/drive_c/masm32/bin
    ASM  := $(MASM_BIN)/ml.exe
    LINK := $(MASM_BIN)/link.exe
    LIB  := $(shell winepath -w "$(CURDIR)/lib")
    CD   := cd "$(DIR)"
    WINE := wine
    RUN  := wine "./$(NAME).exe"
endif

.PHONY: all run debug clean

all:
	$(CD) && $(WINE) "$(ASM)" /c /coff /Zi "/I$(LIB)" "$(NAME).asm"
	$(CD) && $(WINE) "$(LINK)" /SUBSYSTEM:CONSOLE /ENTRY:main "/LIBPATH:$(LIB)" "/OUT:$(NAME).exe" "$(NAME).obj" Irvine32.lib kernel32.lib user32.lib

run: all
	$(CD) && $(RUN)

debug: all
ifeq ($(OS),Windows_NT)
	@echo Windows debugger not configured.
else
	@winedbg --gdb --no-start --port 2345 "$(EXE)" > .winedbg.log 2>&1 & \
	pid=$$!; \
	trap 'kill $$pid 2>/dev/null || true' EXIT; \
	sleep 3; \
	nvim "$(SRC)" "+lua vim.schedule(function() require('dap').continue() end)"
endif

clean:
ifeq ($(OS),Windows_NT)
	-$(CD) && del /Q "$(NAME).obj" "$(NAME).exe"
else
	rm -f "$(DIR)$(NAME).obj" "$(EXE)"
endif
