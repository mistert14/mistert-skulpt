var $builtinmodule = function(name) {
    var mod = {};
    // File-like object for network data
    var netfile = function($gbl, $loc) {
        $loc.__init__ = new Sk.builtin.func(function(self, data) {
            Sk.builtin.pyCheckArgs("file", arguments, 2, 2);
            if (data.__class__ != Sk.builtin.str) {
                throw new Sk.builtin.TypeError("data must be a string");
            };
            self.data = data.v;
            self.pos = 0;
        });
        $loc.read = new Sk.builtin.func(function(self, size) {
            Sk.builtin.pyCheckArgs("read", arguments, 1, 2);
            if (size !== undefined) {
                if (!Sk.builtin.checkInt(size)) {
                    throw new Sk.builtin.TypeError("size must be an int");
                }
                size = Sk.builtin.asnum$(size);
                if (size < 0) {
                    size = self.data.length;
                }
            }
            else {
                size = self.data.length;
            }
            if (self.pos + size > self.data.length) {
                size = self.data.length - self.pos;
            }
            var str = new Sk.builtin.str(self.data.substr(self.pos, size));
            self.pos += size;
            return str;
        });
        var readline_ = function(self, size) {
            if (size !== undefined) {
                if (!Sk.builtin.checkInt(size)) {
                    throw new Sk.builtin.TypeError("size must be an int");
                }
                size = Sk.builtin.asnum$(size);
                if (size < 0) {
                    size = self.data.length;
                }
            }
            else {
                size = self.data.length;
            }
            var nl = self.data.indexOf("", self.pos);
            if (nl !== -1) {
                nl -= self.pos;
                if (size > nl) {
                    size = nl + 1;
                }
            } 
            if (self.pos + size > self.data.length) {
                size = self.data.length - self.pos;
            }
            var str = new Sk.builtin.str(self.data.substr(self.pos, size));
            self.pos += size;
            return str;
        };
        $loc.readline = new Sk.builtin.func(function(self, size) {
            Sk.builtin.pyCheckArgs("readline", arguments, 1, 2);
            return readline_(self, size);
        });
        $loc.readlines = new Sk.builtin.func(function(self, sizehint) {
            Sk.builtin.pyCheckArgs("readlines", arguments, 1, 2);
            // ignore sizehint
            var result = [];
            var line = readline_(self);
            while (line != Sk.builtin.str.$emptystr) {
                result.push(line);
                line = readline_(self);
            }
            return new Sk.builtin.list(result);
        });
        $loc.__iter__ = new Sk.builtin.func(function(self) {
            var ret =
                {
                    tp$iter: function() { return ret; },
                    $obj: self,
                    tp$iternext: function()
                    {
                        var line = readline_(ret.$obj);
                        if (line == Sk.builtin.str.$emptystr) {
                            return undefined;
                        }
                        return line;
                    }
                };
            return ret;
        });
    };
    mod.NetFile = Sk.misceval.buildClass(mod, netfile, 'NetFile', []);
    // URL open method
    mod.urlopen = new Sk.builtin.func(function(url, data, timeout) {
        Sk.builtin.pyCheckArgs("urlopen", arguments, 1, 3);
        if (!Sk.builtin.checkString(url)) {
            throw new Sk.builtin.TypeError("URL must be a string");
        };
        if (data === undefined) {
            data = null;
        };
        // if ((data != null) && !Sk.builtin.checkString(data)) {
        // throw new Sk.builtin.TypeError("data must be a string or None");
        // };
        if (data !== null) {
            throw new Sk.builtin.TypeError("currently, data must be None");
        };
        if (timeout === undefined) {
            // timeout in seconds
            timeout = 5;
        };
        if (!Sk.builtin.checkNumber(timeout)) {
            throw new Sk.builtin.TypeError("timeout must be a number");
        };
        var jsurl = Sk.ffi.unwrapo(url);
        var settings = {
            async: false,
            error: function(jqXHR, textStatus, errorThrown) {
                throw new Sk.builtin.IOError("unable to open '" + jsurl + "' (" + errorThrown + ")");
            },
            success: function(data, textStatus, jqXHR) {
            },
            timeout: timeout * 1000
        };
        
        if (data !== null) {
            settings.data = Sk.ffi.unwrapo(data);
            settings.type = "POST";
        };
        var response = $.ajax(jsurl, settings).responseText;
        // Reset timeout in case network transfer took a long time
        Sk.setExecStartNow(true);
        return Sk.misceval.callsim(mod.NetFile, new Sk.builtin.str(response));
    });
    return mod;
};

