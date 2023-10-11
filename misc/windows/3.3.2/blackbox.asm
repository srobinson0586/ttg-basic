_text SEGMENT

BlackBox PROC
	;; Make sure rsp ends with an '8'.
	or rsp, 8
	;; Smash all the shadow space we're allowed to.
	mov DWORD PTR 08h[rsp], 0DEADBEEFh
	mov DWORD PTR 0ch[rsp], 0DEADBEEFh
	mov DWORD PTR 10h[rsp], 0DEADBEEFh
	mov DWORD PTR 14h[rsp], 0DEADBEEFh
	mov DWORD PTR 18h[rsp], 0DEADBEEFh
	mov DWORD PTR 1ch[rsp], 0DEADBEEFh
	mov DWORD PTR 20h[rsp], 0DEADBEEFh
	mov DWORD PTR 24h[rsp], 0DEADBEEFh
	;; Perform the actual operations.
	mov eax, ecx
	add eax, edx
	sub ecx, edx
	xor eax, ecx
	ret
BlackBox ENDP

END