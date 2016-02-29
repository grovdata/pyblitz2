filename='test/kw_working.txt'
contents=''
IF Open(filehandle, filename,'READ') THEN DO UNTIL EOF(filehandle)
   line = ReadLn(filehandle)
   SAY line
   contents = contents || line || '0a'x
   ADDRESS TED_REXX1; SHOWSCREEN
   ADDRESS TED_REXX1; ACTIVATE
   ADDRESS TED_REXX1; LOAD contents
   ADDRESS TED_REXX1; SAVE 'test/kw/' contents '.bb2'
   END
ELSE EXIT 20
CALL Close(filehandle)
EXIT 0
