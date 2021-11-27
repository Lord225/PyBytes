import sys, os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pybytes.common.aritmetic import Flags
import unittest 
from pybytes import *
import numpy as np


class TestConstruct(unittest.TestCase):
    def test_from_int(self):
        value = Binary(0)
        self.assertTrue((value._data==np.array([0], dtype=np.uint8)).all())
        self.assertEqual(value._len, 1)

        value = Binary(1)
        self.assertTrue((value._data==np.array([1], dtype=np.uint8)).all())
        self.assertEqual(value._len, 1)

        value = Binary(255)
        self.assertTrue((value._data==np.array([255], dtype=np.uint8)).all())
        self.assertEqual(value._len, 8)

        value = Binary(256)
        self.assertTrue((value._data==np.array([0, 1], dtype=np.uint8)).all())
        self.assertEqual(value._len, 9)
    def test_from_int_signed(self):
        value = Binary(-1)
        self.assertEqual(value.sign_behavior(), 'signed')
        self.assertEqual(str(value), '11')

        value = Binary(-2)
        self.assertEqual(value.sign_behavior(), 'signed')
        self.assertEqual(str(value), '110')
        
        value = Binary(-256)
        self.assertEqual(value.sign_behavior(), 'signed')
        self.assertEqual(str(value), '1100000000')

        value = Binary(-1, bit_lenght=9)
        self.assertEqual(value.sign_behavior(), 'signed')
        self.assertEqual(str(value), '111111111')

        value = Binary(-1, bit_lenght=2)
        self.assertEqual(value.sign_behavior(), 'signed')
        self.assertEqual(str(value), '11')
    def test_from_int_magnitute(self):
        value = Binary(-1, sign_behavior='magnitude')
        self.assertEqual(value.sign_behavior(), 'magnitude')
        self.assertEqual(str(value), '11')

        value = Binary(-2, sign_behavior='magnitude')
        self.assertEqual(value.sign_behavior(), 'magnitude')
        self.assertEqual(str(value), '110')

        value = Binary(-3, sign_behavior='magnitude')
        self.assertEqual(value.sign_behavior(), 'magnitude')
        self.assertEqual(str(value), '111')
        
        value = Binary(-256, sign_behavior='magnitude')
        self.assertEqual(value.sign_behavior(), 'magnitude')
        self.assertEqual(str(value), '1100000000')

        value = Binary(-1, bit_lenght=9, sign_behavior='magnitude')
        self.assertEqual(value.sign_behavior(), 'magnitude')
        self.assertEqual(str(value), '100000001')
        
    def test_from_string(self):
        value = Binary("0000")
        self.assertTrue((value._data==np.array([0], dtype=np.uint8)).all())
        self.assertEqual(value._len, 4)

        value = Binary("0   1 1 0")
        self.assertTrue((value._data==np.array([6], dtype=np.uint8)).all())
        self.assertEqual(value._len, 4)

        value = Binary("FF")
        self.assertTrue((value._data==np.array([255], dtype=np.uint8)).all())
        self.assertEqual(value._len, 8)

        value = Binary("0b1111")
        self.assertTrue((value._data==np.array([15], dtype=np.uint8)).all())
        self.assertEqual(value._len, 4)

        value = Binary("0xFF")
        self.assertTrue((value._data==np.array([255], dtype=np.uint8)).all())
        self.assertEqual(value._len, 8)
    def test_from_arrays(self):
        value = Binary([True, True, 0, 0.0])
        self.assertEqual(value, "1100")
        self.assertEqual(value._len, 4)

        value = Binary(0,bytes_lenght=2)
        self.assertEqual(value, 0)
        self.assertEqual(value._len, 16)

        value = Binary(np.array([1, 0]),bytes_lenght=2)
        self.assertEqual(value, 1)
        self.assertEqual(len(value), 16)

    def test_rises(self):
        with self.assertRaises(Exception):
            Binary(0, bytes_lenght=2, bit_lenght=1)


