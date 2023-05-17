#pragma once

#ifdef __unix__

#include <stdlib.h>
#include <stdio.h>

#elif defined(_WIN32) || defined(WIN32)

#include <windows.h>
#include <stdio.h>

#endif

void libCall();
