# cython: language_level=3
# Cython TRNG. Coded by Wojciech Lawren.
from rdrand cimport *

cdef class TRNGError(Exception): pass

# TRNG -> RDRAND | RDSEED
cpdef uint64_t rand64() except? 0:
  cdef uint64_t r = _rand64()
  if r: return r
  raise TRNGError()

cpdef uint32_t rand32() except? 0:
  cdef uint32_t r = _rand32()
  if r: return r
  raise TRNGError()

cpdef uint16_t rand16() except? 0:
  cdef uint16_t r = _rand16()
  if r: return r
  raise TRNGError()

cpdef uint64_t seed64() except? 0:
  cdef uint64_t r = _seed64()
  if r: return r
  raise TRNGError()

cpdef uint32_t seed32() except? 0:
  cdef uint32_t r = _seed32()
  if r: return r
  raise TRNGError()

cpdef uint16_t seed16() except? 0:
  cdef uint16_t r = _seed16()
  if r: return r
  raise TRNGError()

cpdef bytes rand_bytes(uint16_t n = 32):
  cdef uint16_t q = n // 8
  if n%8: q += 1
  cdef bytes rb = bytes(q*8)
  cdef uint64_t *_rb = <uint64_t*><uint8_t*>rb
  for i in range(q): _rb[i] = rand64()
  return rb[:n]