class TestCompare(unittest.TestCase):
    def test_unsigned_cmps(self):
        TESTDATA = [1, 2, 256, 255, 1024, 0]
        for x in TESTDATA:
            for y in TESTDATA:
                xx = Binary(x)
                yy = Binary(y)

                self.assertEqual(xx==yy, x==y)
                self.assertEqual(xx!=yy, x!=y)
                self.assertEqual(xx>yy, x>y)
                self.assertEqual(xx>=yy, x>=y)
                self.assertEqual(xx<yy, x<y)
                self.assertEqual(xx<=yy, x<=y)

                self.assertEqual(x==yy, x==y)
                self.assertEqual(x!=yy, x!=y)
                self.assertEqual(x>yy, x>y)
                self.assertEqual(x>=yy, x>=y)
                self.assertEqual(x<yy, x<y)
                self.assertEqual(x<=yy, x<=y)

                self.assertEqual(xx==y, x==y)
                self.assertEqual(xx!=y, x!=y)
                self.assertEqual(xx>y, x>y)
                self.assertEqual(xx>=y, x>=y)
                self.assertEqual(xx<y, x<y)
                self.assertEqual(xx<=y, x<=y)
    def test_signed_cmps(self):
        TESTDATA = [1, 2, 256, 255, 1024, 0, -1, -2, -256, -255, -1024]
        for x in TESTDATA:
            for y in TESTDATA:
                xx = Binary(x, sign_behavior='signed')
                yy = Binary(y, sign_behavior='signed')

                self.assertEqual(xx==yy, x==y)
                self.assertEqual(xx!=yy, x!=y)
                self.assertEqual(xx>yy, x>y)
                self.assertEqual(xx>=yy, x>=y)
                self.assertEqual(xx<yy, x<y)
                self.assertEqual(xx<=yy, x<=y)

                self.assertEqual(x==yy, x==y)
                self.assertEqual(x!=yy, x!=y)
                self.assertEqual(x>yy, x>y)
                self.assertEqual(x>=yy, x>=y)
                self.assertEqual(x<yy, x<y)
                self.assertEqual(x<=yy, x<=y)

                self.assertEqual(xx==y, x==y)
                self.assertEqual(xx!=y, x!=y)
                self.assertEqual(xx>y, x>y)
                self.assertEqual(xx>=y, x>=y)
                self.assertEqual(xx<y, x<y)
                self.assertEqual(xx<=y, x<=y)
    def test_magnitute_cmps(self):
        TESTDATA = [1, 2, 256, 255, 1024, 0, -1, -2, -256, -255, -1024]
        for x in TESTDATA:
            for y in TESTDATA:
                xx = Binary(x, sign_behavior='magnitude')
                yy = Binary(y, sign_behavior='magnitude')

                self.assertEqual(xx==yy, x==y)
                self.assertEqual(xx!=yy, x!=y)
                self.assertEqual(xx>yy, x>y)
                self.assertEqual(xx>=yy, x>=y)
                self.assertEqual(xx<yy, x<y)
                self.assertEqual(xx<=yy, x<=y)

                self.assertEqual(x==yy, x==y)
                self.assertEqual(x!=yy, x!=y)
                self.assertEqual(x>yy, x>y)
                self.assertEqual(x>=yy, x>=y)
                self.assertEqual(x<yy, x<y)
                self.assertEqual(x<=yy, x<=y)

                self.assertEqual(xx==y, x==y)
                self.assertEqual(xx!=y, x!=y)
                self.assertEqual(xx>y, x>y)
                self.assertEqual(xx>=y, x>=y)
                self.assertEqual(xx<y, x<y)
                self.assertEqual(xx<=y, x<=y)
    def test_mixed_cmps(self):
        SIGNS = ['unsigned', 'signed', 'magnitude']
        TESTDATA = [0, 1, 2, 256, 255, 1024, 0, -1, -2, -256, -255, -1024]
        for x_s in SIGNS:
            for y_s in SIGNS:
                for x in TESTDATA:
                    for y in TESTDATA:
                        if x < 0 and x_s == 'unsigned':
                            continue
                        if y < 0 and y_s == 'unsigned':
                            continue
                        xx = Binary(x, sign_behavior=x_s)
                        yy = Binary(y, sign_behavior=y_s)

                        self.assertEqual(xx==yy, x==y)
                        self.assertEqual(xx!=yy, x!=y)
                        self.assertEqual(xx>yy, x>y)
                        self.assertEqual(xx>=yy, x>=y)
                        self.assertEqual(xx<yy, x<y)
                        self.assertEqual(xx<=yy, x<=y)

                        self.assertEqual(x==yy, x==y)
                        self.assertEqual(x!=yy, x!=y)
                        self.assertEqual(x>yy, x>y)
                        self.assertEqual(x>=yy, x>=y)
                        self.assertEqual(x<yy, x<y)
                        self.assertEqual(x<=yy, x<=y)

                        self.assertEqual(xx==y, x==y)
                        self.assertEqual(xx!=y, x!=y)
                        self.assertEqual(xx>y, x>y)
                        self.assertEqual(xx>=y, x>=y)
                        self.assertEqual(xx<y, x<y)
                        self.assertEqual(xx<=y, x<=y)

