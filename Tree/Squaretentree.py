#!/bin/python3

import os
import sys
import time


def intervalPower( k_ ):

    return 2 ** (k_ - 1) if k_ != 0 else 1



def getMaxK( list_v_ ):
    res   = 0
    while len(list_v_) > intervalPower( res ):
        kl = intervalPower( res )
        res += 1

    return res - 1


def add(list_v_, add_v_):

    if len(list_v_) < len(add_v_):
        return add(add_v_, list_v_ )

    i = 0
    while i < len(add_v_):

        r = int(add_v_[len(add_v_) - 1 - i]) + int(list_v_[len(list_v_) - 1 - i])
        if r < 10:
            list_v_[len(list_v_) - 1 - i] = str(r)
        else:
            list_v_[len(list_v_) - 1 - i] = str(r % 10)
            ri = len(add_v_) - 2 - i
            if ri >= 0:
                add_v_[ri] = str(int(add_v_[ri]) + r // 10)
            else:
                add_v_.insert(0, str(r // 10))
                if len(add_v_) > len(list_v_):
                    list_v_.insert( 0, '0' )

        i += 1

    return list_v_


def deduct( list_v_, ded_v_ ):
    i = 0

    if len(list_v_) >= 10:
        if list_v_ == (['1'] + ['0'] * (len(list_v_) - 1)):
            list_v_ = ['9'] * (len(list_v_) - 1)
            ded_v_ = deduct( ded_v_, ['1'])
            if ded_v_ == ['0']:
                return list_v_
            else:
                return deduct( list_v_, ded_v_ )

    while i < len(ded_v_):

        r = int(list_v_[len(list_v_) - 1 - i]) - int(ded_v_[len(ded_v_) - 1 - i])
        if r > 0:
            list_v_[len(list_v_) - 1 - i] = str(r)
        elif r == 0:
            list_v_[len(list_v_) - 1 - i] = '0'
        else:
            list_v_[len(list_v_) - 1 - i] = str(10 + r)
            ri = len(ded_v_) - 2 - i
            if ri >= 0:
                ded_v_[ri] = str(int(ded_v_[ri]) + 1)
            else:
                ded_v_.insert(0, str(1))

        i += 1

    if list_v_ == ['0'] * len(list_v_):
        return ['0']

    while len(list_v_):
        if list_v_[0] == '0':
            list_v_.pop(0)
        else:
            return list_v_

    return ['0']


def level_remainder( k_, r_ ):

    sz = intervalPower( k_ + 1 ) - intervalPower( k_ )
    res = ['9'] * sz

    rr = deduct( r_, ['1'] )
    if rr == ['0']:
        return res
    res = deduct( res, r_ )

    if res == ['0'] * len(res):
        return ['0']

    while len(res):
        if res[0] == '0':
            res.pop(0)
        else:
            return res

    return ['0']


def moreThenZero( list_v ):

    if len(list_v) == 1:
        return int(list_v[0]) > 0
    if len(list_v) > 1:
        return True



def goToOnePosition( L ):

    res = L[:]
    remainder = int(res[len(res)-1])
    if remainder == 0:
        return add(res, list(str(1)) )
    elif remainder == 1:
        return res

    return add(res, list(str(11 - remainder)) )


def getDownRem(arr_, dec_power_):

    if len(arr_) <= dec_power_:
        return arr_
    else:
        res = arr_[len(arr_) - dec_power_:]

        if res == ['0'] * len(res):
            return ['0']

        while len(res):
            if res[0] == '0':
                res.pop(0)
            else:
                return res

        return ['0']


def getUpRem( arr, power ):

    if len(arr) <= power:
        return ['0']
    else:
        res = arr[:len(arr)-power]

        if res == ['0'] * len(res):
            return ['0']

        while len(res):
            if res[0] == '0':
                res.pop(0)
            else:
                return res

        return ['0']



def goUp(L, lk, max_k):

    out = []

    L_in_one_position = goToOnePosition( L )
    if L != L_in_one_position:
        first_d = list2int(L[len(L)-1:])
        out.append( ('0', str(11 - list2int(L[len(L)-1:])) if first_d != 0 else '1') )

    k = 1
    up_remainder = getUpRem( L_in_one_position, 1 )

    while k <= max_k:

        down_remainder = getDownRem( up_remainder, intervalPower(k) )

        if moreThenZero( down_remainder ):
            if k != max_k:
                out.append((str(k), ''.join(level_remainder(k, down_remainder))))
                up_remainder = add( ['1'] + ['0'] * intervalPower(k), up_remainder )
            else:
                out.append((str(k), ''.join(deduct(lk, down_remainder)) ))
                break

        power_delta = intervalPower(k+1) - intervalPower(k)
        up_remainder = getUpRem( up_remainder, power_delta )
        k += 1

    if len(out) == 0:
        out.append( (str(max_k), ''.join(lk)) )
    return out


def goDown( R, max_k ):

    out = []

    remainder = getDownRem( R,intervalPower(max_k) )
    if remainder == ['0'] * len(remainder):
        return out
    k = max_k - 1

    r = []
    while k >= 0:

        r = getUpRem( remainder, intervalPower(k) ) if k > 0 else remainder
        if moreThenZero( r ):
            out.append( (str(k), ''.join(r)) )
        remainder = getDownRem( remainder, intervalPower(k) )
        k -= 1

    return out


def list2int( segment_ ):

    return int( "".join(segment_) )


def calc(L, R):

    if L == R:
        return [(0, 1)]

    if (len(R) - len(L)) <= 1:
        if (abs(list2int(R[len(R)-2:]) - list2int(L[len(L)-2:])) <= 10) and (R[:len(R)-2] == L[:len(L)-2]):

            R_remaind = list2int( R[len(R)-1:] )
            L_remaind = list2int( L[len(L)-1:] )

            if not (R_remaind == 0 and L_remaind == 1):
                return [(0, R_remaind - L_remaind)]
            else:
                return [(1, 1)]

    max_k_R = getMaxK( R )

    up_info = goUp(L, getUpRem(R, intervalPower(max_k_R)), max_k_R)
    down_info = goDown(R, max_k_R)

    return up_info + down_info


if __name__ == '__main__':

    debug = False

    L = 42
    R = 1024
    if not debug:
        L = list(input())
        R = list(input())

    out = calc(L, R)
    print(len(out))
    for p in out:
        print( '%s %s' % (p[0], p[1]) )