#!/bin/sh
EXEC="exec "

if test x"$1" = x--debug; then
    DEBUG=--debug
    shift
fi

if test x"$1" = x--gdb; then
   shift
   EXEC="gdb --eval-command=run --args "
fi

if test x"$1" = x--valgrind; then
  shift
  EXEC="valgrind $VALGRIND_OPTIONS"   
fi

$EXEC /usr/bin/mono $DEBUG $MONO_OPTIONS /usr/lib/mono/fsharp/%EXENAME% --exename:$(basename "$0") "$@"