class TestAssigns(unittest.TestCase):    
    def test_assign_int_key(self):
        x = Binary("0000 0000")
        x[0] = True
        self.assertEqual(str(x), "00000001")
        x[1] = True
        self.assertEqual(str(x), "00000011")
        x[-1] = True
        self.assertEqual(str(x), "10000011")
        x[0] = False
        self.assertEqual(str(x), "10000010")
    def test_read_int_key(self):
        x = Binary("10000010")
        self.assertEqual(x[0], False)
        self.assertEqual(x[1], True)
        self.assertEqual(x[2], False)

        x = Binary("1 10000010")
        self.assertEqual(x[7], True)
        self.assertEqual(x[8], True)
        self.assertEqual(x[-1], True)
    def test_read_slice_key(self):
        x = Binary("10000010")
        self.assertEqual(x[0:3], "010")
        self.assertEqual(x[:3], "010")
        self.assertEqual(x[-3:], "100")
        
        x = Binary("1 10000010")
        self.assertEqual(x[:-3], "000010")
        self.assertEqual(x[-5:-1], '1000')
        self.assertEqual(x[5:7], '00')
    def test_assign_slice_key(self):
        x = Binary("10000010")
        y = Binary("101")
        x[:3] = y
        self.assertEqual(str(x), "10000101")

        x[4:] = 1
        self.assertEqual(str(x), "11110101")

        x[:4] = 0
        self.assertEqual(str(x), "11110000")

        x[1:4] = "101"
        self.assertEqual(str(x), "11111010")

        x[:] = False
        self.assertEqual(str(x), "00000000")

        x[:] = False
        self.assertEqual(str(x), "00000000")    
    def test_array_assign(self):
        x = Binary("00000000")
        x[[1,3,5]] = True
        self.assertEqual(str(x), "00101010")
        x[[-1,7,0]] = True
        self.assertEqual(str(x), "10101011")
    def test_illegal_assigns(self):
        x = Binary("10000010")
        with self.assertRaises(ValueError):
            x[0:1] = "1111 1111"
        with self.assertRaises(IndexError):
            x[0:100] = "11" 
        with self.assertRaises(ValueError):
            x[-100:1] = "1111 1111"
   
