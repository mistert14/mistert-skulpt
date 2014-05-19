var $builtinmodule = function(name) {
    var mod = {};
    var checkIndex = function(index) {
        // Check that it is a two element sequence
        if (!Sk.builtin.checkSequence(index) || index.sq$length() != 2) {
            return false;
        };
        // Check that each element is an int
        if (!Sk.builtin.checkInt(index.mp$subscript(0)) || !Sk.builtin.checkInt(index.mp$subscript(1))) {
            return false;
        };
        return true;
    };
    var matrix = function($gbl, $loc) {
        $loc.__init__ = new Sk.builtin.func(function(self, data) {
            if (Sk.builtin.checkSequence(data)) {
                self.matrix = [];
                var i, j, row, mrow, item, rowlen;
                rowlen = 0;
                for (i=0; i<data.sq$length(); i++) {
                    row = data.mp$subscript(i);
                    if (!Sk.builtin.checkSequence(row)) {
                        throw new Sk.builtin.TypeError("data must be a sequence of sequences");
                    }
                    if (rowlen === 0) {
                        rowlen = row.sq$length();
                    }
                    if (row.sq$length() != rowlen) {
                        throw new Sk.builtin.TypeError("matrix rows must be the same length");
                    }
                    mrow = [];
                    for (j=0; j<row.sq$length(); j++) {
                        item = row.mp$subscript(j);
                        if (!Sk.builtin.checkNumber(item)) {
                            throw new Sk.builtin.TypeError("matrix elements must be numbers");
                        }
                        mrow.push(Sk.builtin.asnum$(item));
                    }
                    self.matrix.push(mrow);
                }
            } else if (Object.prototype.toString.apply(data) == '[object Array]') {
                self.matrix = data;
            } else {
                throw new Sk.builtin.TypeError("data must be a sequence of sequences");
            }
            self.xdim = self.matrix.length;
            self.ydim = self.matrix[0].length;
            self.matrix_shape = new Sk.builtin.tuple([new Sk.builtin.nmber(self.xdim, Sk.builtin.nmber.int$),
                                                      new Sk.builtin.nmber(self.ydim, Sk.builtin.nmber.int$)]);
            self.__class__ = mod.Matrix;
        });
        $loc.__getitem__ = new Sk.builtin.func(function(self, idx) {
            Sk.builtin.pyCheckArgs("__getitem__", arguments, 2, 2);
            if (!checkIndex(idx))
            {
                throw new Sk.builtin.TypeError("index must be a 2 element sequence");
            }
            var i = Sk.builtin.asnum$(idx.mp$subscript(0));
            var j = Sk.builtin.asnum$(idx.mp$subscript(1));
            return new Sk.builtin.nmber(self.matrix[i][j], Sk.builtin.nmber.float$);
        });
        $loc.getrow = new Sk.builtin.func(function(self, idx) {
            Sk.builtin.pyCheckArgs("getrow", arguments, 2, 2);
            if (!Sk.builtin.checkInt(idx))
            {
                throw new Sk.builtin.TypeError("row index must be an integer");
            }
            idx = Sk.builtin.asnum$(idx);
            if ((idx < 0) || (idx >= self.xdim))
            {
                throw new Sk.builtin.ValueError("index out of bounds");
            }
            
            var row = [self.matrix[idx].slice()];
            return new Sk.misceval.callsim(mod.Matrix, row);
        });
        $loc.getcol = new Sk.builtin.func(function(self, idx) {
            Sk.builtin.pyCheckArgs("getcol", arguments, 2, 2);
            if (!Sk.builtin.checkInt(idx))
            {
                throw new Sk.builtin.TypeError("column index must be an integer");
            }
            idx = Sk.builtin.asnum$(idx);
            if ((idx < 0) || (idx >= self.ydim))
            {
                throw new Sk.builtin.ValueError("index out of bounds");
            }
            
            var i, col;
            col = [];
            for (i = 0; i < self.xdim; i++)
            {
                col.push(self.matrix[i][idx]);
            }
            col = [col];
            return new Sk.misceval.callsim(mod.Matrix, col);
        });
        $loc.__setitem__ = new Sk.builtin.func(function(self, idx, data) {
            Sk.builtin.pyCheckArgs("__setitem__", arguments, 3, 3);
            if (!checkIndex(idx))
            {
                throw new Sk.builtin.TypeError("index must be a 2 element sequence");
            }
            var i = Sk.builtin.asnum$(idx.mp$subscript(0));
            var j = Sk.builtin.asnum$(idx.mp$subscript(1));
            self.matrix[i][j] = Sk.builtin.asnum$(data);
        });
        $loc.__str__ = new Sk.builtin.func(function(self) {
            Sk.builtin.pyCheckArgs("__str__", arguments, 1, 1);
            var s = "[";
            var i, j;
            var el;
            for (i=0; i<self.xdim; i++) {
                if (i !== 0) {
                    s += " ";
                }
                s += "[";
                for (j=0; j<self.ydim; j++) {
                    // Convert float into a Skulpt float in order to use the
                    // float string conversion function.  Otherwise, the numbers
                    // will look different than other floats.
                    el = Sk.builtin.nmber(self.matrix[i][j], Sk.builtin.nmber.float$);
                    s += el.tp$str().v;
                    if (j !== self.ydim - 1) {
                        s += ", ";
                    }
                }
                s += "]";
                if (i !== self.xdim - 1) {
                    s += ",";
                }
            }
            s += "]";
            return new Sk.builtin.str(s);
        });
        $loc["__add__"] = new Sk.builtin.func(function(self, other) {
            Sk.builtin.pyCheckArgs("__add__", arguments, 2, 2);
            if (other.__class__ != mod.Matrix)
            {
                throw new Sk.builtin.TypeError("can only add matrices to matrices");
            }
            var sum = numeric.add(self.matrix, other.matrix);
            return Sk.misceval.callsim(mod.Matrix, sum);
        });
        $loc["__sub__"] = new Sk.builtin.func(function(self, other) {
            Sk.builtin.pyCheckArgs("__sub__", arguments, 2, 2);
            if (other.__class__ != mod.Matrix)
            {
                throw new Sk.builtin.TypeError("can only subtract matrices from matrices");
            }
            var diff = numeric.sub(self.matrix, other.matrix);
            return Sk.misceval.callsim(mod.Matrix, diff);
        });
        $loc["__mul__"] = new Sk.builtin.func(function(self, other) {
            Sk.builtin.pyCheckArgs("__mul__", arguments, 2, 2);
            if (other.__class__ != mod.Matrix)
            {
                throw new Sk.builtin.TypeError("can only multiply matrices with matrices");
            }
            var product = numeric.dot(self.matrix, other.matrix);
            return Sk.misceval.callsim(mod.Matrix, product);
        });
        $loc.copy = new Sk.builtin.func(function(self) {
            Sk.builtin.pyCheckArgs("copy", arguments, 1, 1);
            var copy = numeric.clone(self.matrix);
            return Sk.misceval.callsim(mod.Matrix, copy);
        });
        $loc.inverse = new Sk.builtin.func(function(self) {
            Sk.builtin.pyCheckArgs("inverse", arguments, 1, 1);
            var inv, det;
            try {
                det = numeric.det(self.matrix);
            } catch(x) {
                throw new Sk.builtin.ValueError("matrix has no inverse");
            }
            if ((self.xdim !== self.ydim) || (det === 0)) {
                throw new Sk.builtin.ValueError("matrix has no inverse");
            }
            try {
                inv = numeric.inv(self.matrix);
            } catch (x) {
                throw new Sk.builtin.ValueError("matrix has no inverse");
            }
            return Sk.misceval.callsim(mod.Matrix, inv);
        });
        $loc.transpose = new Sk.builtin.func(function(self) {
            Sk.builtin.pyCheckArgs("transpose", arguments, 1, 1);
            var transpose = numeric.transpose(self.matrix);
            return Sk.misceval.callsim(mod.Matrix, transpose);
        });
        $loc.abs = new Sk.builtin.func(function(self) {
            Sk.builtin.pyCheckArgs("abs", arguments, 1, 1);
            var abs = numeric.abs(self.matrix);
            return Sk.misceval.callsim(mod.Matrix, abs);
        });
        $loc.summation = new Sk.builtin.func(function(self) {
            Sk.builtin.pyCheckArgs("summation", arguments, 1, 1);
            var sum = numeric.sum(self.matrix);
            return new Sk.builtin.nmber(sum, Sk.builtin.nmber.float$);
        });
        $loc.scale = new Sk.builtin.func(function(self, factor) {
            Sk.builtin.pyCheckArgs("scale", arguments, 2, 2);
            if (!Sk.builtin.checkNumber(factor))
            {
                throw new Sk.builtin.TypeError("scale factor must be a number");
            }
            var scaled = numeric.clone(self.matrix);
            factor = Sk.builtin.asnum$(factor);
            var i, j;
            for (i=0; i<self.xdim; i++) {
                for (j=0; j<self.ydim; j++) {
                    scaled[i][j] *= factor;
                }
            }
            return Sk.misceval.callsim(mod.Matrix, scaled);
        });
        
        $loc.shape = new Sk.builtin.func(function(self) {
            Sk.builtin.pyCheckArgs("shape", arguments, 1, 1);
            return self.matrix_shape;
        });
        
    };
    mod.Matrix = Sk.misceval.buildClass(mod, matrix, "Matrix", []);
    mod.identity = new Sk.builtin.func(function(dimension) {
        Sk.builtin.pyCheckArgs("identity", arguments, 1, 1);
        if (!Sk.builtin.checkInt(dimension))
        {
            throw new Sk.builtin.TypeError("dimension must be an integer");
        }
        var dim = Sk.builtin.asnum$(dimension);
        return Sk.misceval.callsim(mod.Matrix, numeric.identity(dim));
    });
    return mod;
};

