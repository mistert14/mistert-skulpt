var $builtinmodule = function(name) {
    var mod = {};
    mod.file2url = new Sk.builtin.func(function(filename) {
        Sk.builtin.pyCheckArgs("file2url", arguments, 1, 1);
        if (!Sk.builtin.checkString(filename)) {
            throw new Sk.builtin.TypeError("filename must be a string");
        };
        var pattern = /^([a-zA-Z][a-zA-Z0-9]*)[_\\-]/;
        var fname = Sk.ffi.unwrapo(filename);
        var bucket = fname.match(pattern);
        if (bucket === null) {
            throw new Sk.builtin.ValueError("invalid filename: '" + fname + "'");
        };
        var url = "http://codeskulptor-" + bucket[1] + ".commondatastorage.googleapis.com/" + fname;
        return new Sk.builtin.str(url);
    });
    mod.set_timeout = new Sk.builtin.func(function(secs) {
        Sk.builtin.pyCheckArgs("set_timeout", arguments, 1, 1);
        if (!Sk.builtin.checkInt(secs)) {
            throw new Sk.builtin.TypeError("timeout must be an integer");
        };
        secs = Sk.builtin.asnum$(secs);
        Sk.setExecLimit(secs*1000);
    });
    return mod;
};
       
