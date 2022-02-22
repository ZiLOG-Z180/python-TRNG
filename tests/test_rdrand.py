#!/usr/bin/env python
import _rdrand as rd

RDS = 1
ITR = 100


def test_rand_bytes():
    for _ in range(ITR):
        n = rd.seed16()
        rb = rd.rand_bytes(n)
        assert rb
        assert type(rb) == bytes
        assert len(rb) == n


def test_rand_bytes0():
    rb = rd.rand_bytes(0)
    assert not rb
    assert type(rb) == bytes
    assert len(rb) == 0


def test_fail_rand_bytes():
    err = 0
    assert not err
    try:
        x = rd.rand_bytes(2**16)
    except OverflowError:
        err = 1
    assert err


def test_rand64():
    for _ in range(ITR):
        r = rd.rand64()
        assert type(r) == int
        assert 0 < r < 2**64


def test_rand32():
    for _ in range(ITR):
        r = rd.rand32()
        assert type(r) == int
        assert 0 < r < 2**32


def test_rand16():
    for _ in range(ITR):
        r = rd.rand16()
        assert type(r) == int
        assert 0 < r < 2**16


def test_seed64():
    for _ in range(ITR):
        r = rd.seed64()
        assert type(r) == int
        assert 0 < r < 2**64


def test_seed32():
    for _ in range(ITR):
        r = rd.seed32()
        assert type(r) == int
        assert 0 < r < 2**32


def test_seed16():
    for _ in range(ITR):
        r = rd.seed16()
        assert type(r) == int
        assert 0 < r < 2**16


def test_rand16b(benchmark):
    benchmark.pedantic(rd.rand16, args=(), rounds=RDS, iterations=ITR)


def test_rand32b(benchmark):
    benchmark.pedantic(rd.rand32, args=(), rounds=RDS, iterations=ITR)


def test_rand64b(benchmark):
    benchmark.pedantic(rd.rand64, args=(), rounds=RDS, iterations=ITR)


def test_seed16b(benchmark):
    benchmark.pedantic(rd.seed16, args=(), rounds=RDS, iterations=ITR)


def test_seed32b(benchmark):
    benchmark.pedantic(rd.seed32, args=(), rounds=RDS, iterations=ITR)


def test_seed64b(benchmark):
    benchmark.pedantic(rd.seed64, args=(), rounds=RDS, iterations=ITR)


def test_rand_bytes8b(benchmark):
    benchmark.pedantic(rd.rand_bytes, args=(8,), rounds=RDS, iterations=ITR)


def test_rand_bytes16b(benchmark):
    benchmark.pedantic(rd.rand_bytes, args=(16,), rounds=RDS, iterations=ITR)
