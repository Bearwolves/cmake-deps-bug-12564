#pragma once

#ifdef _WIN32
  #define hellolib_EXPORT __declspec(dllexport)
#else
  #define hellolib_EXPORT
#endif

hellolib_EXPORT void hellolib2();
