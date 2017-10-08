from .setup import *

import numpy

class tmat3x3:
    def __init__(self, *args, **kw):
        self.dtype = kw.get("dtype", default_dtype)
        
        self.col_type = tvec3
        self.row_type = tvec3

        if len(args) == 1:
            if type(args[0]) == numpy.matrixlib.defmatrix.matrix and args[0].size == 4 and args[0].shape == (2,2):
                self.value = args[0].copy()
                
            if isinstance(args[0], tmat3x3) or isinstance(args[0], tmat4x3) or\
               isinstance(args[0], tmat3x4) or isinstance(args[0], tmat4x4):
                self.value = args[0].value[:3,:3]
                
            elif isinstance(args[0], tmat3x2) or isinstance(args[0], tmat4x2):
                self.value = numpy.matrix([tuple(args[0][0])+(0,),
                              tuple(args[0][1])+(0,),
                              tuple(args[0][2])+(1,)], dtype=self.dtype)

            elif isinstance(args[0], tmat2x3) or isinstance(args[0], tmat2x4):
                self.value = numpy.matrix([tuple(args[0][0]),
                              tuple(args[0][1]),
                              (0, 0, 1)], dtype=self.dtype)

            elif isinstance(args[0], tmat2x2):
                self.value = numpy.matrix([tuple(args[0][0])+(0,),
                              tuple(args[0][1])+(0,),
                              (0, 0, 1)], dtype=self.dtype)
                
            elif type(args[0]) in dtypes:
                self.value = numpy.matrix([(args[0],0, 0),
                              (0,args[0], 0),
                              (0,0, args[0])], dtype=self.dtype)

            elif type(args[0]) in ltypes:
                self.__init__(*args[0])

        elif len(args) == 3:
            self.value = numpy.matrix([(args[0]),
                              (args[1]),
                              (args[2])], dtype=self.dtype)
##            if isinstance(args[0], self.col_type) and isinstance(args[1], self.col_type) and isinstance(args[2], self.col_type):
##                self.value = [(args[0]),
##                              self.col_type(args[1]),
##                              self.col_type(args[2])]

        elif len(args) == 9:
            self.value = numpy.matrix([(args[:3]),
                          (args[3:6]),
                          (args[6:])], dtype=self.dtype)