class LeadingTrailling(unittest.TestCase):
    def test_traling_zeros(self):
        self.assertEqual(Binary("0000 0000").trailing_zeros(), 8)
        self.assertEqual(Binary("0001 0000").trailing_zeros(), 4)
        self.assertEqual(Binary("0000 0001").trailing_zeros(), 0)
        self.assertEqual(Binary("0 0000 0000").trailing_zeros(), 9)
        self.assertEqual(Binary("1 0000 0000").trailing_zeros(), 8)
        self.assertEqual(Binary("1 0000 0001").trailing_zeros(), 0)
        self.assertEqual(Binary("1111 1111").trailing_zeros(), 0)
        self.assertEqual(Binary("0 1111 1111").trailing_zeros(), 0)
    def test_traling_ones(self):
        self.assertEqual(Binary("1111 1111").trailing_ones(), 8)
        self.assertEqual(Binary("0000 1111").trailing_ones(), 4)
        self.assertEqual(Binary("1111 1110").trailing_ones(), 0)
        self.assertEqual(Binary("1 1111 1111").trailing_ones(), 9)
        self.assertEqual(Binary("0 1111 1111").trailing_ones(), 8)
        self.assertEqual(Binary("0 1111 1110").trailing_ones(), 0)
        self.assertEqual(Binary("0000 0000").trailing_ones(), 0)
        self.assertEqual(Binary("1 0000 0000").trailing_ones(), 0)
    def test_leading_zeros(self):
        self.assertEqual(Binary("0000 0000").leading_zeros(), 8)
        self.assertEqual(Binary("0000 1111").leading_zeros(), 4)
        self.assertEqual(Binary("0001 1111").leading_zeros(), 3)
        self.assertEqual(Binary("0111 1111").leading_zeros(), 1)
        self.assertEqual(Binary("1111 1111").leading_zeros(), 0)
        self.assertEqual(Binary("0000 0001").leading_zeros(), 7)
        self.assertEqual(Binary("0000 0000 1").leading_zeros(), 8)
        self.assertEqual(Binary("0000 0000 0").leading_zeros(), 9)
        self.assertEqual(Binary("1000 0000 0000").leading_zeros(), 0)
        self.assertEqual(Binary("0000 0000 0000").leading_zeros(), 12)
        self.assertEqual(Binary("0000 0000 1000").leading_zeros(), 8)
        self.assertEqual(Binary("0000 0001 0000").leading_zeros(), 7)
    def test_leading_ones(self):
        pass

class Operations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Binary("0000 0001")+Binary("0000 0001"), Binary("0000 0010"))
        self.assertEqual(Binary("0001")+Binary("0001"), Binary("0010"))
        self.assertEqual(Binary("1")+Binary("1"), Binary("0"))
        self.assertEqual(ops.overflowing_add(Binary("1"), Binary("1")), (Binary("0"), True))
        self.assertEqual(Binary("1 0000 0000")+Binary("0000 0001"), Binary("1 0000 0001"))
        self.assertEqual(Binary("00 1000 0000")+Binary("1000 0000"), Binary("01 0000 0000"))
        self.assertEqual(Binary("01 1000 0000")+Binary("1000 0000"), Binary("10 0000 0000"))
        self.assertEqual(Binary("11 0000 0000")+1, Binary("11 0000 0001"))
    def test_sub(self):
        self.assertEqual(Binary("0000 0001")-Binary("0000 0001"), Binary("0000 0000"))
        self.assertEqual(Binary("0000 0000")-Binary("0000 0001"), Binary("1111 1111"))
        self.assertEqual(Binary("0000 0001")-Binary("0000 0000"), Binary("0000 0001"))
        self.assertEqual(Binary("0 0000 0000")-Binary("0000 0001"), Binary("1 1111 1111"))
        self.assertEqual(Binary("1 0000 0000")-Binary("0000 0001"), Binary("0 1111 1111"))
        out, flags = ops.flaged_sub(Binary("0 0000 0000"), Binary("0 0000 0001"))
        self.assertEqual((out, list(flags)), (Binary("1 1111 1111"), list(Flags(False, False, True, True))))
        
if __name__ == '__main__':
    unittest.main()