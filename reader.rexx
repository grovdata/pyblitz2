/* REXX */
parse arg listname
if listname='' then listname='test/kw_working.txt'
ascfilename='T:bla.asc'
bbfilename='T:bla.bb2'
contents=''
IF Open(listhandle, listname,'READ') THEN DO UNTIL EOF(listhandle)
   line = ReadLn(listhandle)
   SAY line
   if open(aschandle,ascfilename,'WRITE') then DO
   		call writeln(aschandle,line)
   		call close(aschandle)
		address TED_REXX1 LOAD ascfilename
		if rc~=0 then say "Load failed"
		address TED_REXX1 'SAVE "bbfilename"'
		if rc=0 then DO
			if open(aschandle,ascfilename,'READ') then token=readln(aschandle)
			say line '=' c2x(token)
			call close(aschandle)
		end
   END

END
ELSE EXIT 20
CALL Close(listhandle)
EXIT 0