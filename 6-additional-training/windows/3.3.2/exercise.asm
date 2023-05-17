_text SEGMENT

;; This allows us to call the BlackBox function.
EXTERN BlackBox: PROC

;; int SumFiveArgs(int a, int b, int c, int d, int e);
;; Return the sum of the 5 arguments.
SumFiveArgs PROC
	;; TODO: Implement this function.




SumFiveArgs ENDP

;; This will determine how many bytes you used, just for your information. Smaller is better!
SumFiveArgsSize dd $-SumFiveArgs

;; int Func2(int a, int b, int c, int d);
;; Return the value a + b + BlackBox(c, d).
Func2 PROC
	;; TODO: Implement this function.
	;; The main catch here is that you are required to allocate "shadow space"
	;; for the BlackBox function. Look it up in the MSDN.
	;; You also need to make sure the stack ends up properly aligned.




Func2 ENDP

Func2Size dd $-Func2

END ; _text segment