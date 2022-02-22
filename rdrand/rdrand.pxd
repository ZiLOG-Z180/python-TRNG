# cython: language_level=3
from libc.stdint cimport *

cdef extern from "rdrand.h" nogil:
  uint64_t _rand64()

  uint32_t _rand32()

  uint16_t _rand16()

  uint64_t _seed64()

  uint32_t _seed32()

  uint16_t _seed16()
