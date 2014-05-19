
var input = read('src/lib/html5/__init__.js');
print("-----");
print(input);
print("-----");
Sk.configure({syspath:["src/lib/html5"], read:read, python3:false});
Sk.importMain("__init__", true);
print("-----");
    