##            for arg in args:
##                if not type(arg) in dtypes:
##                    raise TypeError("unsupported type {} for tmat3x3()".format(arg))
##
##            self.value = [self.col_type(*args[:3]),
##                          self.col_type(*args[3:6]),
##                          self.col_type(*args[6:])]
                
        else:
            self.value = numpy.matrix([(1,0,0),
                          (0,1,0),
                          (0,0,1)], dtype=self.dtype)


    def __setitem__(self, *args, **kw):
        return self.value.__setitem__(*args, **kw)

    def length(self):
        return 3
    __len__ = length

    glm_type = GLM_MAT
    shape = GLM_MAT3x3

    def __eq__(self, value):
        if isinstance(value, tmat3x3):
            return (self[0] == value[0] and self[1] == value[1] and self[2] == value[2])
        else:
            try:
                return (self[0] == value[0] and self[1] == value[1] and self[2] == value[2])
            except:
                raise TypeError("unsupported operand type(s) for ==: 'tmat3x3' and '{}'".format(type_to_str(type(value))))

    def __ne__(self, value):
        if isinstance(value, tmat3x3):
            return (self[0] != value[0] or self[1] != value[1] or self[2] != value[2])
        else:
            try:
                return (self[0] != value[0] or self[1] != value[1] or self[2] != value[2])
            except:
                raise TypeError("unsupported operand type(s) for !=: 'tmat3x3' and '{}'".format(type_to_str(type(value))))

    def __add__(self, value):
        try:
            return tmat3x3(self.value + value)
        except:
            raise TypeError("unsupported operand type(s) for +: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            return tmat3x3(self[0] + value,
##                         self[1] + value,
##                           self[2] + value)
##        elif isinstance(value, tmat3x3):
##            return tmat3x3(self[0] + value[0],
##                         self[1] + value[1],
##                           self[2] + value[2])
##        else:
##            try:
##                return tmat3x3(self[0] + value[0],
##                         self[1] + value[1],
##                               self[2] + value[2])
##            except:
##                raise TypeError("unsupported operand type(s) for +: 'tmat3x3' and '{}'".format(type_to_str(type(value))))

    __radd__ = __add__

    def __sub__(self, value):
        try:
            return tmat3x3(self.value - value)
        except:
            raise TypeError("unsupported operand type(s) for -: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            return tmat3x3(self[0] - value,
##                         self[1] - value,
##                           self[2] - value)
##        elif isinstance(value, tmat3x3):
##            return tmat3x3(self[0] - value[0],
##                         self[1] - value[1],
##                           self[2] - value[2])
##        else:
##            try:
##                return tmat3x3(self[0] - value[0],
##                         self[1] - value[1],
##                               self[2] - value[2])
##            except:
##                raise TypeError("unsupported operand type(s) for -: 'tmat3x3' and '{}'".format(type_to_str(type(value))))

    def __rsub__(self, value):
        try:
            return tmat3x3(value - self.value)
        except:
            raise TypeError("unsupported operand type(s) for -: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            return tmat3x3(value - self[0],
##                         value - self[1],
##                           value - self[2])
##        elif isinstance(value, tmat3x3):
##            return tmat3x3(value[0] - self[0],
##                         value[1] - self[1],
##                           value[2] - self[2])
##        else:
##            try:
##                return tmat3x3(value[0] - self[0],
##                         value[1] - self[1],
##                               value[2] - self[2])
##            except:
##                raise TypeError("unsupported operand type(s) for -: 'tmat3x3' and '{}'".format(type_to_str(type(value))))

    def __mul__(self, value):
        try:
            if hasattr(value, "__rmul__"):
                rmul = value.__rmul__
                
            if hasattr(value, "glm_type") and value.glm_type == GLM_MAT:
                value = value.value
                
            if isinstance(value, self.row_type):
                return self.row_type(value.arr.reshape(3) * self.value)
            if type(value) == numpy.ndarray:
                return self.row_type(value.reshape(3) * self.value)

            if type(value) == numpy.matrixlib.defmatrix.matrix:
                if value.shape == (2,3):
                    return tmat2x3(value * self.value)
                if value.shape == (3,3):
                    return tmat3x3(value * self.value)
                if value.shape == (4,3):
                    return tmat4x3(value * self.value)
            
            return rmul(self)
            
        except:
            raise TypeError("unsupported operand type(s) for *: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            return tmat3x3(self[0] * value,
##                         self[1] * value,
##                           self[2] * value)
##        elif isinstance(value, self.row_type):
##            m = self
##            v = value
##            return self.col_type(m[0][0] * v.x + m[1][0] * v.y + m[2][0] * v.z,
##			m[0][1] * v.x + m[1][1] * v.y + m[2][1] * v.z,
##			m[0][2] * v.x + m[1][2] * v.y + m[2][2] * v.z)
##        elif isinstance(value, tmat3x3):
##            m1 = self
##            m2 = value
##            SrcA00 = m1[0][0]
##            SrcA01 = m1[0][1]
##            SrcA02 = m1[0][2]
##            SrcA10 = m1[1][0]
##            SrcA11 = m1[1][1]
##            SrcA12 = m1[1][2]
##            SrcA20 = m1[2][0]
##            SrcA21 = m1[2][1]
##            SrcA22 = m1[2][2]
##
##            SrcB00 = m2[0][0]
##            SrcB01 = m2[0][1]
##            SrcB02 = m2[0][2]
##            SrcB10 = m2[1][0]
##            SrcB11 = m2[1][1]
##            SrcB12 = m2[1][2]
##            SrcB20 = m2[2][0]
##            SrcB21 = m2[2][1]
##            SrcB22 = m2[2][2]
##
##            Result = tmat3x3(0)
##            Result[0][0] = SrcA00 * SrcB00 + SrcA10 * SrcB01 + SrcA20 * SrcB02
##            Result[0][1] = SrcA01 * SrcB00 + SrcA11 * SrcB01 + SrcA21 * SrcB02
##            Result[0][2] = SrcA02 * SrcB00 + SrcA12 * SrcB01 + SrcA22 * SrcB02
##            Result[1][0] = SrcA00 * SrcB10 + SrcA10 * SrcB11 + SrcA20 * SrcB12
##            Result[1][1] = SrcA01 * SrcB10 + SrcA11 * SrcB11 + SrcA21 * SrcB12
##            Result[1][2] = SrcA02 * SrcB10 + SrcA12 * SrcB11 + SrcA22 * SrcB12
##            Result[2][0] = SrcA00 * SrcB20 + SrcA10 * SrcB21 + SrcA20 * SrcB22
##            Result[2][1] = SrcA01 * SrcB20 + SrcA11 * SrcB21 + SrcA21 * SrcB22
##            Result[2][2] = SrcA02 * SrcB20 + SrcA12 * SrcB21 + SrcA22 * SrcB22
##            return Result
##        
##        elif isinstance(value, tmat2x3):
##            m1 = self
##            m2 = value
##            return tmat2x3(m1[0][0] * m2[0][0] + m1[1][0] * m2[0][1] + m1[2][0] * m2[0][2],
##			m1[0][1] * m2[0][0] + m1[1][1] * m2[0][1] + m1[2][1] * m2[0][2],
##			m1[0][2] * m2[0][0] + m1[1][2] * m2[0][1] + m1[2][2] * m2[0][2],
##			m1[0][0] * m2[1][0] + m1[1][0] * m2[1][1] + m1[2][0] * m2[1][2],
##			m1[0][1] * m2[1][0] + m1[1][1] * m2[1][1] + m1[2][1] * m2[1][2],
##			m1[0][2] * m2[1][0] + m1[1][2] * m2[1][1] + m1[2][2] * m2[1][2])
##        elif isinstance(value, tmat4x3):
##            m1 = self
##            m2 = value
##            return tmat4x3(m1[0][0] * m2[0][0] + m1[1][0] * m2[0][1] + m1[2][0] * m2[0][2],
##			m1[0][1] * m2[0][0] + m1[1][1] * m2[0][1] + m1[2][1] * m2[0][2],
##			m1[0][2] * m2[0][0] + m1[1][2] * m2[0][1] + m1[2][2] * m2[0][2],
##			m1[0][0] * m2[1][0] + m1[1][0] * m2[1][1] + m1[2][0] * m2[1][2],
##			m1[0][1] * m2[1][0] + m1[1][1] * m2[1][1] + m1[2][1] * m2[1][2],
##			m1[0][2] * m2[1][0] + m1[1][2] * m2[1][1] + m1[2][2] * m2[1][2],
##			m1[0][0] * m2[2][0] + m1[1][0] * m2[2][1] + m1[2][0] * m2[2][2],
##			m1[0][1] * m2[2][0] + m1[1][1] * m2[2][1] + m1[2][1] * m2[2][2],
##			m1[0][2] * m2[2][0] + m1[1][2] * m2[2][1] + m1[2][2] * m2[2][2],
##			m1[0][0] * m2[3][0] + m1[1][0] * m2[3][1] + m1[2][0] * m2[3][2],
##			m1[0][1] * m2[3][0] + m1[1][1] * m2[3][1] + m1[2][1] * m2[3][2],
##			m1[0][2] * m2[3][0] + m1[1][2] * m2[3][1] + m1[2][2] * m2[3][2])
##        else:
##            raise TypeError("unsupported operand type(s) for *: 'tmat3x3' and '{}'".format(type_to_str(type(value))))

    def __rmul__(self, value):
        try:
            if (hasattr(value, "glm_type") and value.glm_type == GLM_MAT):
                value = value.value
                
            if isinstance(value, self.col_type):
                return self.row_type(self.value * value.arr.reshape(3,1))
            if type(value) == numpy.ndarray:
                return self.row_type(self.value * value.reshape(3,1))

            if type(value) == numpy.matrixlib.defmatrix.matrix:
                if value.shape == (2,3):
                    return tmat2x3(self.value * value)
                if value.shape == (3,3):
                    return tmat3x3(self.value * value)
                if value.shape == (4,3):
                    return tmat4x3(self.value * value)
            
            return tmat3x3(self.value * value)
            
        except:
            raise TypeError("unsupported operand type(s) for *: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            return tmat3x3(self[0] * value,
##                         self[1] * value,
##                           self[2] * value)
##        elif isinstance(value, self.col_type):
##            m = self
##            v = value
##            return self.row_type(m[0][0] * v.x + m[0][1] * v.y + m[0][2] * v.z,
##			m[1][0] * v.x + m[1][1] * v.y + m[1][2] * v.z,
##			m[2][0] * v.x + m[2][1] * v.y + m[2][2] * v.z)
##        elif isinstance(value, tmat3x3):
##            m1 = self
##            m2 = value
##            SrcA00 = m1[0][0]
##            SrcA01 = m1[0][1]
##            SrcA02 = m1[0][2]
##            SrcA10 = m1[1][0]
##            SrcA11 = m1[1][1]
##            SrcA12 = m1[1][2]
##            SrcA20 = m1[2][0]
##            SrcA21 = m1[2][1]
##            SrcA22 = m1[2][2]
##
##            SrcB00 = m2[0][0]
##            SrcB01 = m2[0][1]
##            SrcB02 = m2[0][2]
##            SrcB10 = m2[1][0]
##            SrcB11 = m2[1][1]
##            SrcB12 = m2[1][2]
##            SrcB20 = m2[2][0]
##            SrcB21 = m2[2][1]
##            SrcB22 = m2[2][2]
##
##            Result = tmat3x3(0)
##            Result[0][0] = SrcA00 * SrcB00 + SrcA10 * SrcB01 + SrcA20 * SrcB02
##            Result[0][1] = SrcA01 * SrcB00 + SrcA11 * SrcB01 + SrcA21 * SrcB02
##            Result[0][2] = SrcA02 * SrcB00 + SrcA12 * SrcB01 + SrcA22 * SrcB02
##            Result[1][0] = SrcA00 * SrcB10 + SrcA10 * SrcB11 + SrcA20 * SrcB12
##            Result[1][1] = SrcA01 * SrcB10 + SrcA11 * SrcB11 + SrcA21 * SrcB12
##            Result[1][2] = SrcA02 * SrcB10 + SrcA12 * SrcB11 + SrcA22 * SrcB12
##            Result[2][0] = SrcA00 * SrcB20 + SrcA10 * SrcB21 + SrcA20 * SrcB22
##            Result[2][1] = SrcA01 * SrcB20 + SrcA11 * SrcB21 + SrcA21 * SrcB22
##            Result[2][2] = SrcA02 * SrcB20 + SrcA12 * SrcB21 + SrcA22 * SrcB22
##            return Result
##        
##        elif isinstance(value, tmat2x3):
##            m1 = self
##            m2 = value
##            return tmat2x3(m1[0][0] * m2[0][0] + m1[1][0] * m2[0][1] + m1[2][0] * m2[0][2],
##			m1[0][1] * m2[0][0] + m1[1][1] * m2[0][1] + m1[2][1] * m2[0][2],
##			m1[0][2] * m2[0][0] + m1[1][2] * m2[0][1] + m1[2][2] * m2[0][2],
##			m1[0][0] * m2[1][0] + m1[1][0] * m2[1][1] + m1[2][0] * m2[1][2],
##			m1[0][1] * m2[1][0] + m1[1][1] * m2[1][1] + m1[2][1] * m2[1][2],
##			m1[0][2] * m2[1][0] + m1[1][2] * m2[1][1] + m1[2][2] * m2[1][2])
##        elif isinstance(value, tmat4x3):
##            m1 = self
##            m2 = value
##            return tmat4x3(m1[0][0] * m2[0][0] + m1[1][0] * m2[0][1] + m1[2][0] * m2[0][2],
##			m1[0][1] * m2[0][0] + m1[1][1] * m2[0][1] + m1[2][1] * m2[0][2],
##			m1[0][2] * m2[0][0] + m1[1][2] * m2[0][1] + m1[2][2] * m2[0][2],
##			m1[0][0] * m2[1][0] + m1[1][0] * m2[1][1] + m1[2][0] * m2[1][2],
##			m1[0][1] * m2[1][0] + m1[1][1] * m2[1][1] + m1[2][1] * m2[1][2],
##			m1[0][2] * m2[1][0] + m1[1][2] * m2[1][1] + m1[2][2] * m2[1][2],
##			m1[0][0] * m2[2][0] + m1[1][0] * m2[2][1] + m1[2][0] * m2[2][2],
##			m1[0][1] * m2[2][0] + m1[1][1] * m2[2][1] + m1[2][1] * m2[2][2],
##			m1[0][2] * m2[2][0] + m1[1][2] * m2[2][1] + m1[2][2] * m2[2][2],
##			m1[0][0] * m2[3][0] + m1[1][0] * m2[3][1] + m1[2][0] * m2[3][2],
##			m1[0][1] * m2[3][0] + m1[1][1] * m2[3][1] + m1[2][1] * m2[3][2],
##			m1[0][2] * m2[3][0] + m1[1][2] * m2[3][1] + m1[2][2] * m2[3][2])
##        else:
##            raise TypeError("unsupported operand type(s) for *: 'tmat3x3' and '{}'".format(type_to_str(type(value))))

    def __truediv__(self, value):
        try:
            if isinstance(value, self.row_type):
                return self.row_type(inverse(self) * value)
            return self * inverse(value)
        except:
            try:
                return value.__rdiv__(self)
            except:
                raise TypeError("unsupported operand type(s) for /: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            value = float(value)
##            return tmat3x3(self[0] / value,
##                         self[1] / value,
##                           self[2] / value)
##        elif isinstance(value, self.row_type):
##            return inverse(self) * value
##        elif isinstance(value, tmat3x3):
##            return self * inverse(value)
##        else:
##            try:
##                return self * inverse(value)
##            except:
##                raise TypeError("unsupported operand type(s) for /: 'tmat3x3' and '{}'".format(type_to_str(type(value))))

    def __rtruediv__(self, value):
        try:
            if isinstance(value, self.col_type):
                return self.col_type(value * inverse(self))
            return value * inverse(self)
        except:
            raise TypeError("unsupported operand type(s) for /: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            value = float(value)
##            return tmat3x3(value / self[0],
##                         value / self[1],
##                           value / self[2])
##        elif isinstance(value, self.col_type):
##            return value * inverse(self)
##        elif isinstance(value, tmat3x3):
##            return inverse(self) * value
##        else:
##            try:
##                return value * inverse(self)
##            except:
##                raise TypeError("unsupported operand type(s) for /: 'tmat3x3' and '{}'".format(type_to_str(type(value))))

    __div__ = __truediv__

    __rdiv__ = __rtruediv__

    # __i*__ functions
    def __iadd__(self, value):
        try:
            self.value += value
        except:
            raise TypeError("unsupported operand type(s) for +=: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            self[0] += value
##            self[1] += value
##            self[2] += value
##        elif isinstance(value, tmat3x3):
##            self[0] += value[0]
##            self[1] += value[1]
##            self[2] += value[2]
##        else:
##            try:
##                self[0] += value[0]
##                self[1] += value[1]
##                self[2] += value[2]
##            except:
##                raise TypeError("unsupported operand type(s) for +=: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
        return self

    def __isub__(self, value):
        try:
            self.value -= value
        except:
            raise TypeError("unsupported operand type(s) for -=: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            self[0] -= value
##            self[1] -= value
##            self[2] -= value
##        elif isinstance(value, tmat3x3):
##            self[0] -= value[0]
##            self[1] -= value[1]
##            self[2] -= value[2]
##        else:
##            try:
##                self[0] -= value[0]
##                self[1] -= value[1]
##                self[2] -= value[2]
##            except:
##                raise TypeError("unsupported operand type(s) for -=: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
        return self

    def __imul__(self, value):
        try:
            self.value *= value
        except:
            raise TypeError("unsupported operand type(s) for *=: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            self[0] *= value
##            self[1] *= value
##            self[2] *= value
##            print(value)
##        elif isinstance(value, tmat3x3):
##            self.value = (self * value).value
##        else:
##            try:
##                self[0] *= value[0]
##                self[1] *= value[1]
##                self[2] *= value[2]
##            except:
##                raise TypeError("unsupported operand type(s) for *=: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
        return self

    def __itruediv__(self, value):
        try:
            self.value *= inverse(value)
        except:
            raise TypeError("unsupported operand type(s) for +=: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
##        if type(value) in dtypes:
##            self[0] /= float(value)
##            self[1] /= float(value)
##            self[2] /= float(value)
##        elif isinstance(value, tmat3x3):
##            self *= inverse(value)
##        else:
##            try:
##                self *= inverse(value)
##            except:
##                raise TypeError("unsupported operand type(s) for /=: 'tmat3x3' and '{}'".format(type_to_str(type(value))))
        return self

    __idiv__ = __itruediv__
    
    def __pos__(self):
        return self

    def __neg__(self):
        return tmat3x3(-self.value)

    def __abs__(self):
        return tmat3x3(abs(self.value))

##    def __invert__(self):
##        return invert(self)

    def __getitem__(self, key):
        if type(key) == slice:
            raise TypeError("tmat3x3 doesn't support slices")
        elif type(key) == tuple and len(key) == 2:
            return self.value[key[0], key[1]]
        else:
            if key in (0,-3):
                return self.col_type(self.value[0])
            elif key in (1,-2):
                return self.col_type(self.value[1])
            elif key in (2,-1):
                return self.col_type(self.value[2])
            else:
                raise IndexError("tmat3x3 index out of range")

    def __array__(self, *args, **kw):
        return numpy.matrix(self.value, *args, **kw)

##    def __setitem__(self, key, value):
##        if type(key) == slice:
##            raise TypeError("tmat3x3 doesn't support slices")
##        else:
##            if key in (0,-3):
##                self.value[0] = value
##            elif key in (1,-2):
##                self.value[1] = value
##            elif key in (2,-1):
##                self.value[2] = value
##            else:
##                raise IndexError("tmat3x3 index out of range")

    def __str__(self):
        return "tmat3x3( {}, {}, {},\n         {}, {}, {},\n         {}, {}, {} )".format(self[0][0], self[0][1], self[0][2],
                                                                             self[1][0], self[1][1], self[1][2],
                                                                             self[2][0], self[2][1], self[2][2])

    __repr__ = __str__

from .func_matrix import *
from .type_vec2 import tvec2
from .type_vec3 import tvec3
from .type_vec4 import tvec4

from .type_mat2x2 import tmat2x2
from .type_mat2x3 import tmat2x3
from .type_mat2x4 import tmat2x4

from .type_mat3x2 import tmat3x2
from .type_mat3x4 import tmat3x4

from .type_mat4x2 import tmat4x2
from .type_mat4x3 import tmat4x3
from .type_mat4x4 import tmat4x4
